<template>
  <div class="table-responsive">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Data de Entrega</th>
          <th scope="col">Paciente</th>
          <th scope="col">Médico</th>
          <th scope="col">Medicamentos</th>
          <th scope="col">Posto de Distribuição</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="registro in registros" :key="registro.id">
          <td>{{ registro.data_entrega }}</td>
          <td>{{ registro.beneficiario.nome }}</td>
          <td>{{ registro.receita_medico.nome }}</td>
          <td>
            <ul>
              <li v-for="medicamento in registro.medicamentos" :key="medicamento.medicamento.codigo_barra">
                {{ medicamento.medicamento.produto }} ({{ medicamento.quantidade }})
              </li>
            </ul>
          </td>
          <td>{{ registro.posto_distribuicao.nome }}</td>
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
      registros: []
    };
  },
  mounted() {
    this.fetchRegistros();
  },
  methods: {
    fetchRegistros() {
      axios.get('http://localhost:8000/api/registro-entrega/')
        .then(response => {
          this.registros = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar registros de entrega: ', error);
        });
    }
  }
};
</script>