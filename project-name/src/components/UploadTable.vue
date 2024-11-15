<template>
  <v-container style="background-color: burlywood;">
    <v-file-input
      label="อัปโหลดไฟล์ Excel"
      v-model="file"
      accept=".xlsx, .xls"
      prepend-icon="mdi-upload"
      @change="uploadFile"
    ></v-file-input>
    <v-btn color="primary" @click="uploadFile">อัปโหลดไฟล์</v-btn>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
    };
  },
  methods: {
    async uploadFile() {
      if (!this.file) {
        alert("กรุณาเลือกไฟล์ก่อน");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      console.log("FormData:", formData.get("file"));

      try {
        const response = await axios.post("http://localhost:8000/upload-excel", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        alert("อัปโหลดสำเร็จ");
        console.log("Response:", response.data);
        location.reload();
      } catch (error) {
        console.error("Error uploading file:", error);
        alert("เกิดข้อผิดพลาดในการอัปโหลดไฟล์");
      }
    },
  },
};
</script>

<style scoped>
.v-file-input {
  margin-bottom: 20px;
}
</style>
