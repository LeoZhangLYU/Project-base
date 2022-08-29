/**
 * forEach
 * map
 * where
 * any
 * every
 */
void main(List<String> args) {
  List myList = ['香蕉', '苹果', '西瓜'];
  for (var i = 0; i < myList.length; i++) {
    print(myList[i]);
  }
  for (var item in myList) {
    print(item);
  }
  myList.forEach((value) {
    print('$value');
  });

  List newList = [1, 2, 3, 4];
  var newList2 = newList.map((value) {
    return value * 2;
  });
  print(newList2);

  List whereList = [1, 2, 3, 4, 5];
  var whereList2 = whereList.where((value) {
    return value > 5;
  });
  print(whereList2);

/**
 * any:只要集合中有满足条件的返回true
 */
  List anyList = [1, 2, 3, 4, 5];
  var anyList2 = anyList.any((value) {
    return value > 3;
  });
  print(anyList2);

  /**
   * every:集合中每个元素都满足条件
   */
  List everyList = [2, 3, 4, 5];
  var everyList2 = everyList.every((value) {
    return value > 1;
  });
  print(everyList2);

  var person = {
    "name": "张三",
    "age": 20,
    "work": ["程序员", "外卖"]
  };
  person.forEach((key, value) {
    print("$key-----$value");
  });
}
