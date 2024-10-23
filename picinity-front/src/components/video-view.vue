<template>
    <div class="viewer">
        <div class="btn-all btn-close">
            <img src="/minimize.svg" width="78" height="78" @click="emit('btnminimize')"/>
        </div>
        <div class="btn-all btn-prev">
            <img src="/arrow-left.svg" width="78" height="78" @click="emit('btnprev')"/>
        </div>
        <div class="btn-all btn-next">
            <img src="/arrow-right.svg" width="78" height="78" @click="emit('btnnext')"/>
        </div>
        <div class="image-wrapper">
            <video width="640" height="480" controls :key="globals.getUrl('video/')+props.pathtovideo">
                <source class="image"
                        :src="globals.getUrl('video/')+props.pathtovideo"
                        :type="'video/'+getExt()">
            </video>
        </div>
    </div>
</template>

<script setup>
    import globals from '../globals.js'
    const props = defineProps(['pathtovideo'])
    const emit = defineEmits(['btnnext', 'btnprev', 'btnminimize'])
    console.log("getExt()", getExt())
    function getExt() {
        return props.pathtovideo.split(".").pop()
    }
</script>

<style scoped>

    .viewer {
        display: flex;
        position: absolute;
        height: 100vh;
        width: 100%;
        background-color: rgb(20, 20, 20);
        justify-content: center;
        align-items: center;
        overflow-y: hidden;
    }
    .btn-all {
        filter: invert() opacity(80%);
        background-color: rgba(255, 255, 255, 0.1);
    }
    .btn-close {
        position: absolute;
        top: 5px;
        right: 5px;
        width: 78px;
        height: 78px;
        border-radius: 15px;
        cursor: pointer;
    }
    .btn-next {
        position: absolute;
        top: 200px;
        right: 5px;
        width: 78px;
        height: 78px;

        border-radius: 15px;
        cursor: pointer;
    }
    .btn-prev {
        position: absolute;
        top: 100px;
        right: 5px;
        width: 78px;
        height: 78px;
        border-radius: 15px;
        cursor: pointer;
    }
    .image {
        height: auto;
        width: auto;
        max-width: 100vw;
        max-height: 100vh;
    }

    .image-wrapper {

    }
</style>