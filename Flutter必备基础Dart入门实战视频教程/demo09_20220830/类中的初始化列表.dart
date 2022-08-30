class React {
  late num height;
  late num width;
  React()
      : width = 2,
        height = 2 {}
  get area {
    return this.height * this.width;
  }

  set setHeight(value) {
    this.height = value;
  }
}

void main(List<String> args) {
  React r = new React();
  print(r.area);
  r.setHeight = 7;
  print(r.area);
}
