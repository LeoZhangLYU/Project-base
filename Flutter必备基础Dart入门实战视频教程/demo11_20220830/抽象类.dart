abstract class Animal {
  void eat();
  void printInfo() {
    print('抽象类中的普通方法');
  }
}

class Dog extends Animal {
  @override
  void eat() {
    // TODO: implement eat
    print('小狗在吃');
  }
}

class Cat extends Animal {
  @override
  void eat() {
    // TODO: implement eat
    print('小猫在吃');
  }
}

void main(List<String> args) {
  Dog dog = new Dog();
  dog.eat();
  Cat cat = new Cat();
  cat.eat();
  // Animal animal = new Animal();        //抽象类不能被直接实例化
  cat.printInfo();
}
