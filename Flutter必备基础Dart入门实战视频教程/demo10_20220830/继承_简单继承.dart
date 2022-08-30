class Person {
  String name = '法外狂徒张三';
  num age = 12;
  void printInfo() {
    print('${this.name}-----------${this.age}');
  }
}

class Web extends Person {}

void main(List<String> args) {
  Web w = new Web();
  w.printInfo();
}
