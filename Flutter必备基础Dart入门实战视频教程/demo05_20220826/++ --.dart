void main(List<String> args) {
  var a = 10;
  var b = a++; //先赋值再运算
  var c = ++a; //先运算再赋值
  print(a);
  print(b);
  print(c);
}
