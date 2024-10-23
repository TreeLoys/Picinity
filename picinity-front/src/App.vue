<template>
    <div style="height: 100%;">
        <div v-if="guiView === 'filewalker'">
            <nav-full :fullpath="fullpath" @btnup="clickBtnUp" @btnchange="clickFollow"></nav-full>
            <fileitem-list v-for="fileitem in fileitems" :fileitem="fileitem" @btnup="clickOnPath"></fileitem-list>
        </div>
        <div v-if="guiView === 'imageview'">
            <image-view :pathtoimg="pathtoimg"
                        @btnminimize="imageviewMinimize"
                        @btnnext="imageviewNext"
                        @btnprev="imageviewPrev"
            ></image-view>
        </div>
        <div v-if="guiView === 'videoview'">
            <video-view :pathtovideo="pathtovideo"
                        @btnminimize="videoviewMinimize"
                        @btnnext="videoviewNext"
                        @btnprev="videoviewPrev"
            ></video-view>
        </div>
    </div>
</template>
<script setup>
    import navFull from './components/nav-full.vue'
    import fileitemList from './components/fileitem-list.vue'
    import imageView from './components/image-view.vue'
    import videoView from './components/video-view.vue'

    import {ref, reactive, onMounted} from 'vue'
    import api from './api.js'
    import globals from './globals.js'

    var fileitems = ref([])
    var fullpath = ref('')

    var guiView = ref("filewalker")
    var pathtoimg = ref("")
    var pathtovideo = ref("")
    var guiScroll = ref(0)
    const VIDEO_SUPPORTS = ['mp4', 'ogg', 'webm']
    const IMAGE_SUPPORTS = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
    async function getDiskToPaths() {
        let response = await api.get(globals.getUrl("getDisk"))
        console.log(response)
        fileitems.value = response.map((el) => {
            return {path: el[0], isDrive: true}
        })
    }

    async function getListPath(path) {
        return await api.post(globals.getUrl("getListDir"), {path: path})
    }

    onMounted(async () => {
        await getDiskToPaths()
    })

    function clickFollow(){
        getListPath("C:\\Users\\Sirenko\\Pictures").then((res) => {
            fileitems.value = res
        })
    }
    function clickOnPath(fileitem) {
        console.log("Click on", fileitem)
        let ext = fileitem.ext
        if (ext !== undefined)
            ext = ext.toLowerCase()
        if (IMAGE_SUPPORTS.includes(ext)) {
            guiScroll.value = window.scrollY
            guiView.value = "imageview"
            pathtoimg.value = fileitem.path
        }
        else if(VIDEO_SUPPORTS.includes(ext)){
            guiScroll.value = window.scrollY
            guiView.value = "videoview"
            pathtovideo.value = fileitem.path
        }
        else  {
            if (fileitem.isDir || fileitem.isDrive) {
                fullpath.value = fullpath.value + fileitem.path + "\\"
                getListPath(fullpath.value).then((res) => {
                    fileitems.value = res
                })
            }
        }
    }

    function clickBtnUp() {
        console.log("Click btn up")
        let pathArray = fullpath.value.split('\\');
        // Отобразить диски если дальше некуда
        if (pathArray.length === 3 || pathArray.length === 2) {
            fullpath.value = ""
            getDiskToPaths()
        } else {
            // Если последний хрен пустой
            if (pathArray.pop().length === 0) {
                pathArray.pop()
            }
            pathArray = pathArray.join('\\')
            pathArray += "\\"
            fullpath.value = pathArray;
            getListPath(fullpath.value).then((res) => {
                fileitems.value = res
            })
        }

    }
    /* Image */
    function imageviewMinimize() {
        guiView.value = 'filewalker'
        console.log(guiScroll.value)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 10)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 100)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 300)

    }

    function imageviewNext() {
        let imgs = fileitems.value.filter((el)=>{return IMAGE_SUPPORTS.includes(el.ext)})
        let posCurrImg = imgs.map(e => e.path).indexOf(pathtoimg.value)
        console.log("posCurrImg", posCurrImg)
        if(posCurrImg >= 0 && posCurrImg < imgs.length - 1){
            let nextItem = imgs[posCurrImg + 1]
            pathtoimg.value = nextItem.path
        }

    }
    function imageviewPrev() {
        let imgs = fileitems.value.filter((el)=>{return IMAGE_SUPPORTS.includes(el.ext)})
        let posCurrImg = imgs.map(e => e.path).indexOf(pathtoimg.value)
        console.log("posCurrImg", posCurrImg)
        if(posCurrImg >= 1 && posCurrImg < imgs.length){
            let nextItem = imgs[posCurrImg - 1]
            pathtoimg.value = nextItem.path
        }
    }

    /* Video */
    function videoviewMinimize() {
        guiView.value = 'filewalker'
        console.log(guiScroll.value)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 10)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 100)
        setTimeout(() => {
            window.scrollTo(0, guiScroll.value)
        }, 300)

    }

    function videoviewNext() {
        let imgs = fileitems.value.filter((el)=>{
            if (el.ext === undefined)
                return false
            return VIDEO_SUPPORTS.includes(el.ext.toLowerCase())
        })
        let posCurrImg = imgs.map(e => e.path).indexOf(pathtovideo.value)
        console.log("posCurrImg", posCurrImg)
        if(posCurrImg >= 0 && posCurrImg < imgs.length - 1){
            let nextItem = imgs[posCurrImg + 1]
            pathtovideo.value = nextItem.path
        }

    }
    function videoviewPrev() {
        let imgs = fileitems.value.filter((el)=>{
            if (el.ext === undefined)
                return false
            return VIDEO_SUPPORTS.includes(el.ext.toLowerCase())
        })
        let posCurrImg = imgs.map(e => e.path).indexOf(pathtovideo.value)
        console.log("posCurrImg", posCurrImg)
        if(posCurrImg >= 1 && posCurrImg < imgs.length){
            let nextItem = imgs[posCurrImg - 1]
            pathtovideo.value = nextItem.path
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
