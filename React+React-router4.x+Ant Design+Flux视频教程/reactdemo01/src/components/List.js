import React from "react";

class List extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: React.createRef(),
        }

    }
    // username = React.createRef();
    inputChange = () => {

        /**
         * 获取dom节点
         * 1.给元素定义ref属性  <input ref='username'
         * 2.通过this.refs.username获取dom节点
         */
        // let value = this.username.current.value;
    }
    getInput = () => {
        alert(this.state.username.current.value)
    }

    inputKeyUp = (event) => {
        console.log(event.keyCode);
        if(event.keyCode == 13){
            alert(event.target.value)
        }
    }

    render() {
        return (
            <div>
                <h2>我是List组件</h2>
                {/* 获取表单的值
                1.监听表单的改变事件                     onChange
                2.在改变的事件里面获取表单输入的值        ref
                3.把表单输入的值赋值给username           this.setState({username})
                4.点击按钮的时候获取state里面的username的值   this.state.username
                */}
                <input ref={this.state.username} onChange={this.inputChange} /><button onClick={this.getInput}>获取input的值</button>
                <br />
                <br />
                <br />
                <hr />
                <h2>键盘事件</h2>
                <input onKeyUp={this.inputKeyUp} />
            </div>
        );
    }
}

export default List;