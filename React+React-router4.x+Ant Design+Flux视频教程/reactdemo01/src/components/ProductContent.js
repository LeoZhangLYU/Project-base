import { Component } from "react";
import { useSearchParams } from "react-router-dom";

class ProductContent extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    console.log(this.props);
  }

  render() {
    return (
      <>
        <div>我是商品详情组件</div>
        <Child />
      </>
    );
  }
}
function Child() {
  // We can use the `useParams` hook here to access
  // the dynamic pieces of the URL.
  const [searchParams, setSearchParams] = useSearchParams();
  let aid = searchParams.get("aid");
  console.log(searchParams.get("aid"));
  return (
    <div>
      <h3>AID: {aid}</h3>
    </div>
  );
}
export default ProductContent;
