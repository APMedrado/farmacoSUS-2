<template>
  <main>
    <div class="container mt-5">
      <h2>Cadastro de Novo Fármaco</h2>
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label for="codigoBarra" class="form-label">Código de Barra</label>
          <input type="text" class="form-control" id="codigoBarra" v-model="codigoBarra" required>
        </div>
        <div class="mb-3">
          <label for="nome" class="form-label">Nome</label>
          <input type="text" class="form-control" id="nome" v-model="nome" required>
        </div>
        <div class="mb-3">
          <label for="principioAtivo" class="form-label">Princípio Ativo</label>
          <input type="text" class="form-control" id="principioAtivo" v-model="principioAtivo" required>
        </div>
        <div class="mb-3">
          <label for="laboratorio" class="form-label">Laboratório</label>
          <input type="text" class="form-control" id="laboratorio" v-model="laboratorio" required>
        </div>
        <div class="mb-3">
          <label for="indicacao" class="form-label">Indicação</label>
          <input type="text" class="form-control" id="indicacao" v-model="indicacao" required>
        </div>
        <div class="mb-3">
          <label for="tipoReceita" class="form-label">Tipo de Receita</label>
          <input type="text" class="form-control" id="tipoReceita" v-model="tipoReceita" required>
        </div>
        <button type="submit" class="btn btn-primary">Salvar</button>
      </form>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      codigoBarra: '',
      nome: '',
      principioAtivo: '',
      laboratorio: '',
      indicacao: '',
      tipoReceita: ''
    };
  },
  methods: {
    async submitForm() {
      const novoFarmaco = {
        codigo_barra: this.codigoBarra,
        produto: this.nome,
        principio_ativo: this.principioAtivo,
        laboratorio: this.laboratorio,
        indicacao: this.indicacao,
        tipo_receita: this.tipoReceita
      };

      try {
        const response = await axios.post('http://andromeda.lasdpc.icmc.usp.br:5025/api/farmacos/', novoFarmaco);
        console.log(response.data);
        alert('Fármaco adicionado com sucesso!');
      } catch (error) {
        console.error(error);
        alert('Erro ao adicionar fármaco.');
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