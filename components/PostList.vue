
<template>
  
        <div class ='menu' v-if = "posts.length > 0 ">
            <h3>Список подразделений</h3>
 
<post-item v-for = "post in posts" 
:post="post" 
:key="post.id"
@remove = "$emit('remove',post)"/>
<my-button>Создать пользователя</my-button>
</div>
<h2 v-else style="color:red">
    Список пользователей пуст
</h2>

</template>

<script>
import PostItem from '@/components/PostItem';

export default{
    components:{PostItem},

props:{
 posts:{
  type: Array,
  required:true,
 }

}


}

</script>

<style>

.menu{
	padding: 5vh 20px;
	height: 70vh;
	border-right: 7px solid #fcfffc;
	position: fixed;
	opacity: 0.7;
	transition: 0.4s ease;
}


</style>