<template>
<div>
    <div>
    <div :id=ids  style="width: 300px;height: 250px;" ></div>
     <el-button
        type="text"
        v-clipboard:copy="ids"
        v-clipboard:success="handleCopy"
        v-clipboard:error="handleError"
    >点击复制</el-button>

    </div>
</div>
</template>
<script>
import histogram from "./data/Histogram.json"
import line_chart from "./data/Line_chart.json"
import bing from "./data/bing.json"
    export default {
        name: '',
        data() {
            return {
                ids:"histogram",
                data_echarts:{},
            }
        },
        methods: {
            drawLine(id) {
                this.charts = this.$echarts.init(document.getElementById(this.ids))
                this.charts.setOption(this.data_echarts)
            },
            copy () {
                //创建input标签
                var input = document.createElement('input')
                //将input的值设置为需要复制的内容
                input.value = this.data_echarts;
                //添加input标签
                document.body.appendChild(input)
                //选中input标签
                input.select()
                //执行复制
                document.execCommand('copy')
                //成功提示信息
                //移除input标签
                document.body.removeChild(input)
            },
              handleCopy() {
                    this.$messagesouth({
                    message: "复制成功",
                    type: "comm",
                    center: true
                    });
                },
            handleError() {
                this.$messagesouth({
                message: "复制失败",
                type: "comm",
                center: true
                });
            }

        },
        //调用
        mounted() {
            console.log(this.num)
            this.ids = this.num[0]
            this.data_echarts = this.num[1]
            this.$nextTick(function() {
                this.drawLine(this.ids)
            })
            
            
        },
        props:['num']
    }
</script>
<style scoped>
    /* * {
        margin: 0;
        padding: 0;
        list-style: none;
    } */
 
</style>