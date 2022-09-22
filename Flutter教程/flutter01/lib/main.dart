import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(
        title: const Text('你好，flutter'),
      ),
      body: const myapp(),
    ),
  ));
}

class myapp extends StatelessWidget {
  const myapp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return const Center(
      child: Text(
        'Hello world',
        textDirection: TextDirection.ltr,
        style: TextStyle(
// color: Colors.lightBlue
            color: Color.fromRGBO(244, 244, 123, 1),
            fontSize: 40),
      ),
    );
    // throw UnimplementedError();
  }
}
