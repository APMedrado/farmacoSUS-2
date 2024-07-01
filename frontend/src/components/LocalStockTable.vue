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
          <th scope="col">Quantidade a Receber</th>
          <th scope="col">Posto de Distribuição</th>
          <th scope="col">Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in farmacos" :key="item.id">
          <td>{{ item.medicamento.codigo_barra }}</td>
          <td>{{ item.medicamento.produto }}</td>
          <td>{{ item.medicamento.principio_ativo }}</td>
          <td>{{ item.medicamento.laboratorio }}</td>
          <td>{{ item.quantidade }}</td>
          <td>{{ item.quantidade_a_receber }}</td>
          <td>{{ item.posto_distribuicao.nome }}</td>
          <td>
            <button class="btn btn-success" @click="confirmar Abastecimento(item)">Abastecimento Feito</button>
          </td>
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
      const url = !postoId ? 'http://andromeda.lasdpc.icmc.usp.br:5025/api/estoque-local/' : `http://andromeda.lasdpc.icmc.usp.br:5025/api/estoque-local/?posto_distribuicao=${postoId}`;
      axios.get(url)
        .then(response => {
          this.farmacos = response.data;
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    confirmarAbastecimento(item) {
      const data = {
        medicamento_codigo: item.medicamento.codigo_barra,
        posto_cnes: item.posto_distribuicao.cnes
      };
      axios.post('http://andromeda.lasdpc.icmc.usp.br:5025/api/estoque-local/confirmar-abastecimento/', data)
        .then(response => {
          alert('Abastecimento confirmado com sucesso!');
          this.fetchFarmacos(this.postoId);
        })
        .catch(error => {
          console.error('Erro ao confirmar abastecimento:', error);
          alert('Erro ao confirmar abastecimento');
        });
    }
  }
};
</script>