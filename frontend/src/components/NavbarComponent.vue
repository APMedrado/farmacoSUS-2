<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light mx-0 mt-0 px-3">
    <div class="container-fluid">
      <RouterLink class="navbar-brand d-flex align-items-center me-auto" to="/">
        <img src="/Pill.png" alt="Pill Icon" style="height: 30px; margin-right: 10px;">
        <span class="d-none d-md-block">Gestão de Remédios Gratuitos Disponíveis pelo SUS</span>
      </RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <button class="btn btn-primary me-md-3">
              <RouterLink class="dropdown-item" to="/entrega">Registrar Nova Entrega</RouterLink>
            </button>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Estoque
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
              <li><RouterLink class="dropdown-item" to="/local">Estoque Local</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="/regional">Estoque Regional</RouterLink></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Fármacos
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
              <li><RouterLink class="dropdown-item" to="/farmacos">Listar</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="/farmacos/novo">Novo</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="/farmacos/batch">Batch Input</RouterLink></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Histórico
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
              <li><RouterLink class="dropdown-item" to="#">Registros de Entrega</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="#">Pacientes Registrados</RouterLink></li>
              <li><RouterLink class="dropdown-item" to="#">Médicos Registrados</RouterLink></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
