package automobiles

/**
 * Created by liutizhong on 2015/9/28.
 */
class Vehicle(val id:Int,val year:Int){
   override  def toString():String="ID:" +id +" Year:" +year
   protected  def checkEngine(){}
}
class  Car(override val id:Int,override val year:Int,var fuelLevel:Int) extends  Vehicle(id,year){
  def start(): Unit ={
    checkEngine();
  }
  def tow(car:Car): Unit ={
    car.checkEngine()
  }
  def tow(vehicle:Vehicle): Unit ={
    //vehicle.checkEngine()
  }
  override def  toString() :String =super.toString()+"  Fuel Level:" + fuelLevel
}
class CasStation{
  def fillCas(vehicle: Vehicle): Unit ={

  }
}

object carDemo{
  def main(args: Array[String]) {
    val car=new Car(1,2015,100)
    println(car)
  }
}