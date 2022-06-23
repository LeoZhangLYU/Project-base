import React, { Component } from "react";

class News extends React.Component{

    constructor(props){
        super(props);   //用于父子组件传值，建议作为标准固定写法

        // 定义数据
        this.state={
            userInfo:"张三",
        }
    }

    render(){
        return(
            <div>
                <h2>{this.state.userInfo}</h2>
                <ul>
                    <li>这是一个数据</li>
                    <li>这是一个数据</li>
                    <li>这是一个数据</li>
                    <li>这是一个数据</li>
                </ul>
            </div>
        )
    }
}

export default News;