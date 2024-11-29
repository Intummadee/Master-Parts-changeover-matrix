<template>
  <v-app-bar
    color="cyan darken-1"
    >
    <!-- style="background-image: url('https://picsum.photos/1920/1080?random'); background-size: cover; background-position: center;"
    elevation="0" -->
  
    <template v-slot:image>
      <v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
    </template>

    <template v-slot:prepend>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </template>

    <v-app-bar-title>โรงงานผลิตชิ้นส่วนรถยนต์</v-app-bar-title>

    <v-spacer></v-spacer>

    <v-btn icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>
    
    <v-btn @click="toggleTheme">
        <v-icon>{{ $vuetify.theme.dark ? 'mdi-brightness-7' : 'mdi-moon-waning-crescent' }}</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-heart</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark; // สลับค่า dark/light
      localStorage.setItem("theme", this.$vuetify.theme.dark ? "dark" : "light");
    },
  },
  mounted() {
    const savedTheme = localStorage.getItem("theme");
    this.$vuetify.theme.dark = savedTheme === "dark";
  },
}
</script>

<style>

</style>