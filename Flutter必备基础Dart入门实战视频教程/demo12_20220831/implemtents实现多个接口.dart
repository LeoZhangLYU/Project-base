/**
 * 一个类实现多个接口
 */
abstract class A {
  late String name;
  printA();
}

abstract class B {
  printB();
}

class C implements A, B {
  @override
  late String name;

  @override
  printA() {
    // TODO: implement printA
    throw UnimplementedError();
  }

  @override
  printB() {
    // TODO: implement printB
    throw UnimplementedError();
  }
}

void main(List<String> args) {
  C c = new C();
  c.printA();
}
