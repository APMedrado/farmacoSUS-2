<template>
    <main>
      <div class="container mt-5">
        <h2>Cadastro de Novo Médico</h2>
        <form @submit.prevent="submitForm">
          <div class="mb-3">
            <label for="crm" class="form-label">CRM</label>
            <input type="text" class="form-control" id="crm" v-model="crm" required>
          </div>
          <div class="mb-3">
            <label for="nome" class="form-label">Nome</label>
            <input type="text" class="form-control" id="nome" v-model="nome" required>
          </div>
          <div class="mb-3">
            <label for="especialidade" class="form-label">Especialidade</label>
            <input type="text" class="form-control" id="especialidade" v-model="especialidade" required>
          </div>
          <div class="mb-3">
            <label for="situacao" class="form-label">Situação</label>
            <input type="text" class="form-control" id="situacao" v-model="situacao" required>
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
        crm: '',
        nome: '',
        especialidade: '',
        situacao: ''
      };
    },
    methods: {
      async submitForm() {
        const novoMedico = {
          crm: this.crm,
          nome: this.nome,
          especialidade: this.especialidade,
          situacao: this.situacao
        };
  
        try {
          const response = await axios.post('http://localhost:8000/api/medicos/', novoMedico);
          console.log(response.data);
          alert('Médico adicionado com sucesso!');
        } catch (error) {
          console.error(error);
          alert('Erro ao adicionar médico.');
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