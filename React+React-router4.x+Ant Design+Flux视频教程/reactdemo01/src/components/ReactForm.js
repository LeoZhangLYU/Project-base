import React from "react";

class ReactForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            msg: "react表单",
            name: "",
            sex: "1",
            city: "上海",
            citys: [
                "北京", "上海", "深圳"
            ],
            hobby: [
                {
                    'title': '睡觉',
                    'checked': true,
                },
                {
                    'title': '吃法',
                    'checked': false,
                },
                {
                    'title': '敲代码',
                    'checked': true,
                }
            ],
            info: "beijingshanghai",
        };
    }

    handleSubmit = (event) => {
        // 阻止submit提交事件
        event.preventDefault();
        console.log(this.state.name, this.state.sex, this.state.city, this.state.hobby, this.state.info)
    }
    handelName = (event) => {
        this.setState({
            name: event.target.value
        })
    }
    handelSex = (event) => {
        this.setState({
            sex: event.target.value
        })
    }
    handleCity = (event) => {
        this.setState({
            city: event.target.value
        })
    }
    handleHobby = (key) => {

        var hobby = this.state.hobby;
        hobby[key].checked = !hobby[key].checked
        this.setState({
            hobby: hobby
        })
    }
    handleInfo = (event) => {
        this.setState({
            info: event.target.value
        })
    }

    render() {
        return (
            <div>
                <h2>{this.state.msg}</h2>

                <form onSubmit={this.handleSubmit}>
                    用户名：<input type="text" value={this.state.name} onChange={this.handelName} />
                    性别：
                    男<input type="radio" value="1" checked={this.state.sex == 1} onChange={this.handelSex} />
                    女<input type="radio" value="2" checked={this.state.sex == 2} onChange={this.handelSex} />
                    居住城市：
                    <select value={this.state.city} onChange={this.handleCity}>
                        {
                            this.state.citys.map(function (value, key) {
                                return <option key={key}>{value}</option>
                            })
                        }
                    </select>
                    爱好：
                    {
                        // 注意this指向
                        this.state.hobby.map((value, key) => {
                            return (
                                <span key={key}>
                                    <input type="checkbox" checked={value.checked} onChange={this.handleHobby.bind(this, key)} />{value.title}
                                </span>
                            )
                        })
                    }
                    <textarea value={this.state.info} onChange={this.handleInfo}></textarea>
                    <input type="submit" defaultValue="提交" />
                </form>
            </div>
        );
    }
}

export default ReactForm;