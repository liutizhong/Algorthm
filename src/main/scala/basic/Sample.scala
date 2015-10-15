package basic

/**
 * Created by liutizhong on 2015/9/28.
 */
object Sample {
   def main (args: Array[String]) {
     println("hello scala")
     for (i <-1 to 3){
       print(i+",")
     }
     println();
     for(i <- 1 until 3){
       println(i+",")
     }
     (1 to 3).foreach(i => print(i +","))
     println("scala rocks")
     val(firstname,lastname,emailAddress)=getPersonInfo(1)
     println("First Name is  " + firstname)
     println("last Name is  " + lastname)
     println("email Address is  " +emailAddress)
  }
  def getPersonInfo(primaryKey: Int)={
    ("liu","tizhong","liutizhong@163.com")
  }


}
