<template>
    <v-app>
  
      
  
      <v-container style="margin-top:2rem">
        <v-data-table 
          :headers="headers"
          :items="tableData"
          :item-key="'id'"
          class="grey-table"
          dense
        >
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.part_name }}</td>
              <td v-for="(header, headerIndex) in headers.slice(1)" 
                  :key="headerIndex"
                  :class="{ 
                    'grey-background': item.part_name === header.text
                  }">
                {{ item.changeoverTimes[header.text] || '' }}
              </td>
            </tr>
          </template>
        </v-data-table>
  
      </v-container>
      
      
  
      <!-- Excel Download -->
      <DownloadTable :tableData="tableData" />
  
      <!-- Upload -->
      <UploadTable />
      
      <v-container>
        <h3>Add parts</h3>
        <v-sheet class="mx-auto" width="300">
          <v-form @submit.prevent>
            <v-text-field
              v-model="namePart"
              :rules="rules"
              label="Name Part"
            ></v-text-field>
            <v-btn class="mt-2" type="submit" block @click="submit" >Submit</v-btn>
            
          </v-form>
        </v-sheet>
      </v-container>
  
     
      
  
      <v-container style="margin-top:3rem">
        <h3 style="margin-bottom:2rem">All parts</h3>
      <v-row>
        <v-col
          v-for="(part, index) in parts"
          :key="index"
          cols="12"
          md="4"
        >        
            <v-card
              class="pa-3"
            >
              <span>{{ part.part_name }}</span>
            </v-card>
        </v-col>
      </v-row>
    </v-container>
  
  
  
  
  
    </v-app>
  </template>
  
  <script>
  import axios from "axios";
  import DownloadTable from './DownloadTable.vue';
  import UploadTable from './UploadTable.vue';
  
  
  export default {
    components: {
      DownloadTable,
      UploadTable
    },
    data() {
      return {
        headers: [],
        parts: [],
        tableData: [],
        namePart: '',
        rules: [
          value => {
            if (value?.length <= 10) return true
            return 'Name must be less than 10 characters.'
          },
        ],
      };
    },
    methods: {
      async fetchParts() {
        try {
          // Fetch parts data
          const response = await axios.get("http://localhost:8000/parts");
          this.parts = response.data;
  
          // Define headers, first column as "Part Name", others based on part names
          this.headers = [
            { text: "Part Name", value: "part_name" },
            ...this.parts.map(part => ({ text: part.part_name, value: part.part_name }))
          ];
  
          // Fetch changeover data
          const responseChangeOver = await axios.get("http://localhost:8000/changeOver");
          const changeOverData = responseChangeOver.data;
  
          // Construct the table data with changeover times
          this.tableData = this.parts.map(part => {
            const changeoverTimes = {};
  
            // Map changeover times by matching from_part_id and to_part_id
            changeOverData.forEach(changeover => {
              if (changeover.from_part_id === part.id) {
                const toPart = this.parts.find(p => p.id === changeover.to_part_id);
                if (toPart) {
                  changeoverTimes[toPart.part_name] = changeover.changeover_time;
                }
              }
            });
  
            console.log("header", this.headers);
            
            console.log("changeOverData",changeOverData);
            
  
            return {
              id: part.id,
              part_name: part.part_name,
              changeoverTimes
            };
          });
  
          console.log(this.tableData);
          
  
        } catch (error) {
          console.error("Error fetching parts or changeover data:", error);
        }
      },
  
  
  
      async submit() {
      try {
        const response = await fetch("http://localhost:8000/parts/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ part_name: this.namePart }),
        });
  
        if (!response.ok) {
          const errorData = await response.json();
          console.error("Error:", errorData);
          throw new Error(errorData.detail || "Failed to add part");
        }
  
        const data = await response.json();
        console.log("Part added successfully:", data);
        this.parts.push(data)
        this.namePart = ""; // Reset input field
        location.reload();
  
      } catch (error) {
        console.error("Failed to add part", error);
        alert(error.message);
      }
    }
  
  
    },
    mounted() {
      this.fetchParts();
    }
  };
  </script>
  
  <style scoped>
  .grey-background {
    background-color: grey;
  }
  </style>
  