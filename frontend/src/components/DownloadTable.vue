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
    name: "DownloadTable",
    props: ['tableData'],
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
    
    // let date = new Date(year,month,day)
    const date1 = new Date();
    const day = date1.getDate().toString().padStart(2, '0'); // เติมเลข 0 ข้างหน้า (ถ้าวันน้อยกว่า 10)
    const month = (date1.getMonth() + 1).toString().padStart(2, '0'); // เติมเลข 0 และเดือนเริ่มจาก 0
    const year = date1.getFullYear().toString();

    // รวมค่าที่ต้องการในรูปแบบ 'DD-MM-YYYY'
    const excelName = `${day}-${month}-${year}`;

    let name_excel = excelName + ".xlsx"
    link.setAttribute('download', name_excel);
    

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
  