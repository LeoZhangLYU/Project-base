import React from "react";

class TodeList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "111",
        };
    }

    inputChange = (event) => {
        this.setState({
            username: event.target.value
        })
    }
    setUsername=(event)=>{
        this.setState({
            username:'李四'
        })
    }

    render() {
        return (
            <div>
                <h2>双向数据绑定</h2>

                {/* model改变影响View view反过来影响model */}
                <input value={this.state.username} onChange={this.inputChange}></input>
                <p>{this.state.username}</p>
                <button onClick={this.setUsername}>改变username的值</button>
                <br />
                <br />
                <br />
                <hr />

            </div>
        );
    }
}

export default TodeList;