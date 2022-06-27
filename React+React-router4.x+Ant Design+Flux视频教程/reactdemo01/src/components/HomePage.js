import React from "react";

// import Header from "./Header";
// import DefaultPropsHeader from "./DefaultPropsHeader";
// import Axios from "./Axios";
// import FetchJsonp from "./FetchJsonp";
import LifeCycle from "./LifeCycle";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "这是一个首页组件",
      title: "首页组件",
      count: 20,
      flag: true,
    };
  }

  setFlag = () => {
    this.setState({
      flag: !this.state.flag,
    });
  };
  settitle = () => {
    this.setState({
      title: "我是父组件改变后的title",
    });
  };

  render() {
    return (
      <div>
        {/* <Header title={this.state.title}></Header> */}
        {/* <DefaultPropsHeader
          title={this.state.title}
          num={this.state.count}
        ></DefaultPropsHeader> */}
        {/* <Axios></Axios> */}
        {/* <FetchJsonp></FetchJsonp> */}
        <hr />
        {this.state.flag ? <LifeCycle title={this.state.title} /> : ""}
        <button onClick={this.setFlag}>挂载和销毁生命周期函数的组件</button>
        <button onClick={this.settitle}>改变父组件title的值</button>
        <br />
        <hr />
        <h2>这是首页组件的内容</h2>
      </div>
    );
  }
}

export default HomePage;
