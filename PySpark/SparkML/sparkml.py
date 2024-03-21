import os, pickle
from pyspark.sql import functions as F
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler, StandardScaler, StandardScalerModel
from pyspark.ml.clustering import KMeans, KMeansModel

#============================= KMEANS CLUSTERING ============================================
def cluster_model_sparks(spark_data, feat_cols, n_clus):
    """
        Lập mô hình thực hiện segmentation với KMeans
        >> !wget https://jacobceles.github.io/knowledge_repo/colab_and_pyspark/cars.csv
        >> df = spark.read.csv('cars.csv', header=True, sep=";")
        >> feat_cols = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration']
        >> z = cluster_model_sparks(df, feat_cols, 3)
            For n_clusters=3 then Sum of Squared Errors = 0.5651350090846351
    """
    # define features to collect    
    vec_assembler = VectorAssembler(inputCols = feat_cols, outputCol='features')
    vec_assembler.write().overwrite().save("vector_assembles.h5")
    
    # convert the selected columns to integer
    clus_dt = spark_data.select(*(F.col(c).cast("float").alias(c) for c in feat_cols))

    # transform dataset 
    final_data = vec_assembler.transform(clus_dt)

    # scaling data
    scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", 
                            withStd=True, withMean=False).fit(final_data)
    scaler.write().overwrite().save("scaling_model.h5")
    cluster_final_data = scaler.transform(final_data)
    
    # initialize kmeans model
    model = KMeans(featuresCol='scaledFeatures',k=n_clus).fit(cluster_final_data)  
    model.write().overwrite().save("kmeans")
        
    # Make predictions
    predictions = model.transform(cluster_final_data)

    # Evaluate clustering by computing Silhouette score
    evaluator = ClusteringEvaluator()
    silhouette = evaluator.evaluate(predictions)
            
    print(f"For n_clusters={n_clus} then Sum of Squared Errors = " + str(silhouette))
    
    return silhouette

def kmeans_pred(new_df, feat_cols, vec_model, scale_model, kmean_model):
    """
        Lấy kết quả dự đoán từ mô hình KMeans sau khi đã lưu lại ở trước đó
        ====================================================================
        # Chúng ta tiếp tục với cars data như ở trên
        Example,
        >> vec_model = VectorAssembler.load("vector_assembles.h5")
        >> scale_model = StandardScalerModel.load("scaling_model.h5")
        >> kmean_model = KMeansModel.load("kmeans")
    """
    clust_df = new_df.select(*(F.col(c).cast("float").alias(c) for c in feat_cols))
    final_data = vec_model.transform(clust_df)
    cluster_final_data = scale_model.transform(final_data)
    predictions = kmean_model.transform(cluster_final_data)

    # Evaluate clustering by computing Silhouette score
    evaluator = ClusteringEvaluator()
    silhouette = evaluator.evaluate(predictions)
    print("Silhouette with squared euclidean distance = " + str(silhouette))

    # Shows the result.
    centers = kmean_model.clusterCenters()
    return centers

#============================= LINEAR REGRESSION ============================================
from pyspark.ml import Pipeline
from pyspark.ml.regression import RandomForestRegressor, RandomForestRegressionModel
from pyspark.ml.feature import StringIndexer, VectorAssembler

