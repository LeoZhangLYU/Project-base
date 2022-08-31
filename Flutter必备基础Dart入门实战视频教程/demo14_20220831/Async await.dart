void main(List<String> args) async {
  var result = await testAsync();
  print(result);
}

testAsync() async {
  return 'hello async';
}
