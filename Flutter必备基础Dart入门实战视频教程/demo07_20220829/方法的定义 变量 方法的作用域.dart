/**
  * 自定义方法的基本格式：
      返回类型 方法名称 （参数1，参数2）{
        方法体
        return 返回值
      }
  */

void printInfo() {
  print('自定义方法');
}

void main(List<String> args) {
  print('内置方法');
  printInfo();

  int getNum() {
    return 123;
  }

  print(getNum());
}
