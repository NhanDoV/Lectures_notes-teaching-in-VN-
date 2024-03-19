import pyspark
import findspark
from pyspark.sql import functions as sf
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql.window import Window
from pyspark.sql.functions import col, \
                                    substring, lit, concat, \
                                    sin, exp, \
                                    datediff, months_between, \
                                    date_format, to_date, to_timestamp, date_add, date_sub, hour, date_trunc

#===========================================================================================================
def pre_process_string_sparkdf(sparkdf, input_col, output_col, n_substrings):
    """
        Trích xuất một số phần tử đầu / cuối, ghép nối
        ===========
        Example
        >> !wget https://jacobceles.github.io/knowledge_repo/colab_and_pyspark/cars.csv
        >> df = spark.read.csv('cars.csv', header=True, sep=";")        
        >> ndf = pre_process_string_sparkdf(df, 'Car', 'first_4_letter', 4)
        >> ndf.show(5)
            +--------------------+----------+----------+--------------+---------------+
            |                 Car|4st_letter|4ls_letter|2nd-5th_letter|concat(4ls-4st)|
            +--------------------+----------+----------+--------------+---------------+
            |Chevrolet Chevell...|      Chev|      libu|          hevr|      Chev-libu|
            |   Buick Skylark 320|      Buic|       320|          uick|      Buic- 320|
            |  Plymouth Satellite|      Plym|      lite|          lymo|      Plym-lite|
            |       AMC Rebel SST|      AMC |       SST|          MC R|      AMC - SST|
            |         Ford Torino|      Ford|      rino|          ord |      Ford-rino|
            +--------------------+----------+----------+--------------+---------------+
            only showing top 5 rows
    """
    sparkdf = sparkdf.select(col(input_col),
                             substring(col(input_col), 1, n_substrings).alias(output_col))
    sparkdf = sparkdf.select(col(input_col), col(output_col),
                             substring(col(input_col), -4, n_substrings).alias('4ls_letter'))
    sparkdf = sparkdf.select(col(input_col), col(output_col), col('4ls_letter'),
                             substring(col(input_col), 2, n_substrings).alias('2nd-5th_letter'))
    sparkdf = sparkdf.select(col(input_col), col(output_col), 
                             col('4ls_letter'), col('2nd-5th_letter'),
                             concat(col(output_col), lit("-"), col('4ls_letter')).alias('concat(4ls-4st)'))
    
    return sparkdf

#===========================================================================================================
def numeric_preprocess(sparkdf, col1, col2, col3, col4):
    """
        Một số xử lý cơ bản như +-*/
        ===============================
        Example
        >> !wget https://jacobceles.github.io/knowledge_repo/colab_and_pyspark/cars.csv
        >> df = spark.read.csv('cars.csv', header=True, sep=";")
        >> ndf = numeric_preprocess(df, 'MPG', 'Cylinders', 'Weight', 'Acceleration')
        >> ndf.show(5)
            +----+------+---------+------------+-----------------------+------------------+
            | MPG|Weight|Cylinders|Acceleration|(weight*mpg+3)/cylinder| exp(acceleration)|
            +----+------+---------+------------+-----------------------+------------------+
            |18.0| 3504.|        8|        12.0|               7884.375|162754.79141900392|
            |15.0| 3693.|        8|        11.5|                6924.75|  98715.7710107605|
            |18.0| 3436.|        8|        11.0|               7731.375| 59874.14171519782|
            |16.0| 3433.|        8|        12.0|               6866.375|162754.79141900392|
            |17.0| 3449.|        8|        10.5|                 7329.5|36315.502674246636|
            +----+------+---------+------------+-----------------------+------------------+
            only showing top 5 rows        
    """
    sparkdf = sparkdf.select(col(col1), col(col3), col(col2), col(col4),
                             ((col(col1)*col(col3)+lit(3))/col(col2)).alias('(weight*mpg+3)/cylinder'),
                             (exp(col(col4))).alias('exp(acceleration)')
                            )

    return sparkdf 

