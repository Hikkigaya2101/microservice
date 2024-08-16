<template>
<div class = 'app'>
  
  <h1>Страница с постами</h1>
  
<post-list :posts="posts" 
@remove ="removePost" /> 

<my-button
  @click = "ShowDialog">Создать пользователя
</my-button>

  <my-dialog v-model:show="dialogVisible">
  
    <post-form  @create="createPost"/>
  </my-dialog>


<div class="wave">
</div>
<div class="wave">
</div>
<div class="wave">
</div>
<custom-list :custom="custom"/> 
</div>

</template>
<script>
import PostForm from '@/components/PostForm';
import PostList from "@/components/PostList";
import CustomList from "@/components/CustomList";
//import axios from 'axios';
import { HTTP } from '@/axios/common'

export default{
  components:{PostForm,PostList,CustomList},
data(){
return{

posts:[{id:'',
name:'',
parent:'',
type:''}
],
custom:[{
id:'1',
name:'Паньшин Никита Вадимович',
data_birthday:'21.01.2001',
}
],

  dialogVisible: false,
  }},
   mounted(){
HTTP.get('unit').then(response=>this.posts = response.data);
console.log(this.posts)
},
   
   
methods:
{createPost(post){
   this.posts.push(post);
   this.dialogVisible = false;

},
removePost(post){
this.posts = this.posts.filter(p =>p.id !== post.id);

},
ShowDialog(){
  this.dialogVisible = true;
},
async getUnit(){
  const units=(await HTTP.get('/unit')).data;
  console.log(units);
  return units;


}
}
}


</script>

<style>
body{ margin:0;
  padding:0;
  box-sizing: border-box;
  color:  #fcfffc;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
	font-size: 17px;


  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    overflow: auto;
    background: linear-gradient(315deg, rgba(101,0,94,1) 3%, rgba(60,132,206,1) 38%, rgba(48,238,226,1) 68%, rgba(255,25,25,1) 98%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;
}



@keyframes gradient {
    0% {
        background-position: 0% 0%;
    }
    50% {
        background-position: 100% 100%;
    }
    100% {
        background-position: 0% 0%;
    }
}

.wave {
    background: rgb(255 255 255 / 25%);
    border-radius: 1000% 1000% 0 0;
    position: fixed;
    width: 200%;
    height: 12em;
    animation: wave 10s -3s linear infinite;
    transform: translate3d(0, 0, 0);
    opacity: 0.8;
    bottom: 0;
    left: 0;
    z-index: -1;
}

.wave:nth-of-type(2) {
    bottom: -1.25em;
    animation: wave 18s linear reverse infinite;
    opacity: 0.8;
}

.wave:nth-of-type(3) {
    bottom: -2.5em;
    animation: wave 20s -1s reverse infinite;
    opacity: 0.9;
}

@keyframes wave {
    2% {
        transform: translateX(1);
    }

    25% {
        transform: translateX(-25%);
    }

    50% {
        transform: translateX(-50%);
    }

    75% {
        transform: translateX(-25%);
    }

    100% {
        transform: translateX(1);
    }
}



</style>
