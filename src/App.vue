<template>
  <div class="container">
    <h1 class="title">待办事项应用</h1>
    <form @submit.prevent="addTodo" class="add-form">
      <input v-model="newTodo" placeholder="添加新的待办事项" class="input" />
      <button type="submit" class="button">添加</button>
    </form>
    <ul class="todo-list">
      <li v-for="todo in todos" :key="todo.id" class="todo-item">
        <div class="todo-content">
          <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)" class="checkbox" />
          <span :class="{ completed: todo.completed }">{{ todo.title }}</span>
        </div>
        <button @click="deleteTodo(todo.id)" class="delete-button">删除</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      todos: [],
      newTodo: ''
    }
  },
  mounted() {
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const response = await axios.get('http://localhost:8000/todos/');
        this.todos = response.data;
      } catch (error) {
        console.error('获取待办事项失败:', error);
      }
    },
    async addTodo() {
      if (!this.newTodo.trim()) return;
      try {
        const response = await axios.post('http://localhost:8000/todos/', {
          title: this.newTodo,
          description: '',
          completed: false
        });
        this.todos.push(response.data);
        this.newTodo = '';
      } catch (error) {
        console.error('添加待办事项失败:', error.response ? error.response.data : error);
      }
    },
    async updateTodo(todo) {
      try {
        await axios.put(`http://localhost:8000/todos/${todo.id}`, todo);
      } catch (error) {
        console.error('更新待办事项失败:', error);
      }
    },
    async deleteTodo(id) {
      try {
        await axios.delete(`http://localhost:8000/todos/${id}`);
        this.todos = this.todos.filter(todo => todo.id !== id);
      } catch (error) {
        console.error('删除待办事项失败:', error);
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.title {
  text-align: center;
  color: #333;
}

.add-form {
  display: flex;
  margin-bottom: 20px;
}

.input {
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
}

.button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.button:hover {
  background-color: #45a049;
}

.todo-list {
  list-style-type: none;
  padding: 0;
}

.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  margin-bottom: 10px;
  border-radius: 4px;
}

.todo-content {
  display: flex;
  align-items: center;
}

.checkbox {
  margin-right: 10px;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

.delete-button {
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #d32f2f;
}
</style>