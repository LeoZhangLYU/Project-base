/**
 * 令变量既不会污染全局，又常驻内存（不会被垃圾回收机制回收）
 */
void main(List<String> args) {
  fn() {
    var a = 123;
    return () {
      a++;
      print(a);
    };
  }

  var b = fn();
  b();
  b();
}
