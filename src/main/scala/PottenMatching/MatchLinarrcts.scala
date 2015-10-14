package PottenMatching

/**
 * Created by liutizhong on 2015/9/30.
 */
object MatchLinarrcts extends  App{
    def active(day : String): Unit ={
      day match {
        case "Sunday" => println("eat ,sleep,repeat ....")
        case "Saturday" => println("Hangout with friends....")
        case "Monday" => println("...code for fun...")
      }
    }

  /**
   * match 是一个对Any 起作用的表达式，在用他处理String时，他会对目标执行模式匹配，根据匹配模式的值调用合适的case表达式
   */
  List("Monday","Sunday","Saturday").foreach(active)
}
