import axios from "axios";
import { Component } from "react";
import "../assets/css/basic.css";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
    };
  }

  componentDidMount() {
    var api = "http://a.itying.com/api/productlist";
    axios
      .get(api)
      .then((Response) => {
        console.log(Response.data);
        this.setState({
          list: Response.data.result,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    return (
      <>
        <h2>首页</h2>
        <div className="content">
          <div className="item">
            <h3 className="item_cate">皮蛋瘦肉粥</h3>

            <ul className="item_list">
              <li>
                <div className="inner">
                  <img src={require("../assets/images/1.jpg")} />
                  <p className="title">大蒜腊肉</p>
                  <p className="price">¥26</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </>
    );
  }
}

export default Home;
