package automobiles

/**
 * Created by liutizhong on 2015/9/29.
 */
class Resource private() {
    println("Starting transaction...")
    private  def clearup(){println("Ending transaction...")}

    def op1= println("Operation 1")
    def op2= println("Operation 2")
    def op3= println("Operation 3")
}
object Resource{
  def use(codeBlock:Resource=>Unit): Unit ={
    val resouce=new Resource
    try{
      codeBlock(resouce)
    }
    finally{
      resouce.clearup()
    }
  }

  def main(args: Array[String]) {
    Resource.use{
      resource =>
        resource.op1
        resource.op2
        resource.op3
        resource.op1
    }
  }
}
