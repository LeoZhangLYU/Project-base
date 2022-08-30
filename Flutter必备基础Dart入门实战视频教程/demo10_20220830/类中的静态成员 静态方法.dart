import 'dart:ffi';

import '../demo07_20220829/方法的定义 变量 方法的作用域.dart';

/**
 * 1.使用static关键字来修饰类级别的变量和函数
 * 2.静态方法不能访问非静态成员，非静态方法可以访问静态成员
 */
class Person {
  static String name = '法外狂徒张三';
  int age = 20;
  static void show() {
    print(name);
  }

  void printInfo() {
    print(name); //访问静态属性
    // 访问非静态属性
    print(this.age);
    // 调用静态方法
    show();
  }

  static void printUserInfo() {
    // 静态属性
    print(name);
    // 静态方法
    show();
    // 静态方法不能访问非静态属性
    // print(age);
    // 静态方法不能访问非静态方法
    // printInfo();
  }
}

void main(List<String> args) {
  Person.show();
  print(Person.name);

  Person p = new Person();
  p.printInfo();
}
