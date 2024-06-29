<template>
  <div class="container mt-5">
    <h2>Registrar Nova Entrega</h2>
    <form @submit.prevent="handleSubmit">
      <!-- Posto de Distribuição com Pesquisa de CNES -->
      <div class="mb-3 position-relative">
        <label for="postoDistribuicao" class="form-label">Posto de Distribuição (CNES)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="postoDistribuicao" v-model="postoDistribuicaoSearch" placeholder="Digite o CNES">
          <button type="button" class="btn btn-primary" @click="searchPostoDistribuicao">Pesquisar</button>
        </div>
        <p v-if="postoDistribuicaoSearchResult" class="mt-2">{{ postoDistribuicaoSearchResult }}</p>
        <div v-if="form.postoDistribuicao" class="mt-2">
          <strong>Posto Selecionado:</strong><br>
          CNES: {{ form.postoDistribuicao.cnes }}<br>
          Nome: {{ form.postoDistribuicao.nome }}<br>
          Endereço: {{ form.postoDistribuicao.endereco }}<br>
          Bairro: {{ form.postoDistribuicao.bairro }}<br>
          Município: {{ form.postoDistribuicao.municipio }}
        </div>
      </div>

      <!-- Beneficiário com Pesquisa de CPF -->
      <div class="mb-3 position-relative">
        <label for="beneficiario" class="form-label">Beneficiário (CPF)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="beneficiario" v-model="beneficiarioSearch" @input="formatCpf" placeholder="Digite o CPF">
          <button type="button" class="btn btn-primary" @click="searchBeneficiario">Pesquisar</button>
        </div>
        <p v-if="beneficiarioSearchResult" class="mt-2">{{ beneficiarioSearchResult }}</p>
        <p v-if="beneficiarioInfo" class="mt-2">
          Nome: {{ beneficiarioInfo.nome }}<br>
          Data de Nascimento: {{ beneficiarioInfo.data_nascimento }}<br>
          Bolsa Família: {{ beneficiarioInfo.bolsa_familia || 'N/A' }}<br>
          Cadastro Único: {{ beneficiarioInfo.cadastro_unico || 'N/A' }}
        </p>
      </div>

      <!-- Médico com Pesquisa de CRM -->
      <div class="mb-3 position-relative">
        <label for="medico" class="form-label">Médico (CRM)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="medico" v-model="medicoSearch" placeholder="Digite o CRM">
          <button type="button" class="btn btn-primary" @click="searchMedico">Pesquisar</button>
        </div>
        <p v-if="medicoSearchResult" class="mt-2">{{ medicoSearchResult }}</p>
        <p v-if="medicoInfo" class="mt-2">
          Nome: {{ medicoInfo.nome }}<br>
          Especialidade: {{ medicoInfo.especialidade }}<br>
          Situação: {{ medicoInfo.situacao }}
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

      <!-- Lista de Medicamentos Selecionados -->
      <div class="mb-3" v-if="form.medicamentos.length">
        <label class="form-label">Medicamentos Selecionados</label>
        <ul class="list-group">
          <li v-for="(medicamento, index) in form.medicamentos" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
            {{ medicamento.nome }} ({{ medicamento.codigo_barra }}) - {{ medicamento.quantidade }} un
            <div>
              <input type="number" class="form-control d-inline-block me-2" v-model.number="medicamento.quantidade" :min="1" :max="medicamento.maxQuantidade" style="width: 80px;">
              <button type="button" class="btn btn-danger btn-sm" @click="removeMedicamento(index)">Remover</button>
            </div>
          </li>
        </ul>
      </div>

      <!-- Data da Receita -->
      <div class="mb-3">
        <label for="dataReceita" class="form-label">Data da Receita</label>
        <input type="date" class="form-control" id="dataReceita" v-model="form.dataReceita">
      </div>

      <!-- Data da Entrega -->
      <div class="mb-3">
        <label for="dataEntrega" class="form-label">Data da Entrega</label>
        <input type="date" class="form-control" id="dataEntrega" v-model="form.dataEntrega">
      </div>

      <button type="submit" class="btn btn-primary">Registrar Entrega</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      beneficiarioSearch: '',
      beneficiarioSearchResult: '',
      beneficiarioInfo: null,
      postoDistribuicaoSearch: '',
      postoDistribuicaoSearchResult: '',
      medicoSearch: '',
      medicoSearchResult: '',
      medicoInfo: null,
      medicamentoSearch: '',
      medicamentoSearchResult: '',
      form: {
        medicamentos: [],
        beneficiario: '',
        medico: '',
        dataReceita: '',
        postoDistribuicao: null,
        dataEntrega: this.getCurrentDate() // Pré-preencher com a data atual
      }
    };
  },
  methods: {
    getCurrentDate() {
      const today = new Date();
      const day = String(today.getDate()).padStart(2, '0');
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const year = today.getFullYear();
      return `${year}-${month}-${day}`;
    },
    formatCpf() {
      let cpf = this.beneficiarioSearch.replace(/\D/g, '');
      cpf = cpf.slice(0, 11);
      const formattedCpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
      this.beneficiarioSearch = formattedCpf;
    },
    searchBeneficiario() {
      const cpfUnformatted = this.beneficiarioSearch.replace(/\D/g, '');
      axios.get(`http://localhost:8000/api/pacientes/${cpfUnformatted}/`)
        .then(response => {
          this.beneficiarioInfo = response.data;
          this.form.beneficiario = cpfUnformatted;
          this.beneficiarioSearchResult = '';
        })
        .catch(error => {
          console.error('Erro ao buscar beneficiário: ', error);
          this.beneficiarioInfo = null;
          this.beneficiarioSearchResult = 'Beneficiário não encontrado';
        });
    },
    searchPostoDistribuicao() {
      axios.get(`http://localhost:8000/api/postos-distribuicao/${this.postoDistribuicaoSearch}/`)
        .then(response => {
          this.form.postoDistribuicao = response.data;
          this.postoDistribuicaoSearchResult = '';
          this.form.medicamentos = []; // Resetar lista de medicamentos ao selecionar novo posto
        })
        .catch(error => {
          console.error('Erro ao buscar posto de distribuição: ', error);
          this.form.postoDistribuicao = null;
          this.postoDistribuicaoSearchResult = 'Posto de distribuição não encontrado';
        });
    },
    searchMedico() {
      axios.get(`http://localhost:8000/api/medicos/${this.medicoSearch}/`)
        .then(response => {
          this.medicoInfo = response.data;
          this.form.medico = this.medicoSearch;
          this.medicoSearchResult = '';
        })
        .catch(error => {
          console.error('Erro ao buscar médico: ', error);
          this.medicoInfo = null;
          this.medicoSearchResult = 'Médico não encontrado';
        });
    },
    searchMedicamento() {
      if (!this.form.postoDistribuicao || !this.form.postoDistribuicao.cnes) {
        this.medicamentoSearchResult = 'Por favor, selecione um posto de distribuição válido primeiro';
        return;
      }
      const cnes = this.form.postoDistribuicao.cnes;
      axios.get(`http://localhost:8000/api/estoque-local/?posto_distribuicao=${cnes}&medicamento=${this.medicamentoSearch}`)
        .then(response => {
          const medicamentoEncontrado = response.data.find(item => item.medicamento.codigo_barra === this.medicamentoSearch);
          if (medicamentoEncontrado) {
            medicamentoEncontrado.maxQuantidade = medicamentoEncontrado.quantidade;
            this.addMedicamento(medicamentoEncontrado.medicamento, medicamentoEncontrado.maxQuantidade);
            this.medicamentoSearchResult = '';
          } else {
            this.medicamentoSearchResult = 'Medicamento não encontrado ou fora de estoque';
          }
        })
        .catch(error => {
          console.error('Erro ao buscar medicamento: ', error);
          this.medicamentoSearchResult = 'Erro ao buscar medicamento';
        });
    },
    addMedicamento(medicamento, maxQuantidade) {
      if (medicamento && !this.form.medicamentos.some(m => m.codigo_barra === medicamento.codigo_barra)) {
        this.form.medicamentos.push({
          codigo_barra: medicamento.codigo_barra,
          nome: medicamento.produto,
          quantidade: 1,
          maxQuantidade: maxQuantidade // Armazenar a quantidade máxima disponível
        });
        this.medicamentoSearch = '';
      }
    },
    removeMedicamento(index) {
      this.form.medicamentos.splice(index, 1);
    },
    handleSubmit() {
      const entregaData = {
        beneficiario: this.form.beneficiario,
        receita_medico: this.form.medico,
        receita_data: this.form.dataReceita,
        posto_distribuicao: this.form.postoDistribuicao.cnes,
        data_entrega: this.form.dataEntrega,
        medicamentos: this.form.medicamentos.map(m => ({
          codigo_barra: m.codigo_barra,
          quantidade: m.quantidade
        }))
      };

      axios.post('http://localhost:8000/api/registros-entregas/', entregaData)
        .then(response => {
          alert('Entrega registrada com sucesso!');
          this.resetForm();
        })
        .catch(error => {
          console.error('Erro ao registrar entrega: ', error);
          alert('Erro ao registrar entrega');
        });
    },
    resetForm() {
      this.form = {
        medicamentos: [],
        beneficiario: '',
        medico: '',
        dataReceita: '',
        postoDistribuicao: null,
        dataEntrega: this.getCurrentDate()
      };
      this.beneficiarioSearch = '';
      this.beneficiarioSearchResult = '';
      this.beneficiarioInfo = null;
      this.postoDistribuicaoSearch = '';
      this.postoDistribuicaoSearchResult = '';
      this.medicoSearch = '';
      this.medicoSearchResult = '';
      this.medicoInfo = null;
      this.medicamentoSearch = '';
      this.medicamentoSearchResult = '';
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>