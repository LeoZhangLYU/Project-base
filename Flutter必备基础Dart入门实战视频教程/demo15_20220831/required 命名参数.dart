class Person {
  String? name;
  num age;
  Person({this.name, required this.age});
  void getPersonInfo() {
    print('${this.name}-------${this.age}');
  }
}

void main(List<String> args) {
  Person person = new Person(name: '法外狂徒', age: 30);
  person.getPersonInfo();

  Person person1 = new Person(age: 20);
  person1.getPersonInfo();
}
