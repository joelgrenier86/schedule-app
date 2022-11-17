<template>
    <q-layout view="hHh lpR fFf">
  
      <q-header elevated class="bg-primary text-white">
        <q-toolbar>
          <q-toolbar-title>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
            </q-avatar>
            Teklabs
          </q-toolbar-title>
        </q-toolbar>
      </q-header>
  
      <q-page-container>
        <router-view />
      </q-page-container>
  
      <q-footer elevated class="bg-primary text-white">
        <q-toolbar>
          <q-toolbar-title>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
            </q-avatar>
            <div>Schedule an appointment</div>
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>
  
    </q-layout>
  </template>
  
  
  <script>
  import { ref } from 'vue'
  
  export default {
     name: 'ScheduleLayout',
  
   
  }
  </script>