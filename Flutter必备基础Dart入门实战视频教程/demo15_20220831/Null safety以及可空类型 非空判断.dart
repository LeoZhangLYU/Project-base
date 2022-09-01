void main(List<String> args) {
  var name = '张三';
  // name = null; //A value of type 'Null' can't be assigned to a variable of type 'String'.
  String? username = '法外狂徒';
  username = null;

  print(getData('www.pactera.com'));
  print(null);

  prientLength('123456');
  prientLength(null);
}

String? getData(getUrl) {
  if (getUrl != null) {
    return 'this is a not null String';
  } else {
    return null;
  }
}

void prientLength(String? str) {
  try {
    print(str!.length); //类型断言：如果str不等于null 会打印str的长度，如果等于null会抛出异常
  } catch (e) {
    print('str is null');
  }
}
