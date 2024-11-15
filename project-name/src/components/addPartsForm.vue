<template>
  <v-sheet class="mx-auto" width="300">
    <v-form @submit.prevent>
      <v-text-field
        v-model="namePart"
        :rules="rules"
        label="Name Part"
      ></v-text-field>
      <v-btn class="mt-2" type="submit" block>Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
  export default {
    props: {
      parts: Array
    },
    data: () => ({
      namePart: '',
      rules: [
        value => {
          if (value) return true

          return 'You must enter a first name.'
        },
        value => {
          if (value?.length <= 10) return true
          return 'Name must be less than 10 characters.'
        },
      ],
    }),

    methods: {
    async submitForm() {
      try {
        // Prepare the part data to send to the backend
        const partData = {
          name: this.namePart,
        }
        
        // const isDuplicate = this.props.parts.some(part => part.part_name === this.namePart)
        
        // // ชื่อ part ไม่ซ้ำกัน
        // console.log("this.props.parts 🥥🌴🌺🍍🌸🥥🌴🌺🍍🌸: ", this.props.parts);
        
        // if (isDuplicate){
        //   console.error("Duplicate part name, please choose a different name.")
        //   return
        // }
          

        // Send the POST request to the backend
        const response = await fetch("http://localhost:8000/parts/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(partData),
        })

        if (response.ok) {
          const newPart = await response.json()
          console.log("Part added successfully:", newPart)
          // Optionally, reset the form or show a success message
          this.namePart = ''  // Reset name field
        } else {
          console.error("Error adding part:", await response.text())
        }
      } catch (error) {
        console.error("Network error:", error)
      }
    },



  },
}
</script>