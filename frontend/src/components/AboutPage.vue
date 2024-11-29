<template>
    <v-app>

    <Navbar/>



    <Footer/>


    </v-app>
  </template>
  
  <script>


import Navbar from './FixComponent/NavbarPage.vue'
import Footer from './FixComponent/FooterPage.vue'

  export default {
    components: {
      Navbar,
      Footer
    },
    name: "AboutPage",
    

  };
  </script>
  