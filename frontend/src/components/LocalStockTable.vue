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
          <th scope="col">Posto de Distribuição</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in farmacos" :key="item.id">
          <td>{{ item.medicamento.codigo_barra }}</td>
          <td>{{ item.medicamento.produto }}</td>
          <td>{{ item.medicamento.principio_ativo }}</td>
          <td>{{ item.medicamento.laboratorio }}</td>
          <td>{{ item.quantidade }}</td>
          <td>{{ item.posto_distribuicao.nome }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['postoId'],
  data() {
    return {
      farmacos: []
    };
  },
  watch: {
    postoId(newVal) {
      this.fetchFarmacos(newVal);
    }
  },
  mounted() {
    this.fetchFarmacos(this.postoId);
  },
  methods: {
    fetchFarmacos(postoId) {
      const url = !postoId ? 'http://localhost:8000/api/estoque-local/' : `http://localhost:8000/api/estoque-local/?posto_distribuicao=${postoId}`;
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