class Animal {
  late String _name;
  late int age;
  Animal(String name, int age) {
    this._name = name;
    this.age = age;
  }
  void _run() {
    print('私有方法');
  }

  void exeRun() {
    this._run();
  }
}
