/**
 * mixins的实例类型是什么？
 * mixins的类型就是其超类的子类型
 */
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

class C with A, B {}

void main(List<String> args) {
  var c = new C();
  c.printA();

  print(c is A);
  print(c is B);
  print(c is C);
}
