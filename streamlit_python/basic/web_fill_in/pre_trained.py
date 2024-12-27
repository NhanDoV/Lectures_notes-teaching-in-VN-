import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import logging
import joblib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Paths to saved
tf_vec_fpath = "data/tf_vec_model.pkl"
clf_topic_fpath = "data/clf1_model.pkl"
clf_negative_fpath = "data/clf2_model.pkl"

logging.info("Loading data...")
data = pd.read_excel("data/data.xlsx")
logging.info(f"Data (dimension: {data.shape}) to train loaded successfully!!")

tf_vec_all = TfidfVectorizer()
X = tf_vec_all.fit_transform(data['questions'])
tfidf_df = pd.DataFrame(X.toarray(), columns=tf_vec_all.get_feature_names_out())
tfidf_df['topics'] = data['topics']
tfidf_df['if_negative'] = data['if_negative']
tfidf_df.index = data['questions']
logging.info("Vectorizer data processed successfully")

logging.info("Training classifiers...")
clf1 = RandomForestClassifier().fit(X.toarray(), data['topics'])
clf2 = RandomForestClassifier().fit(X.toarray(), data['if_negative'])

logging.info("Saving models...")
# Save the TfidfVectorizer
joblib.dump(tf_vec_all, tf_vec_fpath)

# Save the first classifier (clf1)
joblib.dump(clf1, clf_topic_fpath)

# Save the second classifier (clf2)
joblib.dump(clf2, clf_negative_fpath)

logging.info("Models trained and saved successfully")