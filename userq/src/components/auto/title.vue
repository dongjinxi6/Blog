<template>
  <div class="auto_title">
    <router-link to='index' class="as" >首页</router-link>
    <router-link to='echarts' class="as" >可视化</router-link>
    <router-link to='index' class="as" >题目</router-link>
  </div>
</template>

<script>
export default {
  data(){
    return{

    }
  }
}
</script>

<style>
.cash{
  position:fixed;
  top:0;
  width:100%;
}
.auto_title{
  /* border:1px dashed #000;  */
  width: 100%;
  height: 50px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.as{
  
  /* position:fixed; */
  top: 15px;
  font-size: 20px;
  text-decoration-line: none;
  color:black;
}
</style>
