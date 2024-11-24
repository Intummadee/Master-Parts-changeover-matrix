<template>
    <v-app :theme="theme"> 
      <!-- คลาสของ theme ถูกผูกไว้กับ <v-app> ผ่าน :class="theme" -->
      <!-- v-app = Primary Component -->
      <!-- v-main = Content area -->
      <v-app-bar  title="App bar" :elevation="8">
        <v-spacer></v-spacer>
        <v-btn 
          :icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
          @click="onToggleTheme"  
        >
          Toggle Theme
        </v-btn>
  
        <v-navigation-drawer>
          <v-list>
            <v-list-item title="Navigation drawer"></v-list-item>
          </v-list>
        </v-navigation-drawer>
  
        <v-main>
          <v-container>
            <h1>Main Content</h1>
          </v-container>
        </v-main>
  
      </v-app-bar>
    </v-app>
  </template>