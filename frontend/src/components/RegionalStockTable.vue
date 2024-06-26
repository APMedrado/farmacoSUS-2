<template>
  <div class="table-responsive">
      <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Código de Barra</th>
              <th scope="col">Nome</th>
              <th scope="col">Princípio Ativo</th>
              <th scope="col">Laboratório</th>
              <th scope="col">Quantidade</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="farmaco in farmacos" :key="farmaco.id">
              <td>{{ farmaco.medicamento.codigo_barra }}</td>
              <td>{{ farmaco.medicamento.produto }}</td>
              <td>{{ farmaco.medicamento.principio_ativo }}</td>
              <td>{{ farmaco.medicamento.laboratorio }}</td>
              <td>{{ farmaco.quantidade }}</td>
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
      farmacos: []
    };
  },
  mounted() {
    this.fetchFarmacos();
  },
  methods: {
    fetchFarmacos() {
      const url = 'http://localhost:8000/api/estoque-regional/';
      axios.get(url)
        .then(response => {
          this.farmacos = response.data;
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    }
  }
};
</script>
