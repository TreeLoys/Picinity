<template>
  <div>
    <div>
      <nav-full :fullpath="fullpath"></nav-full>
      <div v-for="path in paths" class="list-btn" @click="clickOnPath(path)">{{path}}</div>
    </div>
  </div>
</template>
<script setup>
import navFull from './components/nav-full.vue'

import { ref, reactive, onMounted } from 'vue'
import api from './api.js'

var paths = ref([])
var fullpath = ref('')

async function  getDiskToPaths (){
  let response = await api.get("http://localhost:5333/api/getDisk")
  console.log(response)
    paths.value = response.map((el)=>{return el[0]})
}
async function getListPath(path){
  return await api.post("http://localhost:5333/api/getListDir", {path: path})
}
onMounted(async () => {
  await getDiskToPaths()
})

function clickOnPath(path){
  fullpath.value = fullpath.value + path + "\\"
  getListPath(fullpath.value).then((res)=>{
    paths.value = res
  })
}
</script>
<style scoped>
.btn-change {
  position: absolute;
  top: 15px;
  right: 15px;
  will-change: filter;
  transition: filter 300ms;
}
.list-btn{
  padding: 25px;
  font-size: large;
}
.list-btn:hover{
  background-color: seashell;
}
</style>
