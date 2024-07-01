<template>
    <div class="table-responsive">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">CRM</th>
            <th scope="col">Nome</th>
            <th scope="col">Especialidade</th>
            <th scope="col">Situação</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="medico in medicos" :key="medico.crm">
            <td>{{ medico.crm }}</td>
            <td>{{ medico.nome }}</td>
            <td>{{ medico.especialidade }}</td>
            <td>{{ medico.situacao }}</td>
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
        medicos: []
      };
    },
    mounted() {
      this.fetchMedicos();
    },
    methods: {
      fetchMedicos() {
        axios.get('http://andromeda.lasdpc.icmc.usp.br:5025/api/medicos/')
          .then(response => {
            this.medicos = response.data;
          })
          .catch(error => {
            console.error('Erro ao buscar médicos: ', error);
          });
      }
    }
  };
  </script>  