package automobiles

/**
 * Created by liutizhong on 2015/9/28.
 */
class CarDemo(val year:Int) {
   private var milesDriven:Int =0
   def miles()=milesDriven
   def drive(distance:Int): Unit ={
     milesDriven +=Math.abs(distance)
   }
}
object  test{
  def main(args: Array[String]) {
    val car=new CarDemo(2009)
    println("Car made in year" + car.year)
    println("Miles driven" + car.miles())
    println("Drive for 10 miles")
    car.drive(10)
    print("Miles driven"+car.miles())
  }
}
