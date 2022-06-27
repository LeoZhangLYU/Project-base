import React from "react";

// import Header from "./Header";
// import DefaultPropsHeader from "./DefaultPropsHeader";
import Axios from "./Axios";
import FetchJsonp from "./FetchJsonp";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "这是一个首页组件",
      title: "首页组件",
      count: 20,
    };
  }
  render() {
    return (
      <div>
        {/* <Header title={this.state.title}></Header> */}
        {/* <DefaultPropsHeader
          title={this.state.title}
          num={this.state.count}
        ></DefaultPropsHeader> */}
        <Axios></Axios>
        <FetchJsonp></FetchJsonp>
        <br />
        <hr />
        <h2>这是首页组件的内容</h2>
      </div>
    );
  }
}

export default HomePage;