def linreg_spark_model(spark_data, feat_inp, numerical_columns, categorical_columns):
    """
        Ở ví dụ này, ta sẽ lấy minh họa tips-dataset từ seaborn như sau
        >> import seaborn as sns        
        >> pddf = sns.load_dataset("tips")

        # chuyển hóa nó thành spark-dataframe, trước tiên khởi tạo sparksession như sau
        >> from pyspark.sql import SparkSession
        >> from pyspark import SparkConf, SparkContext
        
        # Initialize the Spark-Session
        >> spark = SparkSession.builder.master("local[*]").getOrCreate()

        # Change App-name
        >> spark.sparkContext.appName = "nhan"

        # Property used to format output tables better
        >> conf = SparkConf().setAppName('nhan').set("spark.driver.memory", "4g")\
                                            .set("spark.executor.memory", "12g")\
                                            .set('spark.driver.cores', '5')\
                                            .set('spark.dynamicAllocation.enabled', 'true')\
                                            .set('spark.executor.instances', '0')\
                                            .set('spark.dynamicAllocation.initialExecutors', '0')\
                                            .set('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar')
        >> spark = SparkSession.builder.config(conf=conf).getOrCreate()                
        >> spark_data = spark.createDataFrame(pddf)
        
        # các khai báo dữ liệu chuẩn bị cho mô hình 
        >> feat_inp = ["tip", "total_bill", "size"]
        >> numerical_columns = ["total_bill", "size"]
        >> categorical_columns = ["sex", "smoker", "time", "day"]
        >> linreg_spark_model(spark_data, feat_inp, 
                                            numerical_columns, categorical_columns)

                +----------+----+------+------+---+------+----+----------+-------------+-----------+----------+--------------------+
                |total_bill| tip|   sex|smoker|day|  time|size|sexindexer|smokerindexer|timeindexer|dayindexer|            features|
                +----------+----+------+------+---+------+----+----------+-------------+-----------+----------+--------------------+
                |     16.99|1.01|Female|    No|Sun|Dinner| 2.0|       1.0|          0.0|        0.0|       1.0|[1.0,0.0,0.0,1.0,...|
                |     10.34|1.66|  Male|    No|Sun|Dinner| 3.0|       0.0|          0.0|        0.0|       1.0|[0.0,0.0,0.0,1.0,...|
                |     21.01| 3.5|  Male|    No|Sun|Dinner| 3.0|       0.0|          0.0|        0.0|       1.0|[0.0,0.0,0.0,1.0,...|
                |     23.68|3.31|  Male|    No|Sun|Dinner| 2.0|       0.0|          0.0|        0.0|       1.0|[0.0,0.0,0.0,1.0,...|
                |     24.59|3.61|Female|    No|Sun|Dinner| 4.0|       1.0|          0.0|        0.0|       1.0|[1.0,0.0,0.0,1.0,...|
                +----------+----+------+------+---+------+----+----------+-------------+-----------+----------+--------------------+
                only showing top 5 rows

                predict valid-data
                +--------------------+----+------------------+
                |            features| tip|        prediction|
                +--------------------+----+------------------+
                |(6,[4,5],[16.3099...| 2.0|3.0550599522598096|
                |[0.0,0.0,0.0,1.0,...|1.96|2.5029720593139673|
                |[0.0,1.0,0.0,0.0,...| 3.0| 4.789127769271532|
                |(6,[4,5],[17.5900...|2.64|3.0273099568692357|
                |[0.0,0.0,0.0,3.0,...| 1.5|2.3892730899704855|
                +--------------------+----+------------------+
                only showing top 5 rows                                            
    """
    # transformed
    for c in feat_inp:
        spark_data = spark_data.withColumn(c, F.col(c).cast("float"))

    # feature pre-processing
    pipeline_stages = []
    pipeline_stages=[]
    for value in categorical_columns:
        string_indexer = StringIndexer(inputCol=value, outputCol=value+"indexer")
        pipeline_stages += [string_indexer]

    combined_columns = [columns + "indexer" for columns in categorical_columns] + numerical_columns
    vector_assembler = VectorAssembler(inputCols=combined_columns, outputCol="features")
    pipeline_stages += [vector_assembler]

    # wraping
    pipeline = Pipeline(stages = pipeline_stages)
    pipeline_fit = pipeline.fit(spark_data)
    pipeline_fit.transform(spark_data).show(5)
    df = pipeline_fit.transform(spark_data).select(["features","tip"])

    # train-test split
    training_data, testing_data = df.randomSplit([0.9, 0.1])

    # initialize model
    rf = RandomForestRegressor(featuresCol = 'features', labelCol = 'tip', maxDepth = 30)
    model = rf.fit(training_data)

    # saving model
    pipeline_fit.write().overwrite().save("pipeline")
    model.write().overwrite().save("rf_reg")
    
    print("predict valid-data")
    # Predict the test data
    model.transform(testing_data).show(5)
    
#===================================================
# Predict the new data
def linreg_spark_predict(new_data, reg_model, pipeline_transform):
    """
        >> your_pandas_df = pd.read_csv("testdata.csv")
        >> loadmodel = RandomForestRegressionModel.load("rf_reg")
        >> pipelmodl = PipelineModel.load("pipeline")
        >> new_df = spark.createDataFrame(your_pandas_df)
        >> linreg_spark_predict(new_df, loadmodel, pipelmodl).show(5)
            predict new data
            +--------------------+---+-----------------+
            |            features|tip|       prediction|
            +--------------------+---+-----------------+
            |[0.0,1.0,0.0,1.0,...|3.0|3.170696101252677|
            |[0.0,0.0,0.0,1.0,...|5.0|3.899873294240938|
            |[1.0,1.0,0.0,1.0,...|3.5|3.450900626149443|
            |[0.0,1.0,0.0,1.0,...|2.0| 2.91936633322701|
            |[1.0,1.0,0.0,1.0,...|3.5|3.422483964727985|
            +--------------------+---+-----------------+
            only showing top 5 rows
    """
    print("predict new data")
    new_data = pipeline_transform(new_data).select(["features","tip"])

    return reg_model.transform(new_data)

#============================= CLASSIFICATION ============================================
from pyspark.ml.classification import RandomForestClassifier

