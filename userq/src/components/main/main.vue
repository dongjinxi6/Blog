<template>
  <div>
      <div class="min"></div>
      <!-- 展示表头 -->
      <titles></titles>
      <router-view></router-view>
  </div>
</template>

<script>
import titles from "../auto/title.vue"
export default {
    components:{
        titles
    },
    data(){
        return{

        }
    }

}
</script>

<style>
</style>