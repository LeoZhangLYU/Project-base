void main(List<String> args) {
  // 第1种定义方式
  var person = {
    "name": "张三",
    "age": 20,
    "work": ["程序员", "外卖"]
  };
  print(person);
  print(person["age"]);
  // 第2种定义方式
  var person2 = new Map();
  person2['name'] = '李四';
  print(person2);
}