def RF_clf_spark(spark_data, target_col):
    """
        >> pddf = sns.load_dataset("iris")
        >> pddf = pddf.replace({"species": {'setosa': 0,'versicolor':1, 'virginica': 2}})
        >> spark_data = spark.createDataFrame(pddf) 
        >> RF_clf_spark(spark_data, "species")

                Pipeline-transformation on your training-set
                +------------+-----------+------------+-----------+-------+--------------------+
                |sepal_length|sepal_width|petal_length|petal_width|species|            features|
                +------------+-----------+------------+-----------+-------+--------------------+
                |         5.1|        3.5|         1.4|        0.2|      0|[5.09999990463256...|
                |         4.9|        3.0|         1.4|        0.2|      0|[4.90000009536743...|
                |         4.7|        3.2|         1.3|        0.2|      0|[4.69999980926513...|
                |         4.6|        3.1|         1.5|        0.2|      0|[4.59999990463256...|
                |         5.0|        3.6|         1.4|        0.2|      0|[5.0,3.5999999046...|
                +------------+-----------+------------+-----------+-------+--------------------+
                only showing top 5 rows

                Pipeline-transformation on your training-set (droped columns is in-importance)
                +----------------------------------------------------------------------------+-------+
                |features                                                                    |species|
                +----------------------------------------------------------------------------+-------+
                |[4.300000190734863,3.0,1.100000023841858,0.10000000149011612]               |0      |
                |[4.400000095367432,2.9000000953674316,1.399999976158142,0.20000000298023224]|0      |
                |[4.599999904632568,3.0999999046325684,1.5,0.20000000298023224]              |0      |
                |[4.599999904632568,3.5999999046325684,1.0,0.20000000298023224]              |0      |
                |[4.699999809265137,3.200000047683716,1.2999999523162842,0.20000000298023224]|0      |
                +----------------------------------------------------------------------------+-------+
                only showing top 5 rows

                
                Predict on your validation data                                                                                
                +--------------------+-------+--------------------+--------------------+----------+
                |            features|species|       rawPrediction|         probability|prediction|
                +--------------------+-------+--------------------+--------------------+----------+
                |[4.59999990463256...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[4.80000019073486...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[4.90000009536743...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[5.0,3.2000000476...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[5.0,3.4000000953...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[5.19999980926513...|      0|      [20.0,0.0,0.0]|       [1.0,0.0,0.0]|       0.0|
                |[5.69999980926513...|      0|      [19.0,1.0,0.0]|     [0.95,0.05,0.0]|       0.0|
                |[5.0,3.5,1.600000...|      0|      [16.0,4.0,0.0]|       [0.8,0.2,0.0]|       0.0|
                |[5.59999990463256...|      1|      [0.0,20.0,0.0]|       [0.0,1.0,0.0]|       1.0|
                |[6.59999990463256...|      1|      [0.0,20.0,0.0]|       [0.0,1.0,0.0]|       1.0|
                |[6.90000009536743...|      1|[0.0,15.633333333...|[0.0,0.7816666666...|       1.0|
                |[5.0,2.2999999523...|      1|      [0.0,20.0,0.0]|       [0.0,1.0,0.0]|       1.0|
                |[5.69999980926513...|      1|      [0.0,20.0,0.0]|       [0.0,1.0,0.0]|       1.0|
                |[6.5,3.0,5.800000...|      2|      [0.0,0.0,20.0]|       [0.0,0.0,1.0]|       2.0|
                |[6.5,3.2000000476...|      2|      [0.0,0.0,20.0]|       [0.0,0.0,1.0]|       2.0|
                +--------------------+-------+--------------------+--------------------+----------+
                only showing top 15 rows        
    """
    for col in spark_data.columns:
        if col != 'species':
            spark_data = spark_data.withColumn(col, F.col(col).cast("float"))
            
    pipeline_stages = []
    assembler = VectorAssembler(inputCols=spark_data.columns[:-1],outputCol = 'features')
    pipeline_stages += [assembler]
    pipeline = Pipeline(stages = pipeline_stages)
    pipeline_fit = pipeline.fit(spark_data)

    print("Pipeline-transformation on your training-set")    
    pipeline_fit.transform(spark_data).show(5)

    df = pipeline_fit.transform(spark_data).select(["features", target_col])
    training_data, testing_data = df.randomSplit([0.8, 0.2])
    lr = RandomForestClassifier(featuresCol = 'features', labelCol = target_col)

    print("Pipeline-transformation on your training-set (droped columns is not important)")
    training_data.show(5, truncate=False)

    # Fit & predict
    print("Predict on your validation data")
    model = lr.fit(training_data)
    model.transform(testing_data).show(15)

    # saving model
    pipeline_fit.write().overwrite().save("pipeline")
    model.write().overwrite().save("clf_rf")