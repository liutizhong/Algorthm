package automobiles
import java.util.Date

/**
 * Created by liutizhong on 2015/9/29. *
 * pian han shu
 */
object log {
  def log(date:Date,message:String): Unit ={
    println(date + "-----" + message)
  }
  def main(args: Array[String]) {
    val logWithDateBound=log(new Date, _:String)
    logWithDateBound("message1")
    logWithDateBound("message2")
    logWithDateBound("message3")
    logWithDateBound("message4")
  }
}
