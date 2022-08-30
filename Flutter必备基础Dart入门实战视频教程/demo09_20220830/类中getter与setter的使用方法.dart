class React {
  late num height;
  late num width;
  React(this.height, this.width);
  get area {
    return this.height * this.width;
  }

  set setHeight(value) {
    this.height = value;
  }
}

void main(List<String> args) {
  React r = new React(10, 3);
  print(r.area);
  r.setHeight = 7;
  print(r.area);
}
