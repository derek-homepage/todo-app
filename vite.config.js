import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  root: '.', // 确保 Vite 在正确的目录中查找 index.html
})