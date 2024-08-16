<template>
<div class="post">  
    
    <div>
        <div><strong>Название:</strong>{{ post.name }}</div>
    <div><strong>Тип:</strong>{{ post.type }}</div>
    
    </div>
    <div class="post__btns">
        <my-button @click="$emit('remove',post)">Удалить</my-button>
    </div>
    </div>
    
</template>

<script>

export default{
props:{
 post:{
  type: Object,
  required:true,
 }

}

}

</script>

<style scoped>

.post{
padding:15px;
border: 2px solid teal;
margin-top: 15px;
}
</style>