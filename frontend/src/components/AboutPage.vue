<template>
    <v-app>

    <Navbar/>

    
      <DashBoardViews />
      <Projects />
      <Team />

    <Footer/>


    </v-app>
  </template>
  
  <script>


import Navbar from './FixComponent/NavbarPage.vue'
import Footer from './FixComponent/FooterPage.vue'
import DashBoardViews from './FixComponent/views/DashBoardViews.vue'
import Projects from './FixComponent/views/ProjectsPage.vue'
import Team from './FixComponent/views/TeamPage.vue'
  export default {
    components: {
      Navbar,
      Footer,
      DashBoardViews,
      Projects,
      Team
    },
    name: "AboutPage",
    

  };
  </script>
  