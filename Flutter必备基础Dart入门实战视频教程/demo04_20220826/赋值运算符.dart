void main(List<String> args) {
  // 基础赋值运算符   =  ??=
  int a = 10;
  int b = 3;
  int c = a + b;
  print(c);

  var d;
  d ??= 23; //表示d为空的话把23赋值给d
  print(d);
  // 复合赋值运算符  += -= *= /= %= ~/=
  var e = 12;
  print(e += 10); //表示e= e+10
}
