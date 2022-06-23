import React, { Component } from "react";
import image1 from "../assets/images/微信图片_20220622131904.jpg";
import '../assets/css/index.css'

class News extends React.Component {

    constructor(props) {
        super(props);   //用于父子组件传值，建议作为标准固定写法

        // 定义数据
        this.state = {
            msg: "新闻",
            list: ["111111111", "222222222", "33333333"],
            list2: [<h2 key="1">我是一个h2</h2>, <h2 key="2">我是一个h2</h2>, <h2 key="3">我是一个h2</h2>],
            list3: [
                { title: "新闻1111" },
                { title: "新闻2222" },
                { title: "新闻3333" },
                { title: "新闻4444" },
                { title: "新闻5555" },
            ]
        }
    }

    render() {

        let listResult = this.state.list.map(function (value, key) {
            return <li key={key}>{value}</li>
        })
        return (
            <div className="news">
                {this.state.msg}
                <br />
                <img src={image1}></img>
                <img src={require("../assets/images/微信图片_20220622131904.jpg")}></img>
                <img src="https://www.baidu.com/img/flexible/logo/pc/result.png"></img>
                <hr />
                {this.state.list2}
                <hr />
                <ul>
                    {listResult}
                </ul>
                <hr />
                <ul>
                    {
                        this.state.list3.map(function (value, key) {
                            return <li key={key}>{value.title}</li>
                        })
                    }
                </ul>
            </div>
        )

    }
}

export default News;