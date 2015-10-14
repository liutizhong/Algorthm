package PottenMatching

/**
 * Created by liutizhong on 2015/10/1.
 */
object MatchTuples extends App{
   def processCoordinates(input:Any): Unit ={
     input match {
       case (a,b) => printf("Processing (%d,%d)...",a,b)
       case "done" => println("done")
       case _=> null
     }
   }
  processCoordinates((39,-104))
  processCoordinates("done")

  def processItems(items:List[String]): Unit ={
    items match {
      case List("apple","ibm")=> println("apple and IBMs")
      case List("red","blue","while") => println("Stars and Stripes")
      case List("red","blue",_*) => println("color red ,blue,....")
      //如果需要引用余下的匹配项，可以在特殊符号@前放置一个变量如otherFruits
      case List("apple","orange",otherFruits @ _*) => println("apples,oranges,and "+otherFruits)
    }
  }

  processItems(List("apple","ibm"))
  processItems(List("red","blue","green"))
  processItems(List("red","blue","while"))
  processItems(List("apple","orange","grapes","dates"))

}
