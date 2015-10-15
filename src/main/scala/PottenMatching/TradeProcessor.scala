package PottenMatching

/**
 * Created by liutizhong on 2015/10/1.
 */
/*
class TradeProcessor {
 def processTransaction(request:Trade): Unit ={
   request match {
     case Sell(stock,1000) => println("Selling 1000-untils of "+stock)
     case Sell(stock,quantity) => printf("Selling %d units of %s\n",quantity,stock)
     case Buy(stock,quantity) if(quantity>2000) => printf("Buying %d (large) units of %s\n",quantity,stock)
     case Buy(stock,quantity) => printf("Buying %d units of %s\n",quantity,stock)
     }
 }

}

object TradeProcessor extends App{
  val tradeProcessor=new TradeProcessor
  tradeProcessor.processTransaction(Sell("Good",500))
  tradeProcessor.processTransaction(Buy("good",700))
  tradeProcessor.processTransaction(Sell("good",1000))
  tradeProcessor.processTransaction(Buy("good",3000))
}

sealed abstract case class Trade()
case class  Sell(stockSymbol:String,quantity:Int) extends Trade
case class  Buy(stockSymbol:String,quantity:Int) extends  Trade
case class  Hedge(stockSymbol:String,quantity:Int) extends Trade
*/