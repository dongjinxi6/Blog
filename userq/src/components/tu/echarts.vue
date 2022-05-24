<template>
  <div>
      <div v-for="i,j in data_title" :key="j">
      <templates class="asd" :num="[i, data_json[j]]" ></templates> <br><br>
      </div>

      <!-- <templates class="asd" num="line_chart"></templates><br><br><br>
      <templates class="asd" num="bing"></templates> -->
  </div>
</template>

<script>
import templates from "./Template"
import {show_echarts} from '../axios_api/api'
export default {
    data(){
        return {
            // ids:"",
            // data_echarts:{},
            data_json : [],
            data_title: []
        }
    },
    components:{
        templates
    },

    mounted() {
    show_echarts()
    .then(r=>{
        // console.log(r);
        this.data_json = r
        this.data_title = r.slice(-1)[0]
        console.log(this.data_json);
        console.log(this.data_title);
        // for (var item = 1; item <= r.slice(-1).length; item++) {
        //     this.ids = r.slice(-1).slice(item)
        //     this.data_echarts = r.slice(item)
        // }
    })
}
}
</script>

<style>
   .asd{
       left: 10px;  
        width: 300px;height: 250px;
        border-radius: 60px;
        background: linear-gradient(145deg, #f0f0f0, #cacaca);
        box-shadow:  20px 20px 53px #bebebe,
             -20px -20px 53px #ffffff;
    }
</style>
