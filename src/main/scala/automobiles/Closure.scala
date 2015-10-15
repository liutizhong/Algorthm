package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 * 闭包：
 * 创建有未绑定变量的代码块，调用函数前必须绑定他们，不过，他们可以在局部范围和
 * 参数列表之外绑定变量
 */
object Closure extends App{
   def loopThrough(number: Int)(closure: Int=>Unit): Unit ={
     for(i <- 1 to number){
       closure(i)
     }
   }
  //定义的loopThrough函数的第一个参数
  var result=0
  //定义的loopThrough函数的第二个参数  代码块
  val addIt={value:Int=>result +=value}

  loopThrough(10){addIt}
  println("Total of values from 1 to 10 is "+result)

  result=0
  loopThrough(5){addIt}
  println("Total of values from 1 to 5 is " + result)
  var produce =1
  loopThrough(5){produce *= _}
  println("Product of values from 1 to 5 is "+produce)
}
