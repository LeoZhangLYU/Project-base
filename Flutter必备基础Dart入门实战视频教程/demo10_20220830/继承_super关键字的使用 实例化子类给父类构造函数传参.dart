class Person {
  late String name = '法外狂徒张三';
  late num age = 12;
  Person(this.name, this.age);
  void printInfo() {
    print('${this.name}-----------${this.age}');
  }
}

class Web extends Person {
  late String sex;
  Web(String name, num age, String sex) : super(name, age) {
    this.sex = sex;
  }
  @override
  void printInfo() {
    // TODO: implement printInfo
    print('${this.name}-----------${this.age}-----------${this.sex}');
  }

  void run() {
    print('${this.name}-----------${this.age}-----------${this.sex}');
    super.printInfo(); //子类调用父类方法
  }
}

void main(List<String> args) {
  Person p = new Person('name', 20);
  p.printInfo();

  Web w = new Web('李四', 50, '女');
  w.printInfo();
  w.run();
}
