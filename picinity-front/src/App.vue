<template>
  <div>
    <div>
      <nav-full :fullpath="fullpath" @btnup="clickBtnUp"></nav-full>
      <fileitem-list v-for="fileitem in fileitems" :fileitem="fileitem" @btnup="clickOnPath"></fileitem-list>
    </div>
  </div>
</template>
<script setup>
import navFull from './components/nav-full.vue'
import fileitemList from './components/fileitem-list.vue'

import { ref, reactive, onMounted } from 'vue'
import api from './api.js'

var fileitems = ref([])
var fullpath = ref('')

async function getDiskToPaths (){
  let response = await api.get("http://localhost:5333/api/getDisk")
  console.log(response)
    fileitems.value = response.map((el)=>{return {path:el[0], isDrive: true}})
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
    fileitems.value = res
  })
}
function clickBtnUp() {
  console.log("Click btn up")
  let pathArray = fullpath.value.split('\\');
  // Отобразить диски если дальше некуда
  if (pathArray.length === 3 || pathArray.length === 2){
    fullpath.value = ""
    getDiskToPaths()
  }else{
    // Если последний хрен пустой
    if (pathArray.pop().length === 0){
      pathArray.pop()
    }

    fullpath.value = pathArray.join('\\');
    getListPath(fullpath.value).then((res)=>{
      fileitems.value = res
    })
  }

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

</style>
