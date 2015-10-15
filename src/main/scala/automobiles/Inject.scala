package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 */
object Inject {
   def inject(arr:Array[Int],Initial:Int)(operation:(Int,Int)=>Int):Int={
     var carryOver=Initial
     arr.foreach(element=>carryOver=operation(carryOver,element))
     carryOver
   }

  def main(args: Array[String]) {
    val array=Array(2,3,5,1,6,4)
    val sum=inject(array,0){(carryOver,element)=>carryOver+element}
    println("Sum of element in array "+ array.toString()+ " is " +sum)
  }
}
