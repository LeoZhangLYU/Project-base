void main(List<String> args) {
  var o1 = new Object();
  var o2 = new Object();
  print(identical(o1, o2)); //false
  print(identical(o1, o1)); //true

  // 实例化常量构造函数
  // a1和a2共享了存储空间
  var a1 = const Object();
  var a2 = const Object();
  print(identical(a1, a2));
}
