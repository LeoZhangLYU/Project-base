abstract class Cache<T> {
  getByKey(String str);
  void setByKey(String key, T value);
}

class FileCache<T> implements Cache<T> {
  @override
  getByKey(String str) {
    // TODO: implement getByKey
    print('getByKey:${str}');
  }

  @override
  void setByKey(String key, T value) {
    // TODO: implement setByKey
    print('setByKey:${key}-------${value}');
  }
}

void main(List<String> args) {
  FileCache fileCache = new FileCache<Map>();
  fileCache.getByKey('456');
  fileCache.setByKey('123', {'姓名': '张三', '性别': '男'});
}
