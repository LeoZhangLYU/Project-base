void main(List<String> args) {
  // 定义方式1
  var List1 = ['张三', 20, true];
  print(List1);
  print(List1.length);
  print(List1[0]);
  // 定义方式2 指定类型
  var List2 = <String>['张三', '李四'];
  print(List2);
  // 定义方式3 增加数据
  var List3 = [];
  print(List3);
  List3.add('张三');
  List3.add(20);
  print(List3);
  // 定义方式4
  // var List4 = new List();    //已经废弃
  var List4 = List.filled(6, ""); //创建一个固定长度的集合，无法通过add增加数据，但是可以修改数据
  var List5 = List<String>.filled(6, "");
  print(List4);
}
