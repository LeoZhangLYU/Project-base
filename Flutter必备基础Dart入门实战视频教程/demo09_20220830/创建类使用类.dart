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
  // 实例化
  Person p1 = new Person();
  print(p1.name);
  p1.getInfo();

  p1.setInfo('name');
  print(p1.name);
}
