package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 */
class singleton private (val color:String) {
   println("Creating"+this)
  override  def toString():String="mark color" +color
}

object singleton{
  private val marks = Map(
    "red" -> new singleton("red"),
    "blue" -> new singleton("blue"),
    "green" -> new singleton("green")
  )
  def PrimaryColor="red,green,blue"
  def apply(color:String)=if(marks.contains(color)) marks(color) else null

  def getMark(color: String) = if (marks.contains(color)) marks(color) else null
  def main(args: Array[String]) {
    /*
    println(singleton.getMark("blue"))
    println(singleton getMark "blue")
    println(singleton getMark "red")
    println(singleton getMark "red")
    println(singleton getMark "green")
    */
    println("Primary colors are:" +singleton.PrimaryColor)
    println(singleton("blue"))
    println(singleton("red"))
  }

}