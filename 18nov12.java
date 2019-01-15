class Dog{
  //멤버변수
  String name;
  String color;
  int age;
  //멤버메소드
  void eat{
    System.out.println('강아지가먹는다.')
  }
  void run{
    //달리는액션
  }

}
  //시간이 흐르는 리억월드
public static void main(String[] args){
  Dog tom = new Dog();
  tom.color = "하얀색";
  tom.eat();
  tom.run();

  Person boby = new Person();
  boby.eat();
  boby.run();
}
