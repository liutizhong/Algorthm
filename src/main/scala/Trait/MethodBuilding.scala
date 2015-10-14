package Trait

import java.io.StringWriter

/**
 * Created by liutizhong on 2015/9/30.
 */
class MethodBuilding {

}
abstract  class Writer{
  def writeMessage(message:String)
}
trait  UpperCaseWriter extends Writer{
  abstract  override  def writeMessage(message:String)=
    super.writeMessage(message.toUpperCase)
}
trait ProfanityFilteredWriter extends Writer{
  abstract override def writeMessage(message:String)=
     super.writeMessage(message.replace("stupid","s------"))
}
class StringWriterDelegate extends Writer{
  val writer=new StringWriter()
  def writeMessage(message:String)=writer.write(message)
  override  def toString():String=writer.toString
}
object MethodBuilding extends  App{
  /**
   * 在第一语句中，ProfanityFilteredWriter是最右的trait，所以他会先起作用。
   * 在第二个语句中，他会后起作用
   */
  val myWriterProfanityFirst=
    new StringWriterDelegate with  UpperCaseWriter with  ProfanityFilteredWriter
  val myWriterProfanityLast=
    new StringWriterDelegate with ProfanityFilteredWriter with  UpperCaseWriter
  myWriterProfanityFirst writeMessage "There is no sin except stupidity"
  myWriterProfanityLast writeMessage "There is no sin except stupidity"
  println(myWriterProfanityFirst)
  println(myWriterProfanityLast)
}