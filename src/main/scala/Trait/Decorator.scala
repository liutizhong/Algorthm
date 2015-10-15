package Trait

/**
 * Created by liutizhong on 2015/9/30.
 */
class Decorator {}
abstract class  Check{
  def check():String ="Checked Application Details..."
}
trait CreditCheck extends Check{
  override def check():String="Checked Credit..." +super.check()
}
trait EmploymentCheck extends Check{
  override def check():String="Check Employment..." +super.check()
}
trait CriminalRecordCheck extends Check{
  override def check():String="Check Criminal Records..."+super.check()
}

object Decorator extends  App{
  /*
   最右面的trait开始调用check(),然后顺着super.check(),将调用传递到其左边的trait.最左边的trait
   调用的是真正实例的check()
   */
  val apartmentApplication=new Check with CreditCheck with CriminalRecordCheck
  println(apartmentApplication check)

}