import React from "react";
import PropTypes from "prop-types";

class DefaultPropsHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "默认Props-header",
    };
  }
  render() {
    return (
      <div>
        <h2>
          -----{this.props.title}-------{this.props.num}
        </h2>
      </div>
    );
  }
}

// 如果父组件调用子组件的时候不给子组件传值，可以在子组件中使用defaultProps定义的默认值
DefaultPropsHeader.defaultProps = {
  title: "标题",
};
// 通过propsTypes定义父组件给子组件传值的类型
DefaultPropsHeader.propTypes = {
  num: PropTypes.number,
};

export default DefaultPropsHeader;
