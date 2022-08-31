class PrintClass<T> {
  List list = <T>[];
  void add(T value) {
    this.list.add(value);
  }

  void printList() {
    print(this.list);
  }
}

void main(List<String> args) {
  PrintClass printClassString = new PrintClass<String>();
  printClassString.add('xxxx');
  printClassString.printList();

  PrintClass printClassNum = new PrintClass<num>();
  printClassNum.add(123);
  printClassNum.printList();

  PrintClass printClass = new PrintClass();
  printClass.add('xxxx');
  printClass.add(123);
  printClass.printList();
}
