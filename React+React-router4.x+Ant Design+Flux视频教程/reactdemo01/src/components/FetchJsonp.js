import React from "react";
import fetchJsonp from "fetch-jsonp";

class FetchJsonp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
    };
  }

  getData = () => {
    var api = "http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20"; //接口后台允许了跨域
    fetchJsonp(api)
      .then(function (response) {
        return response.json();
      })
      .then((json) => {
        this.setState({
          list: json.result,
        });
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  };
  render() {
    return (
      <div>
        <h2>FetchJsonp获取jsonp接口的数据</h2>
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

export default FetchJsonp;
