package PottenMatching

/**
 * Created by liutizhong on 2015/10/1.
 */
object MatchTypes  extends  App{
  /**
   * case 的顺序很重要。scala会自上而下的求值
   * @param input
   */
   def process(input:Any): Unit ={
     input match{
       case (a:Int,b:Int) => println("Processing (int,int)...")
       case (a:Double,b:Double) => println("Processing(double,double)....")
       case msg:Int if(msg>10000) =>println("Processing Int>10000")
       case msg:Int =>println("Processing int...")
       case msg:String =>println("Processing String....")
       case _ => println("Can't handle %s...",input)
     }
   }
  process((34.2,-158.3))
  process(0)
  process(100001)
  process(2.2)

}
