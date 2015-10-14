package PottenMatching

/**
 * Created by liutizhong on 2015/10/1.
 */
class Sample {
  /**
   * Scala中模式变量要以小写字母开头，常量要以大写字母开头
   */
   val max=100
  val MIN=0
  def process(input:Int): Unit ={
    input match {
      case this.max => println("Your matched max")
      case MIN => println("Your matched min")
      case _ => println("Unmatched")
    }
  }
}
object  Sample extends  App{
  new Sample().process(100)
  new Sample().process(0)
  new Sample().process(10)
}
