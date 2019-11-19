import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'dart:convert';
import 'dart:async';
import 'package:http/http.dart' as http;

class HomePage extends StatefulWidget {
  @override
  static String tag = 'home-page';
  State<StatefulWidget> createState() {
    return _State();
  }
}

class _State extends State<HomePage> {
  var _userController = TextEditingController();
  var _passwordController = TextEditingController();
  var _text = '';
  static String tag = 'home-page';

  Future<String> getData2() async {
    //var story = myController.text;
    var response = await http.post(
        Uri.encodeFull("http://127.0.0.1:5000/api2"),
        body: {"data": _userController.text}
    );
    print(_userController.text);
    print('&&&');
    setState((){
      _text = jsonDecode(response.body)['hotel_name'];
    });
    _text = jsonDecode(response.body)['hotel_name'];
    print(_text);
    return (jsonDecode(response.body)['hotel_name']);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Magical Trip Advisor'),
      ),
      body: Container(
        padding: EdgeInsets.all(32.0),
        child: Column(
          children: <Widget>[

            Row(
              children: <Widget>[
                Expanded(
                  flex: 3,
                  child: Text('Input your dream resort: '),
                ),
                Expanded(
                  flex: 7,
                  child: TextField(
                    controller: _userController,
                  ),
                ),
              ],
            ),

            Container(
              padding: EdgeInsets.all(16.0),
              child: RaisedButton(
                child: Text('Submit'),
                onPressed: getData2,
              ),
            ),
            Container(
              padding: EdgeInsets.all(8.0),
              child: Text(_text),
            )
          ],
        ),
      ),
    );
  }
}


//class HomePage extends StatelessWidget {
//  static String tag = 'home-page';
//
//  @override
//  Widget build(BuildContext context) {
//    final alucard = Hero(
//      tag: 'hero',
//      child: Padding(
//        padding: EdgeInsets.all(16.0),
//        child: CircleAvatar(
//          radius: 72.0,
//          backgroundColor: Colors.transparent,
//          backgroundImage: AssetImage('assets/alucard.jpg'),
//        ),
//      ),
//    );
//
//    final welcome = Padding(
//      padding: EdgeInsets.all(8.0),
//      child: Text(
//        'Welcome Alucard',
//        style: TextStyle(fontSize: 28.0, color: Colors.white),
//      ),
//    );
//
//    final lorem = Padding(
//      padding: EdgeInsets.all(8.0),
//      child: Text(
//        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec hendrerit condimentum mauris id tempor. Praesent eu commodo lacus. Praesent eget mi sed libero eleifend tempor. Sed at fringilla ipsum. Duis malesuada feugiat urna vitae convallis. Aliquam eu libero arcu.',
//        style: TextStyle(fontSize: 16.0, color: Colors.white),
//      ),
//    );
//
//    final body = Container(
//      width: MediaQuery.of(context).size.width,
//      padding: EdgeInsets.all(28.0),
//      decoration: BoxDecoration(
//        gradient: LinearGradient(colors: [
//          Colors.blue,
//          Colors.lightBlueAccent,
//        ]),
//      ),
//      child: Column(
//        children: <Widget>[alucard, welcome, lorem],
//      ),
//    );
//
//    return Scaffold(
//      body: body,
//    );
//  }
//}
