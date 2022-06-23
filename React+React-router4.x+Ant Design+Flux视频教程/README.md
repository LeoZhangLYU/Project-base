# react+ant design 指北

### 创建项目

**搭建React开发环境之前的准备工作。**

1. 必须安装nodejs      注意：安装nodejs稳定版本

2. 安装 cnpm 用cnpm替代npm

   ```shell
   地址：http://npm.taobao.org/
   安装cnpm:
   	npm install -g cnpm --registry=https://registry.npm.taobao.org
   ```

3. 用yarn替代npm

```shell
	yarn的安装：
		第一种方法：参考官方文档https://yarn.bootcss.com/
		第二种方法：cnpm install -g yarn  或者 npm install -g yarn
```

搭建React开发环境的**第一种方法**（老-现在推荐）：https://reactjs.org/docs/create-a-new-react-app.html

1. 必须要安装nodejs     注意：安装nodejs稳定版本      教程中的nodejs版本:v8.11.2            教程中的npm版本:v5.6.0

2. 安装脚手架工具   （单文件组件项目生成工具）   只需要安装一次

   ```
   npm install -g create-react-app   /  cnpm install -g create-react-app
   ```

3. 创建项目   （可能创建多次），找到项目要创建的目录：

   ```
   create-react-app reactdemo
   ```

4. cd  到项目里面	

```
cd  reactdemo
		npm start             yarn start运行项目
		npm run build         yarn build 生成项目
```

搭建React开发环境的**第二种方法**（新-未来推荐）：https://reactjs.org/docs/create-a-new-react-app.html

1. 必须要安装nodejs     注意：安装nodejs稳定版本      教程中的nodejs版本:v8.11.2            教程中的npm版本:v5.6.0

2. 安装脚手架工具并创建项目，找到项目要创建的目录执行：

   ```
   npx create-react-app reactdemo
   ```

3. cd  到项目里面

   ```
   	cd  reactdemo
   ```

4. ```
   	npm start  运行项目（调试）
       npm run build 生成项目（发布）
   ```

### 文件描述

- reactdemo01------------------------01 React的介绍、yarn npx、用React脚手架create-react-app搭建React环境  运行React项目（22分13秒）/方法一
- reactdemo02------------------------01 React的介绍、yarn npx、用React脚手架create-react-app搭建React环境  运行React项目（22分13秒）/方法二