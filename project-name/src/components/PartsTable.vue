<template>
    <v-data-table :headers="headers" :items="parts" class="elevation-1">
      <template v-slot:top>
        <v-btn @click="fetchParts">Load Parts</v-btn>
        <v-btn @click="exportParts">Export to Excel</v-btn>
        <v-file-input @change="importParts" label="Import Excel" accept=".xlsx"></v-file-input>
      </template>
    </v-data-table>
  </template>
  
  <script>
  import axios from "axios";
  
  
  export default {
    data() {
      return {
        headers: [
          { text: "Part Name", value: "name" },
          { text: "Changeover Time (min)", value: "changeover_time" },
        ],
        parts: [],
      };
    },
    methods: {
      async fetchParts() {
        const response = await axios.get("http://localhost:8000/parts");
        this.parts = response.data;
      },
      async exportParts() {
        await axios.post("http://localhost:8000/export");
        alert("Exported to parts.xlsx");
      },
      async importParts(event) {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append("file", file);
        await axios.post("http://localhost:8000/import", formData);
        this.fetchParts();
      },
    },
  };
  </script>
  
  <style scoped>
  .v-data-table {
    margin-top: 20px;
  }
  </style>
  