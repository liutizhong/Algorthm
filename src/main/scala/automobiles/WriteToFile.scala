package automobiles
import java.io._
/**
 * Created by liutizhong on 2015/9/29.
 */
/*
class WriteToFile {

}
*/
object WriteToFile{
  def wriTofile(fileName:String)(codeBlock:PrintWriter=>Unit)={
    val writer=new PrintWriter(new File(fileName))
    try{
      codeBlock(writer)
    }
    finally{
      writer.close()
    }
  }
  def main(args: Array[String]) {
    wriTofile("output.txt"){writer =>
    writer write "hell from scala world"
    }
  }
}
