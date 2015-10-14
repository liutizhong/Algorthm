package Collection

/**
 * Created by liutizhong on 2015/9/30.
 */
class UsingSet {

}
object  UsingSet extends App{
  val color1=Set("blue","Green","Red")
  var colors=color1
  println("colors1(colors)"+colors)

  colors +="Black"
  println("colors:"+colors)
  println("colors1:"+color1)

  val feeds1=Set("blog.toolshed.com","pragdave.pragprog.com","pragmacitc-osxer.blogspot.com","vita-contemplativa.blogspot.com")
  val feeds2=Set("blog.toolshed.com","martinfowler.com/bliki")

  val blogSpotFeeds= feeds1 filter (_ contains "blogspot")
  println("blogspot feeds:" + blogSpotFeeds.mkString(","))
  //如果需要将两个set集合合并成一个新的Set，可以使用 ++
  val mergedFeeds=feeds1 ++ feeds2
  println("# of merged feeds:"+ mergedFeeds.size)

  //val commonFeeds= feeds1 ** feeds2
  //println("common feeds:" + commonFeeds.mkString(","))

  val urls= feeds1 map ("http://" + _)
  println("One url:" + urls.toString())

  val feeds =Map("Andy Hunt" -> "blog.toolshed.com","Dave Thomas" ->"pragdave.pragprog.com","Dan steinberg" -> "dimsumthinking.com/blog")

  val filterNameStartWithD=feeds filterKeys(_ startsWith "D")
  println("# of Filtered:" + filterNameStartWithD.size)

  val filterNameStartWithDAndBloginFeed= feeds filter {
    element =>
      val (key,value)=element
      (key startsWith "D") && (value contains "blog")
  }
  println("# of feeds with auth name D* and blog in URL:" +filterNameStartWithDAndBloginFeed.size)
  //val newFeeds1=feeds.update("Venkat Subraamaniam","agiledeveloper.com/blog")

  // println("Venkat's blog in original feeds: " +feeds.get("VenKat Subramaniam") )

  //println("Venkat's blog in new feeds:" + newFeeds1.get("Venkat Subramaniam"))


  val list=List("blog.toolshed.com","pragdave.pragprog.com","pragmacitc-osxer.blogspot.com","vita-contemplativa.blogspot.com")
  val prefixedList="forums.pragprog.com/forums/87" :: list

  println("First feed: "+list.head)
  println("Second feed: " + list(1))

  val listwithForums=list ::: prefixedList

  println("First listwithForums: "+listwithForums.head)
  println("First listwithForums: "+listwithForums.last)
  println("First listwithForums: "+listwithForums.filter(_ contains "blog").mkString(","))
  println("All feeds have com:" +listwithForums.forall(_ contains("com")))
  println("All feeds have dave:" +listwithForums.forall(_ contains("dave")))
  println("Any feed has dave :" +listwithForums.exists(_ contains("dave")))
  println("Any feed has bill :"+listwithForums.exists(_ contains("bill")))
  println("Feed url lengths:"+listwithForums.map(_.length).mkString(","))

  val total=listwithForums.foldLeft(0){
    (total,feed) => total +feed.length
  }
  println("Total length of feed urls:" + total)

  val total2=(0 /: listwithForums){
    (totals,lists)=> totals + lists.length
  }
  println("Total length of feed urls :" +total2)

  val total3=(0 /: listwithForums){_+_.length}
  println("Total lenght of feed urls:" + total3)

}