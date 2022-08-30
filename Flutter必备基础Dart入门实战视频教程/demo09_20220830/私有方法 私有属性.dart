import 'lib/Animal.dart';

/**
 * 使用_将属性或方法定义成私有
 * 且仅在单独的类文件中才生效
 */
void main(List<String> args) {
  Animal a = new Animal('小狗', 2);
  print(a.age);
  // print(a._name);
  a.exeRun(); //执行私有方法，间接调用
}
