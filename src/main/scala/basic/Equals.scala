package basic

/**
 * Created by liutizhong on 2015/9/28.
 */
object Equals {
  def main(args: Array[String]) {
    val str1="hello"
    val str2="hello"
    val str3=new String("hello")

    println(str1 == str2)
    println(str1 eq str2)
    println(str1 == str3)
    println(str1 eq str3)
    val microwave=new Micriware
    microwave.start()
    //microwave.turnTable()
  }
}
class Micriware{
  def start()=println("started")
  def stop()=println("stopped")
  private def turnTable()=println("turning table")
}

