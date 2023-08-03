from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
import getopt
spark = SparkSession.builder.appName("App com parametros").getOrCreate()

if __name__:
    
    opts,args = getopt.getopt(sys.argv[0:],"o:d")
    for opt in opts:
        print(opt)


spark.stop()