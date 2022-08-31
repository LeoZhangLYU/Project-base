/**
 * 泛型就是解决类 接口 方法的复用性、以及对不特定数据类型的支持（类型校验）
 */

T getData<T>(T value) {
  return value;
}

void main(List<String> args) {
  getData('123456'); //不带类型校验
  getData<int>(123456); //带类型校验
  print(getData('123456'));
  print(getData<int>(123456));
}
