void main(List<String> args) {
  // Number与String类型之间的转换
  String str1 = "456";
  var num1 = int.parse(str1);
  print(num1 is int);

  String price = "";
  try {
    print(double.parse(price));
  } catch (err) {
    print(double.parse(price = "0"));
    print(err);
  }

  var num2 = 12;
  var str2 = num2.toString();
  print(str2 is String);

  // 其他类型转bool类型

  var str3 = 'xxx';
  if (str3.isEmpty) {
    print("str3 为空");
  } else {
    print("str3 不为空");
  }
}
