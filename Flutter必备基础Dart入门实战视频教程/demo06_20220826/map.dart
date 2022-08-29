void main(List<String> args) {
  // 常用属性
  var person = {
    "name": "张三",
    "age": 20,
    "work": ["程序员", "外卖"]
  };
  print(person);
  print(person.keys);
  print(person.values);

  Map map = new Map();
  map['name'] = '李四';
  print(map);

  // 常用方法
  person.addAll({
    "height": 160,
    "wight": '170',
  });
  print(person);
  person.remove('height');
  print(person);
  print(person.containsValue('张三'));
}
