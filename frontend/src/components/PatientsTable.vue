<template>
    <div class="table-responsive">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">CPF</th>
            <th scope="col">Nome</th>
            <th scope="col">Data de Nascimento</th>
            <th scope="col">Bolsa Família</th>
            <th scope="col">Cadastro Único</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="paciente in pacientes" :key="paciente.cpf">
            <td>{{ paciente.cpf }}</td>
            <td>{{ paciente.nome }}</td>
            <td>{{ paciente.data_nascimento }}</td>
            <td>{{ paciente.bolsa_familia }}</td>
            <td>{{ paciente.cadastro_unico }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        pacientes: []
      };
    },
    mounted() {
      this.fetchPacientes();
    },
    methods: {
      fetchPacientes() {
        axios.get('http://andromeda.lasdpc.icmc.usp.br:5025/api/pacientes/')
          .then(response => {
            this.pacientes = response.data;
          })
          .catch(error => {
            console.error('Erro ao buscar pacientes: ', error);
          });
      }
    }
  };
  </script>  