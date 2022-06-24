import React from "react";
import "../assets/css/index.css";

class TodoList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "1111",
      list: [],
    };
  }

  title = React.createRef("");
  addData = () => {
    // alert(this.title.current.value);
    var tempList = this.state.list;
    tempList.push(this.title.current.value);
    this.title.current.value = "";
    this.setState({
      list: tempList,
    });
  };
  removeData = (key) => {
    var tempList = this.state.list;
    tempList.pop(key);
    this.setState({
      list: tempList,
    });
  };

  render() {
    return (
      <div className="TodoList">
        <h2>React TodeList案例演示</h2>
        <input ref={this.title} /> <button onClick={this.addData}>增加+</button>
        <hr />
        <ul>
          {this.state.list.map((value, key) => {
            return (
              <li key={key}>
                {value}-----------
                <button onClick={this.removeData.bind(this, key)}>删除</button>
              </li>
            );
          })}
        </ul>
      </div>
    );
  }
}

export default TodoList;
