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
          Nome: {{ medicamentoInfo.nome }}<br>
          Código de Barras: {{ medicamentoInfo.codigoBarras }}
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
export default {
  data() {
    return {
      medicamentoSearch: '',
      medicamentoSearchResult: '',
      medicamentoInfo: null,
      quantidade: 1,
      medicamentosDisponiveis: [
        { codigoBarras: '1234567890123', nome: 'Paracetamol' },
        { codigoBarras: '2345678901234', nome: 'Ibuprofeno' },
        { codigoBarras: '3456789012345', nome: 'Dipirona' }
      ]
    };
  },
  methods: {
    searchMedicamento() {
      const found = this.medicamentosDisponiveis.find(medicamento => medicamento.codigoBarras === this.medicamentoSearch);
      if (found) {
        this.medicamentoInfo = found;
        this.medicamentoSearchResult = '';
      } else {
        this.medicamentoInfo = null;
        this.medicamentoSearchResult = 'Medicamento não encontrado';
      }
    },
    handleAddToRegionalStock() {
      // Cria um objeto FormData para enviar os dados
      const formData = new FormData();
      formData.append('codigoBarras', this.medicamentoInfo.codigoBarras);
      formData.append('quantidade', this.quantidade);

      // Aqui você pode adicionar a lógica para enviar o FormData para um servidor via AJAX.
      console.log('Form data:', formData);

      // Limpar o formulário após o envio
      this.medicamentoSearch = '';
      this.medicamentoSearchResult = '';
      this.medicamentoInfo = null;
      this.quantidade = 1;
      alert('Estoque regional atualizado com sucesso!');
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
