void main(List<String> args) {
  // 可选参数
  String getUserInfo(String username, [int? age]) {
    if (age != null) return '姓名:$username------------年龄:$age';
    return '姓名:$username';
  }

  print(getUserInfo('张三'));

  // 命名参数{}
  String getUserInfo2(String username, {int? age, String sex = '男'}) {
    if (age != null) return '姓名:$username-----性别:$sex-------年龄:$age';
    return '姓名:$username-----性别:$sex';
  }

  print(getUserInfo2('张三', sex: '女'));

  // 默认参数[]
  String getUserInfo3(String username, [String sex = '男', int? age]) {
    // 注意无法具体执行参数，参数顺序不能乱
    if (age != null) return '姓名:$username-----性别:$sex-------年龄:$age';
    return '姓名:$username-----性别:$sex';
  }

  print(getUserInfo3('张三', '女'));

  // 实现一个把方法当作参数的方法
  fn1() {
    print('fn1');
  }

  fn2(Function fnName) {
    fnName();
  }

  fn2(fn1);

  // 匿名方法
  var fn = () {
    print('我是一个匿名方法');
  };
  fn();
}
