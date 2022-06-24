import React from "react";

import Header from "./Header";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "这是一个首页组件",
      title: "首页组件",
    };
  }
  render() {
    return (
      <div>
        <Header title={this.state.title}></Header>
        <br />
        <hr />
        <h2>这是首页组件的内容</h2>
      </div>
    );
  }
}

export default HomePage;
