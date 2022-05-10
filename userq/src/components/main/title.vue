<template>
    <div>
        <vue-particles
                color="#409eff"
                :particleOpacity="0.7"
                :particlesNumber="100"
                shapeType="star"
                :particleSize="4"
                linesColor="#daa520"
                :linesWidth="2"
                :lineLinked="true"
                :lineOpacity="0.4"
                :linesDistance="150"
                :moveSpeed="3"
                :hoverEffect="true"
                hoverMode="grab"
                :clickEffect="true"
                clickMode="push"
                class="cash"
        >
        </vue-particles>
        <div class="auto_title">
          <a href="a" class="as">首页</a>
          <a href="a" class="as">可视化</a>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {}
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
