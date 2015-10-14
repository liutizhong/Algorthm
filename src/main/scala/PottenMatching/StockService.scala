package PottenMatching

/**
 * Created by liutizhong on 2015/10/2.
 */
object StockService extends  App{
   def process(input:String): Unit ={
     input match {
       case Symbol() =>println("Look up price for valid symbol"+input)

       /**
        *  这里会先应用ReceiveStockPrice提取器，成功的话，会返回一对结果，对一个结果（symbol）进一步应用Symbol提取器验证
        *  我们可以使用后面跟着的@符号的模式变量，在symbol从两个提取器之间传递的过程中把它拦截住        *
        */
       case ReceiveStockPrice(symbol @ Symbol(),price) => printf("Received price %f for symbol %s\n",price,symbol)
       case _ => println("Invalid input "+input)
     }
   }
  StockService.process("Good")
  StockService.process("Good:310.84")
  StockService.process("Good:Buy")
  StockService.process("IBM")
  StockService.process("ERR:12.21")

}
object Symbol{
  /**
   * unapply() 将对象分解为用以匹配模式的片段，而apply则是为提供一个把他们组合回去的选择
   * @param symbol
   * @return
   */
  def unapply(symbol:String):Boolean=symbol=="Good" || symbol =="IBM"
}
object  ReceiveStockPrice{
  def unapply(input:String):Option[(String,Double)]={
    try{
      if(input contains(":")){
        val splitQuote=input split(":")
        Some(splitQuote(0),splitQuote(1).toDouble)
      }
      else{
        None
      }
    }catch {
      case _ :NumberFormatException => None
    }
  }
}