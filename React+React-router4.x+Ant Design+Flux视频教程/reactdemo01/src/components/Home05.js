import React, { Component } from "react";
import App from "../App";
import '../assets/css/index.css'

class Home05 extends Component {

    constructor(props) {
        /** 子类必须在constructor方法中调用super方法，否则新建实例时会报错。
        这是因为子类没有自己的this对象，而是继承父类的this对象，然后对其进行加工。
        如果不调用super方法，子类就得不到this对象 */
        super(props);

        // 定义数据
        this.state = {
            msg: "我是一个Home组件",
        }

    }

    run = (event) =>{
        // alert(this.state.msg)
        // console.log(event)
        // alert(event.target)   //获取执行时间的DOM节点
        event.target.style.background= "red"

        // 获取DOM的属性
        alert(event.target.getAttribute('aid'))
    }

    inputChange=(event)=>{
        // console.log('111');
        // 获取表单的值
        console.log(event.target.value)
        this.setState({
            username:event.target.value,
        })
    }
    getInput=()=>{
        alert(this.state.username)
    }

    render() {
        return (
            <div>
                <h2>{this.state.msg}</h2>
                {/* 事件对象 */}
                <h2>事件对象演示</h2>
                <button aid="123" onClick={this.run}>事件对象</button>
                <br/>
                <br/>
                <br/>
                <hr/>
                <h2>表单事件</h2>
                {/* 获取表单的值
                1.监听表单的改变事件                     onChange
                2.在改变的事件里面获取表单输入的值        事件对象
                3.把表单输入的值赋值给username           this.setState({username})
                4.点击按钮的时候获取state里面的username的值   this.state.username
                */}
                <input onChange={this.inputChange}/><button onClick={this.getInput}>获取input的值</button>
            </div >
        )
    }
}

export default Home05;