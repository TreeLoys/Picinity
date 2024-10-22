<template>
  <div class="nav">
    <div class="itemit itempath" @click="frawit"> {{ props.fullpath }}</div>
    <div style="width: 100%"></div>
    <div class="itemit itembutton up">../</div>
    <div class="itemit itembutton"><img src="/change.svg" alt="Change" width="32" height="32"/></div>
  </div>
</template>
<script setup>
import {ref, onMounted} from 'vue'
const props = defineProps(['fullpath'])
function frawit (){
  console.log(props.fullpath)
}
</script>


<style scoped>
.nav {
  display: flex;
  font-size: large;
}
.itempath{
  color: gray;
}
.itemit {
  display: flex;
  padding: 25px;
  margin: 5px;
}

.itembutton {
  background-color: #f5f5f5;
  border-radius: 15px;
  cursor: pointer;
}

.up {
  width: 45px;
  justify-content: center;
  margin-right: 15px;
}
</style>
<!-- Valera -->
<!-- 22:59 -->