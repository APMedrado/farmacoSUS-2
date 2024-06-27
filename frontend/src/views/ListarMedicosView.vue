<template>
    <main>
      <div class="container">
        <div class="d-flex justify-content-between align-items-center flex-wrap my-3">
          <h2 class="mb-0">Médicos Registrados no Sistema</h2>
          <button class="btn btn-primary">
            <router-link class="dropdown-item" to="/medicos/novo">Novo Médico</router-link>
          </button>
        </div>
        <p>Aqui você pode conferir e editar os médicos cadastrados no sistema, ou deletar um médico.</p>
        <DoctorsTable />
      </div>
    </main>
  </template>
  
  <script>
  import DoctorsTable from '../components/DoctorsTable.vue';
  
  export default {
    components: {
      DoctorsTable
    }
  };
  </script>  