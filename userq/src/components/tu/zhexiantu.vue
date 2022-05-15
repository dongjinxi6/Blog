<template>
    <!--为echarts准备一个具备大小的容器dom-->
    <div id="main" style="width: 300px;height: 500px;"></div>
</template>
<script>
    export default {
        name: '',
        data() {
            return {
                charts: '',
            /*  opinion: ["1", "3", "3", "4", "5"],*/
                opinionData: ["50", "30000", "20", "1000", "5"],
                dateList:["2022-5-2","2022-5-2","2022-5-2","2022-5-2","2022-5-2"]
            }
        },
        methods: {
            drawLine(id) {
                this.charts = this.$echarts.init(document.getElementById(id))
                this.charts.setOption({
                      visualMap: [
                        {
                        show: true,
                        type: 'continuous',
                        seriesIndex: 0,
                        min: 0,
                        max: 400
                        },
                    ],
                    title: [
                        {
                        left: 'center',
                        text: 'Gradient along the y axis'
                        },
                    ],
                    tooltip: {
                        trigger: 'axis'
                    },
                    xAxis: {
                        data: this.dateList
                    },
                    yAxis: {},
                    grid: [
                        {
                        bottom: '60%'
                        },
                        {
                        top: '60%'
                        }
                    ],
 
                    series: [{
                        name: '近七日收益',
                        type: 'line',
                        stack: '总量',
                        showSymbol: false,    
                        data: this.opinionData
                    },
                    // {
                    //     name: '哦吼',
                    //     type: 'line',
                    //     stack: '总量',
                    //     showSymbol: false,  
                    //     data: this.opinionData,
                    // }
                    ]
                })
            }
        },
        //调用
        mounted() {
            this.$nextTick(function() {
                this.drawLine('main')
            })
        }
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        list-style: none;
    }
</style>