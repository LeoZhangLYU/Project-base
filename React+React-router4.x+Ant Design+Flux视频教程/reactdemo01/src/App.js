import logo from './assets/images/logo.svg';
// import './assets/css/App.css';


// 引入Home组件
// import Home from './components/Home'
// 引入News组件
import News from './components/News';

function App() {

  //jsx：js与html混写
  return (
    <div className="App">
      你好，react，根组件
      <News></News>
    </div>
  );
}

export default App;
