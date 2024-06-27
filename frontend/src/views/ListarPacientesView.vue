<template>
  <main>
    <div class="container">
      <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
        <h2 class="mb-0">Pacientes Registrados no Sistema</h2>
        <button class="btn btn-primary">
          <router-link class="dropdown-item" to="/pacientes/novo">Novo Paciente</router-link>
        </button>
      </div>
      <p>Aqui você pode conferir e editar os pacientes cadastrados no sistema, ou deletar um paciente.</p>
      <PatientsTable />
    </div>
  </main>
</template>

<script>
import PatientsTable from '../components/PatientsTable.vue';

export default {
  components: {
    PatientsTable
  }
};
</script>