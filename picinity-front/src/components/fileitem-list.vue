<template>
  <div class="fileitem-list" @click="emit('btnup', props.fileitem)">
    <div class="icon-list typing-icon">
      <img v-if="props.fileitem.isDrive" src="/server.svg" />
      <img v-if="props.fileitem.isDir" src="/folder.svg" />
      <img v-if="props.fileitem.isFile" src="/file.svg" class="img-file"/>
    </div>
    <div class="item-name">{{props.fileitem.path}}</div>
    <img v-if="['jpg','jpeg', 'bmp', 'png', 'gif'].includes(props.fileitem.ext)"
         :src="'http://127.0.0.1:5333/api/it/78/'+props.fileitem.path">
  </div>
</template>
<script setup>
import {ref, reactive, onMounted} from 'vue'
import api from '../api.js'
const emit = defineEmits(['btnup'])
const props = defineProps(['fileitem'])
let data = ref(0)
</script>


<style scoped>
.fileitem-list{
  display: flex;
  cursor: pointer;
  font-size: large;
}
.fileitem-list:hover{
  background-color: seashell;
}
.icon-list img{
  filter: opacity(80%);
  width:28px;
  height:28px;
  padding: 25px;
  padding-bottom: 18px;
}
.img-file{
  filter: opacity(60%) !important;
}
.item-name{
  padding: 25px;
  padding-left: 0;
  width: 100%;
}
</style>
