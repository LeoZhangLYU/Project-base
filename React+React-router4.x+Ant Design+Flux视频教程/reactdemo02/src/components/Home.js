import axios from "axios";
import { Component } from "react";
import { Link } from "react-router-dom";
import "../assets/css/basic.css";
import "../assets/css/index.css";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
      domain: "http://a.itying.com/",
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
      <div className="home">
        <h2>首页</h2>
        <div className="list">
          {this.state.list.map((value, key) => {
            return (
              <div className="item" key={key}>
                <h3 className="item_cate">{value.title}</h3>

                <ul className="item_list">
                  {value.list.map((value, key) => {
                    return (
                      <li key={key}>
                        <Link to={`/pcontent/${value._id}`}>
                          <div className="inner">
                            <img src={`${this.state.domain}${value.img_url}`} />
                            <p className="title">{value.title}</p>
                            <p className="price">{value.price}元</p>
                          </div>
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}

export default Home;
