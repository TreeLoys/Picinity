<template>
  <div class="nav">
    <div class="itemit itempath" @click="frawit"> {{ props.fullpath }}</div>
    <div style=""></div>
    <div class="itemit itembutton up" @click="emit('btnup')">../</div>
    <div class="itemit itembutton" @click="emit('btnchange')"><img src="/change.svg" alt="Change" width="32" height="32"/></div>
  </div>
</template>
<script setup>
import {ref, onMounted} from 'vue'
const emit = defineEmits(['btnup', 'btnchange'])

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
  width: 100%;
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