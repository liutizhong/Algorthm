package Trait
import java.util._
/**
 * Created by liutizhong on 2015/9/30.
 */
class DateHelper(number:Int) {
  /*
    def days(when:String):Date={
      val date=Calendar.getInstance()


      when match {

        case DateHelper.ago => date.add(Calendar.DAY_OF_MONTH,number)
        case DateHelper.form_now => date.add(Calendar.DAY_OF_MONTH,number)
        case _ => date

      }
    }
     */
}
object DateHelper{
  val ago="ago"
  val form_now="form_now"
  implicit  def convertInt2DateHelp(number:Int)=new DateHelper(number)
}