#===========================================================================================================
def preprocess_timestamp(sparkdf, date_col):
    """
        Một số xử lý cơ bản về date-time trong Sparks như
        - trích xuất một số phần tử ngày / tháng / giờ
        - tìm số ngày đến thời điểm nào đó
        - tìm ngày trước và ngày sau tại một thời điểm
        ======================
        Example
        >> Mdf = spark.createDataFrame([['2019-08-25 13:30:00'], 
                                        ['2023-10-06 05:12:11'],
                                        ['2022-04-01 00:00:00'], 
                                        ['2024-03-18 20:10:12']], ['DOB'])
        >> Mdf = preprocess_timestamp(Mdf, 'DOB')
        >> Mdf.show()
            +-------------------+------------+---------+--------------+----+---------+-----------+----------+-----------+
            |                DOB|current_date|get_month|get_month_name|hour|diff_days|diff_months|3day.later|3day.before|
            +-------------------+------------+---------+--------------+----+---------+-----------+----------+-----------+
            |2019-08-25 13:30:00|  2024-03-19|       08|        August|  13|     1668|54.78830645|2019-08-28| 2019-08-22|
            |2023-10-06 05:12:11|  2024-03-19|       10|       October|  05|      165| 5.41236148|2023-10-09| 2023-10-03|
            |2022-04-01 00:00:00|  2024-03-19|       04|         April|  00|      718|23.58064516|2022-04-04| 2022-03-29|
            |2024-03-18 20:10:12|  2024-03-19|       03|         March|  20|        1| 0.00514785|2024-03-21| 2024-03-15|
            +-------------------+------------+---------+--------------+----+---------+-----------+----------+-----------+
    """
    # adding new column with the constant-values '2024-03-19'
    sparkdf = sparkdf.withColumn('current_date', lit('2024-03-19'))
    
    # datetime-processing
    sparkdf = sparkdf.select(col(date_col), col('current_date'),
                     date_format(to_date(col(date_col)), 'MM').alias('get_month'),
                     date_format(to_date(col(date_col)), 'MMMM').alias('get_month_name'),
                     date_format(to_timestamp(col(date_col)), 'HH').alias('hour'),
                     datediff(col('current_date'), to_timestamp(col(date_col))).alias('diff_days'),
                     months_between(col('current_date'), to_timestamp(col(date_col))).alias('diff_months'),                             
                     date_add(to_date(col(date_col)), 3).alias('3day.later'),
                     date_add(to_date(col(date_col)), -3).alias('3day.before'),  # you can also used day_sub(col, 3)               
                    )
    return sparkdf

def spark_query_sql(sparkdf, table_name, query):
    """
        Thực hiện một SQL query từ một table với sparks
        ==========================
        Example
        >> !wget https://jacobceles.github.io/knowledge_repo/colab_and_pyspark/cars.csv
        >> df = spark.read.csv('cars.csv', header=True, sep=";")
        >> ndf = spark_query_sql(df, "car", "select * from car limit 5")
        >> ndf.show()               
            +--------------------+----+---------+------------+----------+------+------------+-----+------+
            |                 Car| MPG|Cylinders|Displacement|Horsepower|Weight|Acceleration|Model|Origin|
            +--------------------+----+---------+------------+----------+------+------------+-----+------+
            |Chevrolet Chevell...|18.0|        8|       307.0|     130.0| 3504.|        12.0|   70|    US|
            |   Buick Skylark 320|15.0|        8|       350.0|     165.0| 3693.|        11.5|   70|    US|
            |  Plymouth Satellite|18.0|        8|       318.0|     150.0| 3436.|        11.0|   70|    US|
            |       AMC Rebel SST|16.0|        8|       304.0|     150.0| 3433.|        12.0|   70|    US|
            |         Ford Torino|17.0|        8|       302.0|     140.0| 3449.|        10.5|   70|    US|
            +--------------------+----+---------+------------+----------+------+------------+-----+------+        
        .................. Với một số query khá dài ta có thể kẹp nó ở giữa 3 ký tự "
        >> q = (3)" select count(*) as total_count, Origin
                 from car 
                 group by Origin
                 order by total_count desc
               "(3)
        >> ndf = spark_query_sql(df, "car", q)
        >> ndf.show()
            +-----------+------+
            |total_count|Origin|
            +-----------+------+
            |        254|    US|
            |         79| Japan|
            |         73|Europe|
            +-----------+------+
    """
    # Register Temporary Table
    sparkdf.createOrReplaceTempView(table_name)
    
    # return
    return spark.sql(query)

