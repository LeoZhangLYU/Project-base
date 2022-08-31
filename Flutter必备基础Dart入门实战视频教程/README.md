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

   - `final`定义时可以不赋值，但只能赋值一次，`final`具有`const`的编译时常量的特性，最重要的是它是运行时常量，并且`final`是惰性初始化，即在运行时第一次使用前才初始化。

     ```dart
       const a = new DateTime.now();      //失败
       final b = new DateTime.now();      //成功
     ```

### 抽象类

`Dart`抽象类主要用于定义标准，子类可以继承抽象类，也可以实现抽象类接口

1. 抽象类通过`abstract`关键字来定义
2. `Dart`中的抽象方法不能用`abstract`声明，`Dart`中没有方法体的方法我们称为抽象方法。
3. 如果子类继承抽象类必须要实现里面的抽象方法
4. 如果把抽象类当作接口实现的话必须要实现抽象类里面定义的所有属性和方法。
5. 抽象类不能被实例化，只有继承它的子类可以

`extends`抽象类和`implements`的区别：

1. 如果要复用抽象类里面的方法，并且要用抽象方法约束子类的话我们就用`extents`继承抽象类
2. 如果只是把抽象类当作标准的话我们就用impls实现抽象类

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

##### List

###### 哈哈











