import axios from "axios";
import "../assets/css/pcontent.css";
import { Component } from "react";
import { useParams, useSearchParams } from "react-router-dom";

class Pcontent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: Object,
    };
  }
  render() {
    return (
      <>
        <h2>商品详情页面</h2>
        <Content />
        {/* <Detail /> */}
      </>
    );
  }
}

// function Detail() {
//   const [search, setSearch] = useSearchParams();
//   const id = search.get("id");
//   const title = search.get("title");
//   const content = search.get("content");
//   return (
//     <ul>
//       <li>
//         <button onClick={() => setSearch("id=008&title=哈哈&content=嘻嘻")}>
//           点我更新一下收到的search参数
//         </button>
//       </li>
//       <li>消息编号：{id}</li>
//       <li>消息标题：{title}</li>
//       <li>消息内容：{content}</li>
//     </ul>
//   );
// }
let list;

function Content() {
  let { id } = useParams();
  let list = "aaaa";
  axios
    .get("http://a.itying.com/api/productcontent?id=" + id)
    .then((response) => {
      console.log(response.data.result[0]);
      list = JSON.stringify(response.data.result[0]);
    })
    .catch((error) => {
      console.log(error);
    });
  return <p>{list}</p>;
}

export default Pcontent;
