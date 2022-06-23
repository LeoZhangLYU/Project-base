import React, { Component } from "react";
import App from "../App";
import '../assets/css/index.css'

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
            title: "我是一个title",
            red: "red",
            style:{
                color:"red",
                fontSize:"40px"
            }
        }
    }

    // jsx：js与html混写
    render() {
        return (
            <div>
                <h2>{this.state.msg}</h2>

                <div title="1111">我是一个div</div>
                <br />
                <div id="box" title={this.state.title}>我是一个div    box</div>
                <br />
                <div className='red'>我是一个红色的div</div>
                <br />
                <div className={this.state.red}>我是一个红色的div 111</div>

                <br/>
                <label htmlFor="name">姓名</label>
                <input id="name" />

                <br/>
                <div style={{"color":"red"}}>我是一个红色的div 行内样式</div>
                <br/>
                <div style={this.state.style}>我是一个红色的div 行内样式</div>
            </div >
        )
    }
}

export default Home;