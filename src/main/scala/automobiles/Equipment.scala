package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 */
class Equipment(val routine:Int=>Int) {
  def simulate(input:Int)={
    println("Running simulation...")
    routine(input)
  }

}
object EquipmentUserNotDry{
  def main(args: Array[String]) {
   // val equipment1=new Equipment({input=>println("calc with: "+input);input})
   // val equipment2=new Equipment({input=>println("calc with: "+input);input})
   // equipment1.simulate(4)
   // equipment2.simulate(6)
    val arr=Array(1,2,3,4,5)
    println("Sum of all values in array is "+ (0 /: arr){(sum,elem)=>sum+elem})
    println("Sum of all values in array is " + (0 /: arr){_+_})
    val negative=arr.exists{ _ < 0}
    println("Array has negative number?"+negative)
    var max=(Integer.MIN_VALUE /: arr){ (large,elem) => max2(large,elem)}
    max=(Integer.MIN_VALUE /: arr){max2(_,_)}

    val  max1=(Integer.MIN_VALUE /: arr){max2 _}
    val  max3=(Integer.MIN_VALUE /: arr){max2}
    println("max "+max)
    println("max1 "+max1)
    println("max3 "+max3)
  }
  def max2(a:Int,b:Int):Int=if(a>b) a else b




}
