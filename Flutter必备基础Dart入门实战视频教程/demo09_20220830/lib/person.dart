class Person {
  late String name;
  late int age;

// 默认构造函数
  Person(String name, int age) {
    this.name = name;
    this.age = age;
    print('${this.name}-+-----${this.age}');
  }
  // 默认构造函数的简写
  // Person(this.name, this.age);
// 命名构造函数
  Person.createNewPerson(String name, int age) {
    this.name = name;
    this.age = age;
    print('${this.name}-+-----${this.age}');
  }

  void getInfo() {
    print('${this.name}-+-----${this.age}');
  }

  void setInfo(String name) {
    this.name = name;
  }
}
