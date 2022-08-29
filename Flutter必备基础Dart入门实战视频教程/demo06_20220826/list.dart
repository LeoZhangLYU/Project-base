void main(List<String> args) {
  // List中的属性
  List list1 = ['张三', '李四', '王五'];
  print(list1.length);
  print(list1.isEmpty);
  print(list1.isNotEmpty);
  print(list1.reversed.toList()); //列表倒序排序

  // List中的方法
  list1.add('法外狂徒');
  list1.addAll(['罗翔', '慢慢']);
  print(list1);
  print(list1.indexOf('法外狂徒'));
  print(list1);
  print(list1.remove("慢慢"));
  print(list1);
  print(list1.removeAt(1));
  print(list1);
  list1.fillRange(1, 2, '李四'); //修改不是新增
  print(list1);
  list1.insert(1, '我王五回来了');
  print(list1);
  list1.insertAll(2, ['我回来了1', '我回来了2']);
  print(list1);
  print(list1.join('---'));
}
