import React from "react";

class Footer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "这是一个底部组件",
    };
  }

  run = () => {
    alert("我是底部组件的run方法");
  };
  render() {
    return (
      <div>
        <h2>我是一个底部组件</h2>
      </div>
    );
  }
}

export default Footer;
