package PottenMatching

/**
 * Created by liutizhong on 2015/10/1.
 */
object DayOfWeek extends Enumeration {
  val SUNDAT = Value("Sunday")
  val MONDAY = Value("Monday")
  val TUESDAY = Value("Tuesday")
  val WEDNESDAY = Value("Wednesday")
  val THURSDAY = Value("Thursday")
  val FRIDAY = Value("Friday")
  val SATURDAY = Value("Saturday")

  def activity(day: DayOfWeek.Value): Unit = {
    day match {
      case DayOfWeek.SUNDAT=> println("Eat sleep ,repeat ...")
      case DayOfWeek.SATURDAY => println("Hangout with friends...")
      case _ => println("...code for fun")
    }
  }

  def main(args: Array[String]) {
    activity(DayOfWeek.SATURDAY)
    activity(DayOfWeek.MONDAY)
  }

}

