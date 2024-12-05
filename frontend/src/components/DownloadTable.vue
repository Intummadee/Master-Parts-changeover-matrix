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

    // async downloadExcel() {
    //   try {
    //     const response = await axios.get('http://localhost:8000/table', {
    //       responseType: 'blob', // ระบุว่าเป็นการดาวน์โหลดไฟล์
    //       // ตั้งค่า responseType: 'blob' เพื่อรองรับไฟล์ binary
    //     });

    //     const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
    //     const url = window.URL.createObjectURL(blob);
    //     // สร้าง URL ชั่วคราว (window.URL.createObjectURL) สำหรับไฟล์ที่ดึงมา
    //     const link = document.createElement('a');
    //     link.href = url;
    //     link.target="_self"
    //     // สร้างลิงก์ <a> ชั่วคราวเพื่อใช้ดาวน์โหลดไฟล์
        
    //     // let date = new Date(year,month,day)
    //     const date1 = new Date();
    //     const day = date1.getDate().toString().padStart(2, '0'); // เติมเลข 0 ข้างหน้า (ถ้าวันน้อยกว่า 10)
    //     const month = (date1.getMonth() + 1).toString().padStart(2, '0'); // เติมเลข 0 และเดือนเริ่มจาก 0
    //     const year = date1.getFullYear().toString();

    //     // รวมค่าที่ต้องการในรูปแบบ 'DD-MM-YYYY'
    //     const excelName = `${day}-${month}-${year}`;

    //     let name_excel = excelName + ".xlsx"
    //     link.setAttribute('download', name_excel);
        

    //     document.body.appendChild(link); // ใส่ลิงก์ลงใน DOM ชั่วคราว
    //     link.click(); // คลิกเพื่อดาวน์โหลด
    //     document.body.removeChild(link); // ลบลิงก์ออกจาก DOM
    //     window.URL.revokeObjectURL(url); // ลบ URL blob หลังใช้งาน
    //   } 
    //   catch (error) {
    //     console.error('Error downloading Excel file:', error);
    //   }
    // }

    async downloadExcel() {
      try {
        const response = await axios.get('http://localhost:8000/table');

        // แยกข้อมูลออกจาก response
        const { file, column_colors } = response.data;

        // ถอดรหัส base64 และแปลงเป็น Blob
        const binaryData = atob(file);
        const byteArray = new Uint8Array(binaryData.length);
        for (let i = 0; i < binaryData.length; i++) {
          byteArray[i] = binaryData.charCodeAt(i);
        }
        const blob = new Blob([byteArray], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
        const url = window.URL.createObjectURL(blob);

        // สร้างลิงก์ดาวน์โหลด
        const link = document.createElement('a');
        link.href = url;
        const date1 = new Date();
        const day = date1.getDate().toString().padStart(2, '0');
        const month = (date1.getMonth() + 1).toString().padStart(2, '0');
        const year = date1.getFullYear().toString();
        const excelName = `${day}-${month}-${year}`;
        link.setAttribute('download', `${excelName}.xlsx`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);

        // ใช้ column_colors
        console.log('Column Colors:', column_colors);
      } catch (error) {
        console.error('Error downloading Excel file:', error);
      }
    }


}
  };
  </script>
  
  <style scoped>
  </style>
  