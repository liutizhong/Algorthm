package Trait

/**
 * Created by liutizhong on 2015/9/29.
 */
class Human(val name: String) extends Friend {
  //def listen()=println("Your friend " +name + "is listening")
}

class Man(override val name: String) extends Human(name)

class Woman(override val name: String) extends Human(name)

class Cat(val name:String)extends  Animal

trait Friend {
  val name: String

  def listen() = println("Your friend " + name + " is listening")
}

class Animal

class Dog(val name: String) extends Animal with Friend {
  override def listen = println(name + "'s listening quietly")
}

object useFridend extends App {
  val john = new Man("John")
  john.listen()
  val sara = new Woman("sara")
  sara.listen()
  val comet = new Dog("Comet")
  comet.listen

  val mansBestFriend:Friend=comet
  mansBestFriend.listen()

  def helpAsFriend(friend: Friend)=friend listen

  helpAsFriend(sara)
  helpAsFriend(comet)

  def userFriends(friend: Friend)=friend listen

  val snowy=new Cat("Snowy") with Friend
  val friend:Friend=snowy
  friend.listen()

  userFriends(snowy)
}


