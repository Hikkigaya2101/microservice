<template>
    <div class = 'add_form'>
    <form @submit.prevent>
        <h4>Создание поста</h4>
        <my-input
         v-model="post.id"
           
          placeholder="Название"/>
          <my-input  v-model = "post.name"  placeholder="Описание"/>
        <my-button  style ='align-self: flex-end' @click='createPost' >Создать</my-button>
        
        </form>
    </div>
</template>

<style scoped>


</style >

<script>


export default {

    data(){
       return{
        post:{
            id:'',
           name:'',
           parent:'',
           type:''
        }
    }
},
    methods:{
createPost(){
this.post.id= Date.now();
this.$emit('create',this.post)
this.post = {name : '',type : ''}
        }
    }
}
    
</script>