# ===========================================================================================

# Read more
#========================== To install Pysparks - JDK and hadoop ===========================
""" 
# innstall java
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

# install spark (change the version number if needed)
!wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz

# unzip the spark file to the current folder
!tar xf spark-3.0.0-bin-hadoop3.2.tgz

# install findspark and pyspark using pip
!pip install -q findspark
!pip install -q pyspark
"""
#============================= Initialize the SparkSession =================================
"""
# Initialize findspark
findspark.init()

# Initialize the Spark-Session
spark = SparkSession.builder.master("local[*]").getOrCreate()

# Change App-name
spark.sparkContext.appName = "nhan"

# Property used to format output tables better
conf = SparkConf().setAppName('nhan').set("spark.driver.memory", "4g")\
                                       .set("spark.executor.memory", "12g")\
                                       .set('spark.driver.cores', '5')\
                                       .set('spark.dynamicAllocation.enabled', 'true')\
                                       .set('spark.executor.instances', '0')\
                                       .set('spark.dynamicAllocation.initialExecutors', '0')\
                                       .set('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar')
spark = SparkSession.builder.config(conf=conf).getOrCreate()
"""

#==================================== Basic properties ===========================================
# df = spark.read.csv('cars.csv', header=True, sep=";")
# df.show(5)
#================================ you will receive the output like this ==========================
"""
with using : !wget https://jacobceles.github.io/knowledge_repo/colab_and_pyspark/cars.csv
and the df.show(5) throws
....................
Result:

    +--------------------+----+---------+------------+----------+------+------------+-----+------+
    |                 Car| MPG|Cylinders|Displacement|Horsepower|Weight|Acceleration|Model|Origin|
    +--------------------+----+---------+------------+----------+------+------------+-----+------+
    |Chevrolet Chevell...|18.0|        8|       307.0|     130.0| 3504.|        12.0|   70|    US|
    |   Buick Skylark 320|15.0|        8|       350.0|     165.0| 3693.|        11.5|   70|    US|
    |  Plymouth Satellite|18.0|        8|       318.0|     150.0| 3436.|        11.0|   70|    US|
    |       AMC Rebel SST|16.0|        8|       304.0|     150.0| 3433.|        12.0|   70|    US|
    |         Ford Torino|17.0|        8|       302.0|     140.0| 3449.|        10.5|   70|    US|
    +--------------------+----+---------+------------+----------+------+------------+-----+------+
**************************************************************************************************
Explaination
        1.   `df.take(5)` will return a list of five Row objects. 
        2.   `df.collect()` will get all of the data from the entire DataFrame. 
                    Be really careful when using it, because if you have a large data set, 
                    you can easily crash the driver node. 
        3.   `df.show()` is the most commonly used method to view a dataframe. 
                    There are a few parameters we can pass to this method, like the number of rows and truncation. 
                    For example, `df.show(5, False)` or ` df.show(5, truncate=False)` 
                    will show the entire data wihtout any truncation.
        4.   `df.limit(5)` will **return a new DataFrame** by taking the first n rows. 
                    As spark is distributed in nature, there is no guarantee that `df.limit()` will give you 
                    the same results each time.
=====================================================================================================
""" 
#                                                                                                      #
#                                               *************                                          #
#                                ******************************************                            # 
#******************************************************************************************************#
#================================== 1. OPERATIONS ON COLUMNS ==========================================#
#******************************************************************************************************#
#                                ******************************************                            #
#                                               *************                                          #
#                                                                                                      #
#====================================== 1.1 Print all columns =========================================#
# print(df.columns)
#================================================== Output ============================================#
#['Car', 'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model', 'Origin']
#======================================================================================================#

