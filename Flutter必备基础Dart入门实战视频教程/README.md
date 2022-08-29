# it营/Flutter必备基础Dart入门实战视频教程

## 文件描述

demo01_20220825------------------01 Dart介绍 Win Mac上面分别搭建Dart环境  开发工具配置 以及运行Dart

demo02_20220825------------------02 Dart 入口方法介绍 Dart打印 Dart注释  Dart变量 常量申明 变量命名规则

## 注意项

### 命名规则

1. 变量名称必须由数字、字母、下划线和$组成

2. 注意：标识符开头不能是数字

3. 标识符不能是保留字和关键字

4. 变量的名字是区分大小写的，如：`age`和`Age`是不同的变量。

5. **常量**：`final`和`const`修饰符（**永远不改变的量**）

   - `const`值不变，定义时赋值

   - `final`定义时可以不赋值，但只能赋值一次，`final`具有`const`的编译时常量的特性，最重要的是它是运行时常量，并且final时惰性初始化，即在运行时第一次使用前才初始化。

     ```dart
       const a = new DateTime.now();      //失败
       final b = new DateTime.now();      //成功
     ```

6. 

## 配置注意项

## 细节点

#### 字符串的拼接

```dart
  String str6 = '你好';
  String str7 = 'Dart';
  print(str6 + str7);      //你好Dart
  print("$str6 $str7");    //你好 Dart
```

#### 定义List

```dart
  // var List4 = new List();    //已经废弃
  var List4 = List.filled(6, ""); //创建一个固定长度的集合，无法通过add增加数据，但是可以修改数据
  var List5 = List<String>.filled(6, "");
  print(List4);  //[, , , , , ]
```

#### 自增与自减

```dart
  var b = a++; //先赋值再运算
  var c = ++a; //先运算再赋值
```

#### List翻转

```dart
List list1 = ['张三', '李四', '王五'];
print(list1.reversed);    //(王五, 李四, 张三)
print(list1.reversed.toList());    //[王五, 李四, 张三]
```









