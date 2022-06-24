import logo from './assets/images/logo.svg';
// import './assets/css/App.css';


// 引入Home组件
// import Home from './components/Home'
// 引入News组件
// import News from './components/News';

// import Home05 from './components/Home05';
// import List from './components/List';
import TodeList from './components/TodeList';


function App() {

  //jsx：js与html混写
  return (
    <div className="App">
      你好，react，根组件
      {/* <Home05></Home05> */}
      {/* <List></List> */}
      <TodeList></TodeList>
    </div>
  );
}

export default App;
