<template>
  <div class="container mt-5">
    <h2>Adicionar ao Estoque Local</h2>
    <form @submit.prevent="handleAddStock">
      <!-- Posto de Distribuição com Pesquisa de CNES -->
      <div class="mb-3 position-relative">
        <label for="postoDistribuicao" class="form-label">Posto de Distribuição (CNES)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="postoDistribuicao" v-model="postoDistribuicaoSearch" placeholder="Digite o CNES">
          <button type="button" class="btn btn-primary" @click="searchPostoDistribuicao">Pesquisar</button>
        </div>
        <p v-if="postoDistribuicaoSearchResult" class="mt-2">{{ postoDistribuicaoSearchResult }}</p>
        <p v-if="postoDistribuicaoInfo" class="mt-2">
          CNES: {{ postoDistribuicaoInfo.cnes }}<br>
          Nome: {{ postoDistribuicaoInfo.nome }}<br>
          Endereço: {{ postoDistribuicaoInfo.endereco }}<br>
          Bairro: {{ postoDistribuicaoInfo.bairro }}<br>
          Município: {{ postoDistribuicaoInfo.municipio }}
        </p>
      </div>

      <!-- Medicamento(s) com Pesquisa de Código de Barras -->
      <div class="mb-3 position-relative">
        <label for="medicamento" class="form-label">Medicamento (Código de Barras)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="medicamento" v-model="medicamentoSearch" placeholder="Digite o Código de Barras">
          <button type="button" class="btn btn-primary" @click="searchMedicamento">Pesquisar</button>
        </div>
        <p v-if="medicamentoSearchResult" class="mt-2">{{ medicamentoSearchResult }}</p>
      </div>

      <!-- Lista de Medicamentos a Adicionar -->
      <div class="mb-3" v-if="form.medicamentos.length">
        <label class="form-label">Medicamentos a Adicionar</label>
        <ul class="list-group">
          <li v-for="(medicamento, index) in form.medicamentos" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
            {{ medicamento.produto }} ({{ medicamento.codigo_barra }})
            <div>
              <input type="number" class="form-control d-inline-block me-2" v-model.number="medicamento.quantidade" min="1" style="width: 80px;">
              <button type="button" class="btn btn-danger btn-sm" @click="removeMedicamento(index)">Remover</button>
            </div>
          </li>
        </ul>
      </div>

      <button type="submit" class="btn btn-primary">Adicionar ao Estoque</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      postoDistribuicaoSearch: '',
      postoDistribuicaoSearchResult: '',
      postoDistribuicaoInfo: null,
      medicamentoSearch: '',
      medicamentoSearchResult: '',
      form: {
        medicamentos: [],
        postoDistribuicao: ''
      }
    };
  },
  methods: {
    async searchPostoDistribuicao() {
      try {
        const response = await axios.get(`http://andromeda.lasdpc.icmc.usp.br:5025/api/postos-distribuicao/${this.postoDistribuicaoSearch}/`);
        this.postoDistribuicaoInfo = response.data;
        this.form.postoDistribuicao = response.data.cnes;
        this.postoDistribuicaoSearchResult = '';
      } catch (error) {
        this.postoDistribuicaoInfo = null;
        this.postoDistribuicaoSearchResult = 'Posto de distribuição não encontrado';
      }
    },
    async searchMedicamento() {
      try {
        const response = await axios.get(`http://andromeda.lasdpc.icmc.usp.br:5025/api/farmacos/${this.medicamentoSearch}`);
        this.addMedicamento(response.data);
        this.medicamentoSearchResult = '';
      } catch (error) {
        this.medicamentoSearchResult = 'Medicamento não encontrado';
      }
    },
    addMedicamento(medicamento) {
      const existingMed = this.form.medicamentos.find(m => m.codigo_barra === medicamento.codigo_barra);
      if (existingMed) {
        existingMed.quantidade += 1;
      } else {
        this.form.medicamentos.push({ ...medicamento, quantidade: 1 });
      }
    },
    removeMedicamento(index) {
      this.form.medicamentos.splice(index, 1);
    },
    async handleAddStock() {
      try {
        const estoqueData = this.form.medicamentos.map(med => ({
          medicamento: med.codigo_barra,
          quantidade: med.quantidade,
          posto_distribuicao: this.form.postoDistribuicao
        }));

        await axios.post('http://andromeda.lasdpc.icmc.usp.br:5025/api/estoque-local/batch/', estoqueData);

        // Limpar o formulário após o envio
        this.form = {
          medicamentos: [],
          postoDistribuicao: ''
        };
        this.postoDistribuicaoSearch = '';
        this.postoDistribuicaoSearchResult = '';
        this.postoDistribuicaoInfo = null;
        this.medicamentoSearch = '';
        this.medicamentoSearchResult = '';
        alert('Estoque adicionado com sucesso!');
      } catch (error) {
        console.error('Erro ao adicionar estoque:', error);
        alert('Erro ao adicionar estoque');
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>