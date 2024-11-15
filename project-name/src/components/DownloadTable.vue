<template>
    <v-container>
      <v-btn @click="downloadExcel" color="primary" dark>
        Download Parts Table (Excel)
      </v-btn>

    

    </v-container>
  </template>
  
  <script>
  import axios from 'axios'



  export default {
    props: ['tableData'],
    name: "DownloadTable",
    methods: {
        downloadTable(){
            console.log("Hi");
            
        },
      
    
    async fetchParts() {
        try {
        const response = await axios.get("http://localhost:8000/table");
        this.parts = response.data;
        } catch (error) {
            console.error("Error fetching parts or changeover data:", error);
        }

    },

    async downloadExcel() {
  try {
    const response = await axios.get('http://localhost:8000/table', {
      responseType: 'blob',
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'parts_table.xlsx');
    document.body.appendChild(link);
    link.click();
    link.remove();
  } catch (error) {
    console.error('Error downloading Excel file:', error);
  }
}


}
  };
  </script>
  
  <style scoped>
  </style>
  