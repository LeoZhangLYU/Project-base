import React, { Component } from "react";
import App from "../App";
import "../assets/css/index.css";

/**
 * 绑定属性注意:
 * class要变成className
 * for要换成htmlFor
 * style:<div style={{"color":"red"}}>我是一个红色的div 行内样式</div>
 * 其他的属性和以前一样
 */

class Home extends Component {
  constructor(props) {
    /** 子类必须在constructor方法中调用super方法，否则新建实例时会报错。
        这是因为子类没有自己的this对象，而是继承父类的this对象，然后对其进行加工。
        如果不调用super方法，子类就得不到this对象 */
    super(props);

    // 定义数据
    this.state = {
      msg: "我是一个Home组件",
      message: "我是一个Message",
      username: "itying",
    };

    // 第二种改变this的方法
    this.getMessage = this.getMessage.bind(this);
  }

  run() {
    alert("我是一个run方法");
  }

  getData() {
    alert(this.state.msg);
  }
  getMessage() {
    alert(this.state.message);
  }
  // 第三种改变this指向的方法
  getUserName = () => {
    alert(this.state.username);
  };

  setMeg = () => {
    //改变state的值
    this.setState({
      msg: "我是一个Home组件,这是改变后的值",
    });
  };

  setUsername = (str) => {
    //改变state的值
    this.setState({
      username: str,
    });
  };

  // jsx：js与html混写
  render() {
    return (
      <div>
        <h2>{this.state.msg}</h2>
        <h2>{this.state.username}</h2>
        <button onClick={this.run}>执行方法</button>
        <br />
        <br />
        <button onClick={this.getData.bind(this)}>
          获取数据----第一种:改变this指向的方法
        </button>
        <br />
        <br />
        <button onClick={this.getMessage}>
          获取数据----第二种:改变this指向的方法
        </button>
        <br />
        <br />
        <button onClick={this.getUserName}>
          获取数据----第三种:改变this指向的方法
        </button>
        <br />
        <br />
        <button onClick={this.setMeg}>改变state里面的值</button>
        <br />
        <br />
        <button onClick={this.setUsername.bind(this, "张三")}>
          执行方法传值
        </button>
      </div>
    );
  }
}

export default Home;
