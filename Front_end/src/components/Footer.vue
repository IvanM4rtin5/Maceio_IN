<template>
    <footer class="footer-section">
      <div class="social-media-section">
        <div class="social-icons">
          <a href="https://facebook.com" target="_blank" class="social-icon">
            <i class="pi pi-facebook"></i>
          </a>
          <a href="https://instagram.com" target="_blank" class="social-icon">
            <i class="pi pi-instagram"></i>
          </a>
          <a href="https://youtube.com" target="_blank" class="social-icon">
            <i class="pi pi-youtube"></i>
          </a>
          <a href="https://twitter.com" target="_blank" class="social-icon">
            <i class="pi pi-twitter" ></i>
          </a>
          <a href="https://spotify.com" target="_blank" class="social-icon">
            <i class="pi pi-spotify"></i>
          </a>
        </div>
        <p>Rua Pedro Monteiro, nº 47, Centro - Maceió/AL CEP: 57020-380</p>
        <a href="mailto:atendimento@semec.maceio.al.gov.br" target="_blank">atendimento@semec.maceio.al.gov.br</a>
      </div>
    </footer>
  </template>
  
  <script setup>
 
  </script>
  
  <style scoped>
  .footer-section {
    background-image: url('../assets/maceio_topo.svg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    text-align: center;
    /* margin-top: 2rem; */
    padding: 1rem;
    background-color: #f9f9f9;
    border-top: 1px solid #ddd;
  }
  
  .social-media-section {
    margin: 0 auto;
    max-width: 600px;
  }
  
  .social-icons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 1rem;
  }
    
  .social-icon:hover {
    color: #0056b3;
  }
    
    i{
       margin-right: 0.5rem;
       margin-top: 20px;
       margin-bottom: 30px;
       background-color:transparent;
       color: #007bff  ;
       border-radius: 100%; 
       font-size:30px;
       transition: color 0.3s ease;
     }
  i:hover {
    cursor: pointer;
    color: #0056b3;
  }
  </style>