/**
 * 允许将子类类型的指针赋值给父类类型的指针，同一个函数调用会有不同的执行效果
 * 子类的实例赋值给父类的引用
 * 多态就是父类定义一个方法不去实现，让继承它的子类去实现，每个子类有不同的表现
 */
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

  void run() {
    print('小猫在跑');
  }
}

void main(List<String> args) {
  Animal cat = new Cat();
  cat.eat();
  // cat.run();
}
