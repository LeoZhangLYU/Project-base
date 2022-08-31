/**
 * 和java一样，dart也有接口，但是和java有区别
 * 首先，dart的接口没有interface关键词定义接口，而是普通类和抽象类都可以作为接口被实现
 * 同样使用implement关键字进行实现
 * 但是dart的接口有点奇怪，如果实现的类是普通类，会将普通类和抽象中的属性的方法全部都需要覆写一遍
 * 而因为抽象类可以定义抽象方法，普通类不可以，所以一般如果要实现像java接口那样的方式，一般会使用抽象类
 * 建议使用抽象类定义接口
 */

/**
 * 定义一个DB库 支持mysql mssql mongodb
 * 三个类里面都有同样的方法
 */
import 'lib/Mssql.dart';
import 'lib/Mysql.dart';

void main(List<String> args) {
  Mysql mysql = new Mysql('xxx123456');
  mysql.add('xxx');

  Mssql mssql = new Mssql();
  mssql.uri = '127.0.0.1';
  mssql.add('增加数据');
}
