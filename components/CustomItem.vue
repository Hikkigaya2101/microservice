<template>
    <div class="custom_card">  
        <div><strong>id пользователя:</strong>{{ custom[0].id }}</div>
    <div><strong>ФИО:</strong>{{ custom[0].name }}</div>
    <div><strong>Дата рождения:</strong>{{ custom[0].data_birthday }}</div>
                
        </div>
        
    </template>
    
    <script>
    
    export default{
    props:{
     post:{
      type: Array,
      required:true,
     }
    
    }
    
    }
    
    </script>
    
    <style scoped>
    
    .custom_item{
    padding:15px;
    border: 2px solid teal;
    margin-top: 15px;
    }
    </style>