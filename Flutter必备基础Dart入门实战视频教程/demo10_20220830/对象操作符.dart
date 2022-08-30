/**
 * as类型转换 is类型判断 ?判空  ..级联操作
 */
class Person {
  String name = '张三';
  int age = 2;
  void getInfo() {
    print('${this.name}-+-----${this.age}');
  }

  void setInfo(String name) {
    this.name = name;
  }
}

void main(List<String> args) {
  var p = new Person();
  p?.getInfo();
  print(p is Person);

  var p1;
  p1 = '';
  p1 = new Person();
  // p1.getInfo();
  (p1 as Person).getInfo();

// 级联操作
  Person p2 = new Person();
  p2.getInfo();
  p2
    ..name = '李四'
    ..age = 22
    ..getInfo();
}
