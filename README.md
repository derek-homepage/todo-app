# 待办事项应用程序

这是一个使用FastAPI作为后端，Vue.js作为前端的简单待办事项应用程序。

## 功能

- 添加新的待办事项
- 查看所有待办事项
- 更新待办事项的完成状态
- 删除待办事项

## 如何启动应用程序

### 后端

1. 确保已安装Python 3.7+
2. 安装所需的依赖：
   ```
   pip install fastapi uvicorn
   ```
3. 在项目根目录下运行以下命令启动后端服务器：
   ```
   uvicorn main:app --reload
   ```
   服务器将在 http://localhost:8000 上运行

### 前端

1. 确保已安装Node.js和npm
2. 在项目根目录下安装依赖：
   ```
   npm install vue axios
   npm install --save-dev vite @vitejs/plugin-vue
   ```
3. 创建一个 `vite.config.js` 文件在项目根目录，内容如下：
   ```javascript
   import { defineConfig } from 'vite'
   import vue from '@vitejs/plugin-vue'

   export default defineConfig({
     plugins: [vue()]
   })
   ```
4. 在 `package.json` 文件中添加以下脚本：
   ```json
   "scripts": {
     "dev": "vite",
     "build": "vite build",
     "preview": "vite preview"
   }
   ```
5. 启动开发服务器：
   ```
   npm run dev
   ```
   前端应用将在 http://localhost:5173 上运行（或者命令行中显示的其他地址）

6. 在浏览器中打开显示的地址即可使用应用程序

## API文档

启动后端服务器后，可以在 http://localhost:8000/docs 查看自动生成的API文档。

## 技术栈

- 后端：FastAPI
- 前端：Vue.js 3
- 构建工具：Vite
- HTTP客户端：Axios

## 如何开始

1. 克隆仓库：
   ```bash
   git clone https://github.com/您的用户名/todo-app.git
   cd todo-app
   ```

2. 按照以下说明设置后端和前端。

## 贡献

欢迎提交问题和拉取请求。对于重大更改，请先开issue讨论您想要更改的内容。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)
