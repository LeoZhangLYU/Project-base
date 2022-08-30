import 'dart:ffi';

void main(List<String> args) {
  // 自执行方法
  ((int n) {
    print('我是自执行方法-----$n');
  })(12);
}
