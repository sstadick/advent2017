import scala.io.Source
import scala.collection.mutable.ArrayBuffer

val input_file = "./inputs/advent2_1.txt"

val diffs = ArrayBuffer[Int]()

for (line <- Source.fromFile(input_file).getLines) {
  val values = line.split(" ")
  val val_ins = values.map(_.toInt)
  diffs += (val_ins.max - val_ins.min)
}

println(diffs.sum)
