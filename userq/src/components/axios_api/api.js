


//将我们http.js中封装好的  get,post.put,delete  导过来
import { axios_get, axios_post, axios_delete, axios_put } from './http.js'

export const show_echarts = p => axios_get("echarts/show/", p) //全部验证码