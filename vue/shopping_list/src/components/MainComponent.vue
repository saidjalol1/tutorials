<template>
    <div class="container">
             <div class="form">
                 <div class="input">
                     <input type="text" v-model="title" placeholder="item name">
                     <button @click="add(title)">Add</button>
                 </div>
             </div>
             <div class="list">
                 <div v-for="(item, index) in items" :key="item.id">
                     <span class="name">{{ item.name }}</span>
                     <span class="remove" @click="removeItem(index)">remove</span>
                 </div>
             </div>
    </div>
 </template>
 
 <script setup>
 const items = [
     {
         'id': 0,
         'name': 'Nmadur'
     },
     {
         'id': 1,
         'name': 'Nmadur 2'
     },
     {
         'id': 2,
         'name': 'Nmadur 3'
     },
     {
         'id': 3,
         'name': 'Nmadur 4'
     },
 ]
 let title = ''
 let id = items.length // Initialize id with the length of the items array
 
 const add = (itemName) => {
     id++; // Increment id for the next item
     items.push({
         "id": id,
         "name": itemName
     });
 }
 
 const removeItem = (index) => {
     items.splice(index, 1);
 }
 </script>
 

<style scoped>
.form{
    margin: 0 auto;
    text-align: center;
}
.input {
    margin-top: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    column-gap: 10px;
}
input{
    width: 50%;
    padding: 1% 1%;
    outline: none;
    border-radius: 10px;
    font-size: 20px;
}
input:focus{
    border-color: blue;
}
button{
    background-color: #000000;
    color: white;
    border-radius: 10px;
    padding: 1% 1%;
    font-size: 20px;
    cursor: pointer;
}

.list{
    width: 100%;
    border: 1px solid gray;
    margin-top: 40px;
    padding: 5% 5%;
    border-radius: 10px;
}
.list .name {
    font-size: 20px;
    font-weight: 900;
    color: blue;
}
.list div{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1% 5%;
}
.list div:hover{
    background-color: gray;
}
.list .remove{
    cursor: pointer;
    padding: 1%;
    background-color: red;
    color: white;
    border-radius: 10px;
}
</style>