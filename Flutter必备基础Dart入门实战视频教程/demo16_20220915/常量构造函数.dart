/**
 * 1. 常量构造函数需以`const`关键字修饰
2. `const`构造函数必须用于成员变量都是`final`的类
3. 如果实例化时不加`const`修饰符，即使调用的是常量构造函数，实例化的对象也不是常量。
4. 实例化常量构造函数的时候，多个地方创建这个对象，如果传入的值相同，只会保留一个对象。
5. `Flutter`中`const`修饰不仅仅是节省组件构建时的内存开销，`Flutter`在需要重新构建组件的时候，重新构建没有意义，因此`Flutter`不会重新构建`const`组件。
 */

class Person {
  String name;
  Person({required this.name});
}

// 常量构造函数
class Container {
  final int width;
  final int height;
  const Container({required this.width, required this.height});
}

void main(List<String> args) {
  var P1 = new Person(name: '1');
  var P2 = new Person(name: '2');
  print(identical(P1, P2));

  var C1 = new Container(width: 10, height: 20);
  var C2 = new Container(width: 10, height: 20);
  print(identical(C1, C2));
  var C3 = const Container(width: 10, height: 20);
  var C4 = const Container(width: 10, height: 20);
  print(identical(C3, C4));
}
