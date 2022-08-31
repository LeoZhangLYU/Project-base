/**
 * 在Dart中可以使用mixins实现类似多继承的功能
 * 因为使用mixins的条件，随着Dart版本一直在变，这里讲的是Dart2.x中使用mixins的条件：
 * 1.作为mixins的类只能继承自Object，不能继承其他类
 * 2.作为mixins的类不能有构造函数,但可以从extends父类继承构造函数
 * 3.一个类可以mixins多个mixins类
 * 4。mixins绝不是继承，也不是接口，二是一种全新的特性
 * 5.当mixins多个类时，如果具有相同的方法，后面的会替换掉前面的
 */

class Person {
  late String name;
  late num age;
  Person(this.name, this.age);
  run() {
    print('Person run');
  }
}

class A {
  String isA = 'this is A';
  printA() {
    print('A');
  }

  run() {
    print('A run');
  }
}

class B {
  printB() {
    print('B');
  }

  run() {
    print('B run');
  }
}

class C extends Person with A, B {
  C(super.name, super.age);
}

void main(List<String> args) {
  C c = new C('法外狂徒', 20);
  c.printA();
  print(c.isA);
  c.run();
  print(c.name);
}
