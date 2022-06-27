import logo from "./assets/images/logo.svg";
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
function App() {
  //jsx：js与html混写
  return (
    <div className="App">
      你好，react，根组件
      <HomePage></HomePage>
      {/* <NewsPage></NewsPage> */}
      {/* <Home05></Home05> */}
      {/* <List></List> */}
      {/* <TodeList></TodeList> */}
      {/* <ReactForm></ReactForm> */}
      {/* <TodoList></TodoList> */}
      {/* <Header></Header> */}
    </div>
  );
}

export default App;
