<template>
  <div class="container mt-5">
    <h2>Adicionar ao Estoque Regional</h2>
    <form @submit.prevent="handleAddToRegionalStock">
      <!-- Medicamento com Pesquisa de Código de Barras -->
      <div class="mb-3 position-relative">
        <label for="medicamento" class="form-label">Medicamento (Código de Barras)</label>
        <div class="input-group">
          <input type="text" class="form-control" id="medicamento" v-model="medicamentoSearch" placeholder="Digite o Código de Barras">
          <button type="button" class="btn btn-primary" @click="searchMedicamento">Pesquisar</button>
        </div>
        <p v-if="medicamentoSearchResult" class="mt-2">{{ medicamentoSearchResult }}</p>
        <p v-if="medicamentoInfo" class="mt-2">
          Nome: {{ medicamentoInfo.produto }}<br>
          Código de Barras: {{ medicamentoInfo.codigo_barra }}
        </p>
      </div>

      <!-- Quantidade a Adicionar -->
      <div class="mb-3" v-if="medicamentoInfo">
        <label for="quantidade" class="form-label">Quantidade</label>
        <input type="number" class="form-control" id="quantidade" v-model.number="quantidade" min="1">
      </div>

      <button type="submit" class="btn btn-primary" :disabled="!medicamentoInfo">Adicionar ao Estoque</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      medicamentoSearch: '',
      medicamentoSearchResult: '',
      medicamentoInfo: null,
      quantidade: 1
    };
  },
  methods: {
    searchMedicamento() {
      axios.get(`http://localhost:8000/api/farmacos/${this.medicamentoSearch}/`)
        .then(response => {
          this.medicamentoInfo = response.data;
          this.medicamentoSearchResult = '';
        })
        .catch(error => {
          console.error('Erro ao buscar medicamento: ', error);
          this.medicamentoInfo = null;
          this.medicamentoSearchResult = 'Medicamento não encontrado';
        });
    },
    handleAddToRegionalStock() {
      const payload = {
        medicamento: this.medicamentoInfo.codigo_barra,
        quantidade: this.quantidade
      };

      axios.post('http://localhost:8000/api/estoque-regional/batch/', [payload])
        .then(response => {
          alert('Estoque regional atualizado com sucesso!');
          this.medicamentoSearch = '';
          this.medicamentoSearchResult = '';
          this.medicamentoInfo = null;
          this.quantidade = 1;
        })
        .catch(error => {
          console.error('Erro ao adicionar ao estoque regional: ', error);
          alert('Erro ao adicionar ao estoque regional.');
        });
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>