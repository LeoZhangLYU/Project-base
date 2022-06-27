import React from "react";
import axios from "axios";

class Axios extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
    };
  }

  getData = () => {
    var api = "http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20"; //接口后台允许了跨域
    axios
      .get(api)
      .then((resp) => {
        console.log(resp.data.result);
        // 用到this，要注意this指向
        this.setState({
          list: resp.data.result,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  render() {
    return (
      <div>
        <h2>Axios获取服务器数据</h2>

        <button onClick={this.getData}>获取服务器api接口数据</button>
        <hr />
        <ul>
          {this.state.list.map((value, key) => {
            return <li key={key}>{value.title}</li>;
          })}
        </ul>
      </div>
    );
  }
}

export default Axios;
