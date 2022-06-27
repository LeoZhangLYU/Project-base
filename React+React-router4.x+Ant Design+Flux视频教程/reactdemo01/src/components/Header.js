import React from "react";

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "这是一个头部组件",
    };
  }

  getNews = () => {
    alert(this.props.news.state.msg);
  };
  render() {
    return (
      <div>
        <h2>{this.props.title}</h2>
        <button onClick={this.props.run}>调用父组件的run方法</button>
        <br />
        <br />
        <button onClick={this.props.news.getData}>
          获取整个news组件的getData方法
        </button>
        <br />
        <br />
        <button onClick={this.getNews}>获取整个news组件实例</button>
        <br />
        <br />
        <button
          onClick={this.props.news.getChildData.bind(this, "我是子组件的数据")}
        >
          子组件给父组件传值
        </button>
      </div>
    );
  }
}

Header.defaultProps = {
  title: "标题",
};
export default Header;
