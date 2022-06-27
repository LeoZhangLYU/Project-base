import { Component } from "react";
import { useParams } from "react-router-dom";

class NewsContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      aid: null,
    };
  }

  componentDidMount() {
    // console.log(params);
    // this.Invoice();
  }

  render() {
    return (
      <>
        <h2>
          新闻详情组件----------
          <Child />
        </h2>
      </>
    );
  }
}

function Child() {
  // We can use the `useParams` hook here to access
  // the dynamic pieces of the URL.
  let { aid } = useParams();
  return (
    <div>
      <h3>AID: {aid}</h3>
    </div>
  );
}
export default NewsContent;
