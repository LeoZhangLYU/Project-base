void main(List<String> args) {
  // if which
  bool flag1 = true;
  if (flag1) {
    print("真");
  }
  String sex = '男';
  switch (sex) {
    case '男':
      {
        print('男');
        break;
      }
    case '女':
      {
        print('女');
        break;
      }
    default:
      {
        print('传入参数错误');
        break;
      }
  }

  // 三目运算符
  bool flag2 = true;
  String c = flag2 ? '我是true' : '我是false';
  print(c);

  // ??运算符   参考赋值运算符
}
