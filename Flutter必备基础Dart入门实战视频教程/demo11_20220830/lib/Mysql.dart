import 'Db.dart';

class Mysql implements Db {
  @override
  late String uri;
  Mysql(this.uri);

  @override
  add(String data) {
    // TODO: implement add
    print('Mysql的add方法' + data);
  }

  @override
  delete() {
    // TODO: implement delete
  }

  @override
  edit() {
    // TODO: implement edit
  }
}
