/**
 * 1.React是React的核心库
 * 2.react-dom.js是提供与DOM相关的功能
 */
import React from "react";
import ReactDOM from "react-dom/client";
// import './index.css';            //css可以删掉

// 引入App.js这个组件
import App from "./App";

//不用管，加快react运行速度的一个js文件
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
