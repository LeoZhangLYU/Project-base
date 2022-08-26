void main(List<String> args) {
  // 字符串定义的几种方式
  var str1 = 'this is a str';
  var str2 = "this is a str";
  print(str1);
  print(str2);

  String str3 = 'this is a String';
  String str4 = "this is a String";
  print(str3);
  print(str4);

  String str5 = '''第一行
  第二行
  
  第四行''';
  print(str5);

  // 字符串的拼接
  String str6 = '你好';
  String str7 = 'Dart';
  print(str6 + str7);
  print("$str6 $str7");
}
