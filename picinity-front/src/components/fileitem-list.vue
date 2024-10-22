<template>
  <div class="fileitem-list" @click="emit('btnup', props.fileitem.path)">
    <div class="icon-list">
      <img v-if="props.fileitem.isDrive" src="/server.svg" />
      <img v-if="props.fileitem.isDir" src="/folder.svg" />
      <img v-if="props.fileitem.isFile" src="/file.svg" />
    </div>
    <div>{{props.fileitem.path}}</div>
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
.fileitem-list {
  display: flex;

  cursor: pointer;
}
.fileitem-list{
  padding: 25px;
  padding-bottom: 18px;
  font-size: large;
}
.fileitem-list:hover{
  background-color: seashell;
}
.icon-list img{
  filter: opacity(80%);
  margin-right: 25px;
  width:28px;
  height:28px;
}
.disk{
}
</style>
