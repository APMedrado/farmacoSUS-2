<template>
  <div class="table-responsive">
      <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Código de Barra</th>
              <th scope="col">Nome</th>
              <th scope="col">Princípio Ativo</th>
              <th scope="col">Laboratório</th>
              <th scope="col">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="farmaco in farmacos" :key="farmaco.codigo_barra">
              <td>{{ farmaco.codigo_barra }}</td>
              <td>{{ farmaco.produto }}</td>
              <td>{{ farmaco.principio_ativo }}</td>
              <td>{{ farmaco.laboratorio }}</td>
              <td>
                <button class="btn btn-primary" @click="editFarmaco(farmaco)">Editar</button>
                <button class="btn btn-danger" @click="deleteFarmaco(farmaco.codigo_barra)">Deletar</button>
              </td>
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
      axios.get('http://localhost:8000/api/farmacos/')
        .then(response => {
          this.farmacos = response.data;
          console.log(this.farmacos[0]);
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    editFarmaco(farmaco) {
      // Lógica de redirecionamento ou exibição de modal para edição
    },
    deleteFarmaco(codigoBarra) {
      axios.delete(`http://localhost:8000/api/farmacos/${codigoBarra}`)
        .then(() => {
          this.farmacos = this.farmacos.filter(f => f.codigo_barra !== codigoBarra);
          alert('Fármaco deletado com sucesso!');
        })
        .catch(error => {
          alert('Erro ao deletar fármaco: ' + error.message);
        });
    }
  }
};
</script>