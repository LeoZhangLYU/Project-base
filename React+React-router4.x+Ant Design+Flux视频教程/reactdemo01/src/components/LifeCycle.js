import { Component } from "react";

/**
 * 必须记住的生命周期函数：
 * 加载的时候：componentWillMount、componentDidMount(dom操作)、render
 * 更新的时候：componentWillUpdate、componentDidUpdate、render
 * 销毁的时候：componentWillUnmount
 */
class LifeCycle extends Component {
  constructor(props) {
    super(props);
    console.log("01构造函数");
    this.state = {
      msg: "我是一个msg",
    };
  }

  //   数据将要挂载的时候触发的生命周期函数
  componentWillMount() {
    console.log("02组件将要挂载");
  }
  //   组件挂载完成的时候触发的生命周期函数;
  componentDidMount() {
    // dom操作，数据请求操作放在这里面
    console.log("04数据挂载完成");
  }
  //   是否要更新数据 如果返回true才会执行更新数据的操作
  shouldComponentUpdate(nextProps, nextState) {
    console.log("01是否要更新数据");
    console.log(nextProps);
    console.log(nextState);
    return true;
  }
  //   将要更新数据的时候触发
  componentWillUpdate() {
    console.log("01组件将要更新");
  }
  //   组件更新完成
  componentDidUpdate() {
    console.log("02组件数据更新完成");
  }
  //   组件销毁的时候触发的生命周期函数
  componentWillUnmount() {
    console.log("组件销毁");
  }
  //   父组件里面改变props传值的时候触发;
  componentWillReceiveProps() {
    console.log("父子组件传值，父组件里面改变了props的值触发的方法");
  }

  setMsg = () => {
    this.setState({
      msg: "我是改变后的msg",
    });
  };

  render() {
    console.log("03数据渲染render");
    return (
      <div>
        <h2>
          生命周期函数演示-----------{this.state.msg}-------------
          {this.props.title}
        </h2>
        <hr />
        <button onClick={this.setMsg}>更新msg的数据</button>
      </div>
    );
  }
}

export default LifeCycle;
