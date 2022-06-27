import logo from "./assets/images/logo.svg";
import { Routes, Route, Link } from "react-router-dom";
// import './assets/css/App.css';

// 引入Home组件
// import Home from "./components/Home";
// 引入News组件
// import News from './components/News';

// import Home05 from './components/Home05';
// import List from './components/List';
// import TodeList from './components/TodeList';
// import ReactForm from './components/ReactForm';
// import TodoList from "./components/TodoList";

import HomePage from "./components/HomePage";
import NewsPage from "./components/NewsPage";
import ProductPage from "./components/ProductPage";
function App() {
  //jsx：js与html混写
  return (
    <>
      <div className="App">
        {/* 你好，react，根组件  */}
        {/* <HomePage></HomePage> */}
        {/* <NewsPage></NewsPage> */}
        {/* <Home05></Home05> */}
        {/* <List></List> */}
        {/* <TodeList></TodeList> */}
        {/* <ReactForm></ReactForm> */}
        {/* <TodoList></TodoList> */}
        {/* <Header></Header> */}
      </div>
      <hr />
      <nav>
        <Link to="/">首页</Link>
        <Link to="/news">新闻</Link>
        <Link to="/product">商品</Link>
      </nav>
      <hr />
      <Routes>
        <Route exact path="/" element={<HomePage></HomePage>} />
        {/* exact表示严格匹配 */}
        <Route path="/news" element={<NewsPage></NewsPage>} />
        <Route path="/product" element={<ProductPage></ProductPage>} />
      </Routes>
    </>
  );
}

export default App;
