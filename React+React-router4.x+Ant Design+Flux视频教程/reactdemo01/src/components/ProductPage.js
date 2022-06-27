import { Component } from "react";
import { Link } from "react-router-dom";

class ProductPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [
        {
          aid: 111,
          title: "我是商品111",
        },
        {
          aid: 222,
          title: "我是商品222",
        },
        {
          aid: 333,
          title: "我是商品333",
        },
        {
          aid: 444,
          title: "我是商品444",
        },
      ],
    };
  }
  render() {
    return (
      <div>
        <h2>这是一个product组件</h2>
        <hr />
        <ul>
          {this.state.list.map((value, key) => {
            return (
              <li key={key}>
                <Link to={`/productcontent?aid=${value.aid}`}>
                  {value.title}
                </Link>
              </li>
            );
          })}
        </ul>
        <br />
      </div>
    );
  }
}

export default ProductPage;
