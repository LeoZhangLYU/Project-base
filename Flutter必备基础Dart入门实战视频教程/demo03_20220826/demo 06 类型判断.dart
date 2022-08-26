void main(List<String> args) {
  var str = '1234';
  if (str is String) {
    print("String类型");
  } else if (str is int) {
    print("int类型");
  }
}
