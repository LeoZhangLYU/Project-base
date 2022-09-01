void main(List<String> args) {
  String getUserInfo(String username, {required int age, required String sex}) {
    return '姓名:$username-----性别:$sex-------年龄:$age';
  }

  // print(getUserInfo('username', sex: '女'));
  //The named parameter 'age' is required, but there's no corresponding argument.
  print(getUserInfo('username', age: 12, sex: '男'));

  // 命名参数{}
  String getUserInfo2(String username, {int? age, String sex = '男'}) {
    if (age != null) return '姓名:$username-----性别:$sex-------年龄:$age';
    return '姓名:$username-----性别:$sex';
  }

  print(getUserInfo2('张三', sex: '女'));
}
