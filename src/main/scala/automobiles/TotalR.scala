package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 */
object TotalR {
  def main(args: Array[String]) {
     //println(totalResultOverRange(11,i => i))
   // println(totalResultOverRange(11,i=>if(i%2==0) 1 else 0))
    //println(totalResultOverRange(11,i=>if(i%2!=0) 1 else 0))
   // val array=Array(2,3,5,1,6,4)
   // val sum=inject(array,0,(carryOver,elem)=>carryOver + elem)
   // println("Sum of element in array"+ array.toString() + " is "+ sum)

   // val max=inject(array,Integer.MIN_VALUE,(carryOver,elem)=>Math.max(carryOver,elem))
   // println("Max of elements in array"+array.toString()+"is"+max)
    val array=Array(2,3,5,1,6,4)
    val sum=(0 /: array){(sum,elem)=>sum+elem}
    val max=(Integer.MIN_VALUE /: array){
      (large,elem)=> Math.max(large,elem)
    }
    println("Max of elements in array"+array.toString()+"is"+max)
    println("Sum of element in array"+ array.toString() + " is "+ sum)
  }

  def totalResultOverRange(number:Int,codeBlock:Int=> Int):Int={
    var result=0
    for(i<- 1 to number){
      result +=codeBlock(i)
    }
    result
  }
  def inject(arr:Array[Int],initial:Int,operation:(Int,Int)=>Int):Int={
    var carryOver=initial
    arr.foreach(element => carryOver=operation(carryOver,element))
    carryOver
  }


}
