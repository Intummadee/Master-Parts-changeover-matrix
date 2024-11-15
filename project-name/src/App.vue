<template>
  <v-app>
    <v-container>
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
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      headers: [],
      parts: [],
      tableData: []
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

          console.log(changeOverData);
          

          return {
            id: part.id,
            part_name: part.part_name,
            changeoverTimes
          };
        });

      } catch (error) {
        console.error("Error fetching parts or changeover data:", error);
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
