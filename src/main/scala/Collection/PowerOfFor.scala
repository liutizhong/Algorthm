package Collection

/**
 * Created by liutizhong on 2015/9/30.
 */
object Person extends App {
  def apply(firstName: String, lastname: String): Person = new Person(firstName, lastname)
  val friends=List(Person("Brian","Sletten"),Person("Neal","Fold"),Person("Stuart","Halloway"))
  val lastName=for(friend <- friends;lastName=friend.lastName)
    yield lastName

  println(lastName.mkString(","))
  val result = for (i <- 1 to 10)
    yield i * 2
  val result2 = (1 to 10).map(_ * 2)

  val doubleEven = for (i <- 1 to 10; if i % 2 == 0)
    yield i * 2

  for {
    i <- 1 to 10
    if i % 2 == 0
  }
    yield i * 2

  for (i <- 1 to 3;j <- 4 to 5){
    println("["+i+","+j+"]")
  }
}

class Person(val firstName: String, val lastName: String)