#============================================= Data type ==============================================#
# print(df.dtypes)
#================================================ Output ==============================================#
# [('Car', 'string'), ('MPG', 'string'), ('Cylinders', 'string'), 
#  ('Displacement', 'string'), ('Horsepower', 'string'), ('Weight', 'string'), 
#  ('Acceleration', 'string'), ('Model', 'string'), ('Origin', 'string')]
#======================================================================================================#

#====================================== 1.2 Print out schema ==========================================#
# df.printSchema()
""" you will see
root
 |-- Car: string (nullable = true)
 |-- MPG: string (nullable = true)
 |-- Cylinders: string (nullable = true)
 |-- Displacement: string (nullable = true)
 |-- Horsepower: string (nullable = true)
 |-- Weight: string (nullable = true)
 |-- Acceleration: string (nullable = true)
 |-- Model: string (nullable = true)
 |-- Origin: string (nullable = true)
"""
#================================ 1.3 SELECT a column in spark-dataframe ===============================
# df.select(df.Car).show(truncate=False)
# Other syntaxs:
# - df.select(df['car'],df['cylinders'])
# - df.select(col('car'),col('cylinders'))
"""
# you also use another method like this
    from pyspark.sql.functions import col
    df.select(col('car')).show(truncate=False)
this will give the same result:
        +--------------------------------+
        |Car                             |
        +--------------------------------+
        |Chevrolet Chevelle Malibu       |
        |Buick Skylark 320               |
        |Plymouth Satellite              |
        |AMC Rebel SST                   |
        |Ford Torino                     |
        |Ford Galaxie 500                |
        |Chevrolet Impala                |
        |Plymouth Fury iii               |
        |Pontiac Catalina                |
        |AMC Ambassador DPL              |
        |Citroen DS-21 Pallas            |
        |Chevrolet Chevelle Concours (sw)|
        |Ford Torino (sw)                |
        |Plymouth Satellite (sw)         |
        |AMC Rebel SST (sw)              |
        |Dodge Challenger SE             |
        |Plymouth 'Cuda 340              |
        |Ford Mustang Boss 302           |
        |Chevrolet Monte Carlo           |
        |Buick Estate Wagon (sw)         |
        +--------------------------------+
        only showing top 20 rows
"""
#=============================================== 1.4. Adding new columns ============================================
# from pyspark.sql.functions import lit
# CASE 1. Adding a new column
# df = df.withColumn('first_column',lit(1)) 
# lit means literal. It populates the row with the literal value given. When adding static data / constant values, it is a good practice to use it.
# df.show(5,truncate=False)
# ......... Output ...................
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+
#|Car                      |MPG |Cylinders|Displacement|Horsepower|Weight|Acceleration|Model|Origin|first_column|
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+
#|Chevrolet Chevelle Malibu|18.0|8        |307.0       |130.0     |3504.0|12.0        |70   |US    |1           |
#|Buick Skylark 320        |15.0|8        |350.0       |165.0     |3693.0|11.5        |70   |US    |1           |
#|Plymouth Satellite       |18.0|8        |318.0       |150.0     |3436.0|11.0        |70   |US    |1           |
#|AMC Rebel SST            |16.0|8        |304.0       |150.0     |3433.0|12.0        |70   |US    |1           |
#|Ford Torino              |17.0|8        |302.0       |140.0     |3449.0|10.5        |70   |US    |1           |
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+
# ===================================================================
# CASE 2. Adding multiple columns
# df = df.withColumn('second_column', lit(2)) \
#        .withColumn('third_column', lit('Third Column'))
# df.show(5,truncate=False)
# ......... Output ...................
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+
#|Car                      |MPG |Cylinders|Displacement|Horsepower|Weight|Acceleration|Model|Origin|first_column|second_column|third_column|
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+
#|Chevrolet Chevelle Malibu|18.0|8        |307.0       |130.0     |3504.0|12.0        |70   |US    |1           |2            |Third Column|
#|Buick Skylark 320        |15.0|8        |350.0       |165.0     |3693.0|11.5        |70   |US    |1           |2            |Third Column|
#|Plymouth Satellite       |18.0|8        |318.0       |150.0     |3436.0|11.0        |70   |US    |1           |2            |Third Column|
#|AMC Rebel SST            |16.0|8        |304.0       |150.0     |3433.0|12.0        |70   |US    |1           |2            |Third Column|
#|Ford Torino              |17.0|8        |302.0       |140.0     |3449.0|10.5        |70   |US    |1           |2            |Third Column|
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+ 
# ===================================================================
# CASE 3. Deriving a new column from an exisitng one
# from pyspark.sql.functions import concat
# df = df.withColumn('car_model', concat(col("Car"), lit(" "), col("model")))
# df.show(5,truncate=False)
# ......... Output ...................
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+----------------------------+
#|Car                      |MPG |Cylinders|Displacement|Horsepower|Weight|Acceleration|Model|Origin|first_column|second_column|third_column|car_model                   |
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+----------------------------+
#|Chevrolet Chevelle Malibu|18.0|8        |307.0       |130.0     |3504.0|12.0        |70   |US    |1           |2            |Third Column|Chevrolet Chevelle Malibu 70|
#|Buick Skylark 320        |15.0|8        |350.0       |165.0     |3693.0|11.5        |70   |US    |1           |2            |Third Column|Buick Skylark 320 70        |
#|Plymouth Satellite       |18.0|8        |318.0       |150.0     |3436.0|11.0        |70   |US    |1           |2            |Third Column|Plymouth Satellite 70       |
#|AMC Rebel SST            |16.0|8        |304.0       |150.0     |3433.0|12.0        |70   |US    |1           |2            |Third Column|AMC Rebel SST 70            |
#|Ford Torino              |17.0|8        |302.0       |140.0     |3449.0|10.5        |70   |US    |1           |2            |Third Column|Ford Torino 70              |
#+-------------------------+----+---------+------------+----------+------+------------+-----+------+------------+-------------+------------+----------------------------+
#=============================================== 1.5. Renaming columns ============================================
#
# df = df.withColumnRenamed('first_column', 'new_column_one') \
#       .withColumnRenamed('second_column', 'new_column_two') \
#       .withColumnRenamed('third_column', 'new_column_three')
#=============================================== 1.6. Grouping by a column ============================================
# df.groupBy('Origin').count().show(5)
#=============================================== 1.7. Removing a column ============================================
# df = df.drop('new_column_one')
#                                                                                                      #
#                                               *************                                          #
#                                ******************************************                            # 
#******************************************************************************************************#
#================================== 2. OPERATIONS ON ROWS ==========================================#
#******************************************************************************************************#
#                                ******************************************                            #
#                                               *************                                          #
#                                                                                                      #
#========== 2.1. Filtering rows in PySpark
# Syntax :
# dataframe.filter(col according to a specific condition)
# df.filter(col('Origin')=='Europe').show(truncate=False)
#========== 2.2. Get Unique Rows
# df.select('Origin').distinct() # for one column
# df.select('Origin','model').distinct().show() # or multiple columns,
#========== 2.3. Sort Rows
# df.orderBy('Cylinders').show(truncate=False) 
#========== 2.4. Union dataframes
# df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
# df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col0"])
# df1.unionByName(df2).show()
# ========================================================================================================