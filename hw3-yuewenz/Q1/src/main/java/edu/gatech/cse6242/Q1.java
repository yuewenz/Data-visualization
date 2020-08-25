package edu.gatech.cse6242;

import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class Q1 {
/* TODO: Update variable below with your gtid */
  final String gtid = "yzheng420";
  public static class TokenizerMapper extends Mapper<Object, Text, Text, Text>{
    private Text word= new Text();
    private Text lines= new Text();
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
     String[] texts = value.toString().split(",");
     String pickupid= texts[0].toString();
     String distances= texts[2].toString();
    //reference by https://beginnersbook.com/2013/12/how-to-convert-string-to-double-in-java/
     double distance=Double.parseDouble(distances);
     String fares= texts[3].toString();
     double fare=Double.parseDouble(fares);
     Integer first = 1;
     if (distance != 0 && fare >0) {
       word.set(pickupid);
       //System.out.println(word);
       lines.set(first+","+fare);
       context.write(word, lines);
       //System.out.println(word);
}
}
}

  public static class Sum extends Reducer<Text, Text, Text, Text> {
    private Text total= new Text();
    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
      int sum = 0;
      double faresum = 0;
      for (Text val : values) {
         String[] idnum=val.toString().split(",");
         double idnums=Double.parseDouble(idnum[0]);
         int n =(int) idnums;
         sum += (n);
         double totalfare=Double.parseDouble(idnum[1]);
         faresum+= (totalfare);
         
         
         
}
//reference by https://www.admfactory.com/display-double-in-2-decimal-points-in-java/
String fare_two=String.format("%(,.2f",faresum);

total.set(sum+","+fare_two);
context.write(key, total);
}
}

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Q1");

    /* TODO: Needs to be implemented */
    job.setJarByClass(Q1.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setReducerClass(Sum.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
