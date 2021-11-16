import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# for classification and KFolds-cross_validate
from sklearn.model_selection import StratifiedKFold, GridSearchCV, cross_val_score, cross_validate

# For evaluating model
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score, accuracy_score, roc_auc_score, log_loss

# For clustering
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# /=================================================================================================\
def classification_preprocessing(data, target_col):
    """
    
    """
    import warnings
    warnings.filterwarnings("ignore")
    from sklearn.preprocessing import LabelEncoder
    
    sns.set_theme(style = "darkgrid", 
                  rc = {"axes.spines.right": False, "axes.spines.top": False})
    num_cols = list(data.columns[data.dtypes != 'object'])
    enc_cols = list(data.columns[data.dtypes == 'object'])
    str_cols = list(set(enc_cols) - set([target_col]))

    if len(num_cols) > 0:
        for col in num_cols:
            data[col] = data[col].fillna(data[col].median())
            
    if len(str_cols) > 0:
        for col in str_cols:
            data[col] = data[col].fillna(data[col].value_counts().index[0])    
            
    LE = LabelEncoder()        
    if len(str_cols) > 0:
        fig, ax = plt.subplots(nrows = len(str_cols), ncols = 1, figsize = (12, 3.75*len(str_cols)))
        for idx, col in enumerate(str_cols):
            sns.countplot(x = col, data = data, hue = target_col, ax = ax[idx])
            for p in ax[idx].patches:
                cnt = p.get_height()
                cnt = np.where(np.isnan(cnt), 0, cnt) 
                ax[idx].annotate(f'\n{cnt}', 
                                xy = (p.get_x() + p.get_width() / 2, p.get_height()),
                                ha = 'center', 
                                va = 'top', 
                                color = 'white', 
                                size = 12)
        plt.show()
        
        data_enc = pd.get_dummies(data[str_cols])
        data_enc = pd.concat([data, data_enc], axis = 1)
        data_enc[target_col] = LE.fit_transform(data_enc[target_col])
        data_plot = data_enc
        
        n_classes = LE.classes_
        transf_mtd = {k : n_classes[k] for k in range(len(n_classes))}              
        final_data = pd.concat([data[target_col], 
                        data_enc.drop(columns = enc_cols)
                        ], 
                        axis = 1)
    else:
        final_data = data.copy()
        data_plot = data.copy()
        data_plot[target_col] = LE.fit_transform(data_plot[target_col])
    
    if data_plot.shape[1] <= 20:
        fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (20, min(12, data_plot.shape[1] / 2)) )
        ax = sns.heatmap(data_plot.corr(), annot=True, cmap='Reds', fmt='.3g')
        plt.show()
        
        fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (20, min(12, data_plot.shape[1] / 2)) )
        sns.countplot(x = target_col, data = data, ax = ax)
        for p in ax.patches:
            cnt = p.get_height()
            cnt = np.where(np.isnan(cnt), 0, cnt) 
            ax.annotate(f'\n{int(p.get_height())}', 
                        xy = (p.get_x() + p.get_width() / 2, p.get_height()),
                        ha = 'center', 
                        va = 'top', 
                        color = 'white', 
                        size = 12)
        plt.show()
        
    if (len(num_cols) > 0) & (len(num_cols) <= 10):
        ax2 = sns.pairplot(data, hue = target_col)
    
    return final_data

# /=================================================================================================\
def get_dict_val(dict_data, col_name):
    """
        This function is used inside the function k_Fold_Best_params_show_all_ in this package
        - Parameters
            dict_data (dataframe)
            col_name
        - Return
    """
    z = 0
    size = len(dict_data)
    for k in range(size):
        p = [val for (key, val) in dict_data[col_name][k].items()]
        names = [key for (key, val) in dict_data[col_name][k].items()]
        z += np.array(p) / size
    
    return {names[k] : np.round(z[k], 4) for k in range(len(names))}        

# /=================================================================================================\
def create_pca_dataset(data, col_to_drop, target_col, keep_ratio = 0.99):
    """
        Parameters
            - data (dataframe)
            - col_to_drop (list of strings) :
            - target_col (str)
            - keep_ratio (float, in 0 and 1)
        Return
    """
    from sklearn.decomposition import PCA
    X = data.drop(columns = col_to_drop + [target_col])
    y = data[target_col]
    pca = PCA(n_components = keep_ratio)
    X_pca = pca.fit_transform(X)
    X_pca = pd.DataFrame(data = X_pca, 
                         columns = ["PC_{}".format(k + 1) for k in range( X_pca.shape[1] ) ])
    X_pca = pd.concat([y, X_pca], axis = 1)
    
    return X_pca  
        
# /=================================================================================================\        
def k_Fold_Best_params_show_all_(data, n_folds, base_est, grid_params, 
                                 clf_column, x_name, y_name,
                                 is_shuffle = True,
                                 show_all = True
                                ):
    """
        This function is used to compute the "all_scores" on the test-set when using K-Fold cross-validate
        Parameters
            - data (dataframe)
            - n_folds (int) : number of folds
            - clf_column (str) : target-column
            - grid_params (dict)
            - x_name, y_name : column to view in the train-test-split
            - show_all (boolean) : display the classification_reports and the scatter-charts or not
    """
    import time
    import warnings
    
    t0 = time.time()
    warnings.filterwarnings("ignore")
    
    cv_kfolds = StratifiedKFold(n_splits = n_folds, shuffle = is_shuffle)
    grid_clf = GridSearchCV(base_est, param_grid = grid_params, cv = cv_kfolds)
    
    X = data.drop(columns = clf_column)
    y = data[clf_column]
    grid_clf.fit(X, y)
    
    best_params = grid_clf.best_params_
    clf = base_est.set_params(**best_params)
    dict_data = pd.DataFrame(columns = ['ROC_AUC', 'accuracy', 'f1_score', 'precison',
                                        'recall', 'log_loss(cross-entropy)'])
    
    time_measured = time.time() - t0
    cv_kfolds = StratifiedKFold(n_splits = n_folds, 
                                shuffle = True, random_state = 20)
    print("{}\nBest parameters = {} \nTrained_time = {} minutes, {} seconds \n{}".format(100*"=",
                                                                                          best_params,
                                                                                          time_measured // 60,
                                                                                          np.round(time_measured % 60, 2),
                                                                                          100*"-"))

    sns.set_theme(style = "darkgrid", 
                  rc = {"axes.spines.right": False, "axes.spines.top": False})
    fig, ax = plt.subplots(nrows = n_folds, ncols = 4, figsize = (22, 7.2*n_folds))
    ax = ax.ravel()    
    
    for idx, (train_index, test_index) in enumerate(cv_kfolds.split(X, y)):

        X_fold_k_train = X.loc[train_index]
        y_fold_k_train = y.loc[train_index]
        data_train_fold_k = pd.concat([X_fold_k_train, y_fold_k_train], axis = 1)

        X_fold_k_test = X.loc[test_index]
        y_fold_k_test = y.loc[test_index]
        data_test_fold_k = pd.concat([X_fold_k_test, y_fold_k_test], axis = 1)

        clf.fit(X_fold_k_train, y_fold_k_train)
        base_est = clf
        base_est.fit(X_fold_k_train, y_fold_k_train)

        y_train_pred = pd.DataFrame({clf_column: base_est.predict(X_fold_k_train)},
                                    index = X_fold_k_train.index
                                   )
        data_train_pred_k = pd.concat([X_fold_k_train, y_train_pred], axis = 1)

        y_test_pred = pd.DataFrame({clf_column: base_est.predict(X_fold_k_test)},
                                   index = X_fold_k_test.index
                                  )
        data_test_pred_k = pd.concat([X_fold_k_test, y_test_pred], axis = 1)

        train_acc = base_est.score(X_fold_k_train, y_fold_k_train)
        test_acc = base_est.score(X_fold_k_test, y_fold_k_test)

        # Show the train_set (true)
        k_idx = idx*4
        sns.scatterplot(x=x_name, y = y_name, data = data_train_fold_k, hue = clf_column, 
                        ax = ax[k_idx])
        ax[k_idx].set_title("Split_{} - train-set (true) \nFold{} used to test".format(idx + 1, idx + 1))

        # Show the predict on the train-set
        sns.scatterplot(x=x_name, y = y_name, data = data_train_pred_k, hue = clf_column,
                        ax = ax[k_idx + 1])
        ax[k_idx + 1].set_title("Split_{} - train-set (predict) \n acc = {} %".format(idx + 1, 
                                                                                         np.round(100*train_acc, 2)))

        # Test-set
        sns.scatterplot(x=x_name, y = y_name, data = data_test_fold_k, hue = clf_column,
                        ax = ax[k_idx + 2])
        ax[k_idx + 2].set_title("Split_{} - test-set (true)".format(idx + 1))

        # Test-set (predict)
        sns.scatterplot(x=x_name, y = y_name, data = data_test_pred_k, hue = clf_column,
                        ax = ax[k_idx + 3])
        ax[k_idx + 3].set_title("Split_{} - test-set (predict)\n acc = {} %".format(idx + 1, 
                                                                                       np.round(100*test_acc, 2)))
        
        y_fold_k_pred = clf.predict(X_fold_k_test)
        target_values = y_fold_k_test.unique()

        # Compute the accuracy
        acc_score = accuracy_score(y_fold_k_test, y_fold_k_pred)

        # Compute precision
        kf = len(y.unique())
        kfold_precisn = precision_score(y_fold_k_test, y_fold_k_pred, average=None)
        kfold_precisn = [np.round(x, 2) for x in kfold_precisn]
        k_precisions = {target_values[idx] : kfold_precisn[idx] for idx in range(kf)}

        # Compute recall
        kfold_recall = recall_score(y_fold_k_test, y_fold_k_pred, average=None)
        kfold_recall = [np.round(x, 2) for x in kfold_recall]
        k_recalls = {target_values[idx] : kfold_recall[idx] for idx in range(kf)}

        # Compue f1-score
        kfold_f1_score = f1_score(y_fold_k_test, y_fold_k_pred, average=None)
        kfold_f1_score = [np.round(x, 2) for x in kfold_f1_score]
        k_f1_scores = {target_values[idx] : kfold_f1_score[idx] for idx in range(kf)}

        # Compute ROC_AUC_score
        y_proba = clf.predict_proba(X_fold_k_test)
        if kf > 2:
            roc_auc = roc_auc_score(y_fold_k_test, y_proba,
                                average = 'weighted', multi_class = 'ovr')
        else:
            roc_auc = roc_auc_score(y_fold_k_test, y_proba[:, 1])

        # Cross-entropy
        crs_ent = log_loss(y_fold_k_test, y_proba)
        split_id = "Split_{}".format(idx + 1)
        dict_data.loc[split_id] = [roc_auc, acc_score, k_f1_scores, k_precisions, k_recalls, crs_ent]

        # Display charts or report
        if show_all == 1:
            print("{}\nSplit_{}. Classification report (on the test-set only).\n{}".format(100*"=",
                                                                                           idx+1, 
                                                                                           100*"=")
                 )
            print(classification_report(y_fold_k_test, y_fold_k_pred))  
            
        else:
            plt.close()
    
    avg_precison = get_dict_val(dict_data,'precison')
    avg_f1_score = get_dict_val(dict_data,'f1_score')
    avg_recall = get_dict_val(dict_data,'f1_score')
    avg_rocauc = dict_data['ROC_AUC'].mean()
    avg_loss = dict_data['log_loss(cross-entropy)'].mean()
    avg_acc = dict_data['accuracy'].mean()
    dict_data.loc['avg_score_k_split'] = (avg_rocauc, avg_acc, avg_f1_score, avg_precison, avg_recall, avg_loss)
    
    dict_data['n_features'] = X.shape[1]
    dict_data['best_param'] = len(dict_data)*[best_params]
    
    return dict_data

# /=================================================================================================\
def table_count_null(data):
    """
        This function is used to count the missing-values at all columns in frequencies and percentages
    """
    tab_null = pd.DataFrame(data.dtypes).T.rename(index = {0:'column_type'})
    tab_null = tab_null.append(pd.DataFrame(data.isnull().sum()).T.rename(index={0:'cnt_null_data (nb)'}))
    tab_null = tab_null.append(pd.DataFrame(data.isnull().sum()/data.shape[0]*100).T.rename(index={0:'cnt_null_data (%)'}))
    
    return tab_null

# /=================================================================================================\
def pie_params(labels):
    """
        This function is used to create the parameters of pie-charts from the other functions.
        Parameters
        - labels (label of corresponding col_name) : must be in ['month', 'year', 'is_weekend', 'weekday']
    """
    from numpy.random import uniform as unif
    colors = [(round(unif(0.6, 0.9), 2),
                   round(unif(0.6, 0.9), 2), 
                   round(unif(0.6, 0.9), 2))  for k in range(len(labels))]
    if len(labels) >= 12:
        explode = tuple(4*[0, 0, 0.1] + [0]*(len(labels) - 12))
    elif (len(labels) >= 5) & (len(labels) < 12):
        explode = tuple([0, 0.1, 0, 0.1, 0] + [0]*(len(labels) - 5))
    elif (len(labels) > 2) & (len(labels) < 5):
        explode = tuple([0, 0.1] + [0]*(len(labels) - 2))
    else:
        explode = (0, 0.1)

    return explode, colors

# /=================================================================================================\
def data_expand_date(data):
    """
    
    """
    import warnings
    warnings.filterwarnings("ignore")
    
    data['month'] = data['InvoiceDate'].dt.month_name().apply(lambda x: x[:3])
    data['year'] = data['InvoiceDate'].dt.year
    data['quarter'] = data['InvoiceDate'].dt.quarter.apply(lambda x: 'Quarter_{}'.format(x))
    data['is_weekend'] = data['InvoiceDate'].dt.weekday.apply(lambda x: 'weekend' if x >= 5 else 'weekday')
    data['weekday'] = data['InvoiceDate'].dt.day_name().apply(lambda x: x[:3])
    
    return data

# /=================================================================================================\
def view_data_by_date(data, quan_cols):
    """
    
    """
    n_col = len(quan_cols) + 1
    date_cols = ['month', 'year', 'is_weekend', 'weekday', 'quarter']
    fig, ax = plt.subplots(nrows = 5, ncols = n_col, figsize = (22, 35))
    ax = ax.ravel()

    for idx, col in enumerate(date_cols):

        # column 1
        labels_1 = data[col].value_counts().index
        values_1 = data[col].value_counts().values
        explode_1, colors_1 = pie_params(labels_1)
        ax[n_col*idx].pie(values_1, explode = explode_1, colors = colors_1,
                    labels = labels_1, autopct = '%1.1f%%',shadow = True, startangle = 90)
        ax[n_col*idx].set_title("count of records {}".format(col))

        # column 2-3
        for k, cl in enumerate(quan_cols):
            labels_2 = data.groupby(col).sum()[cl].index
            values_2 = data.groupby(col).sum()[cl].values
            explode_2, colors_2 = pie_params(labels_2)
            ax[n_col*idx + k + 1].pie(values_2, explode = explode_2, colors = colors_2,
                        labels = labels_2, autopct = '%1.1f%%',shadow = True, startangle = 90)
            ax[n_col*idx + k + 1].set_title("Total {} by {}".format(cl, col))    
            
# /=================================================================================================\            
def data_duplicate(data):
    """
    
    """
    print("|{}\n|\tThe initial_shape of your dataset is {}\n|{}".format(100*'*', data.shape, 100*'-'))
    n_before = data.shape[0]
    data = data.drop_duplicates()
    n_then = data.shape[0]
    print("|\tNumber of duplicated-values = {}, about {}% of initial dataset.\n|{}".format(n_before - n_then, 
                                                                                     100*float(n_before - n_then) / n_before,
                                                                                     100*'-'
                                                                                        )
         )
    print("|\tViewing the first 5 rows.\n|{}".format(100*'*'))
    display(data.head())
    
    return data

# /=================================================================================================\
def table_count_unique(data):
    """
        This function is used to compute the number of 
            - unique (distinct) value
            - value of the most_occurrences element and its frequencies / percentages
        from your input data.
    """
    col_name = data.columns
    tab_distinct = pd.DataFrame(data.dtypes).T.rename(index = {0:'column_type'})
    tab_distinct = tab_distinct.append(pd.DataFrame({'cnt_unique (nb)': [len(data[col].unique()) for col in data.columns]}, 
                                                    index = data.columns).T)
    
    tab_distinct = tab_distinct.append(pd.DataFrame({'most_appeared_value': [list(data[col].mode().values) for col in data.columns]}, 
                                                    index = data.columns).T)
    tab_distinct = tab_distinct.append(pd.DataFrame({'cnt_occurrences (nb)':[data[x].isin(data[x].mode()).sum() for x in data]},
                                                    index = data.columns).T                                       
                                      )
    tab_distinct.loc['cnt_occurrences (%)'] = tab_distinct.loc['cnt_occurrences (nb)'] / len(data) * 100
    
    return tab_distinct

# /=================================================================================================\
def viewing_by_country(df, observed_cols):
    """
        data (dataframe)
        observed_cols must contain the country at least.
    """
    import plotly.graph_objs as go
    from plotly.offline import init_notebook_mode,iplot
    
    temp = df[observed_cols].groupby(observed_cols).count()
    temp = temp.reset_index(drop = False)
    countries = temp['Country'].value_counts()
    data = dict(type = 'choropleth',
                locations = countries.index,
                locationmode = 'country names', z = countries,
                text = countries.index, colorbar = {'title':'Order nb.'},
                colorscale=[[0, 'rgb(224,255,255)'],
                            [0.01, 'rgb(166,206,227)'], [0.02, 'rgb(31,120,180)'],
                            [0.03, 'rgb(178,223,138)'], [0.05, 'rgb(51,160,44)'],
                            [0.10, 'rgb(251,154,153)'], [0.20, 'rgb(255,255,0)'],
                            [1, 'rgb(227,26,28)']],    
                reversescale = False
               )
    layout = dict(title = 'Number of orders by country',
                  geo = dict(showframe = True, projection={'type':'mercator'})
                 )
    fig = go.Figure(data = [data], layout = layout)
    fig.update_layout(autosize = False, width = 1000, height = 700)
    iplot(fig)
    
# /=================================================================================================\    
def initial_viewing(data, inc_col, age_col, sex_col, score_col):
    """
        Parameters
            - data (dataframe)
            - inc_col (str) column of income
            - age_col
            - sex_col
            - score_col
        Return
    """
    import warnings
    warnings.filterwarnings("ignore")
    
    fig, ax = plt.subplots(nrows = 3, ncols = 3, figsize = (20, 12))
    ax = ax.ravel()
    sns.set_theme(style = "darkgrid", 
                  rc = {"axes.spines.right": False, "axes.spines.top": False})
    cols = [inc_col, age_col, score_col]
    conj = [score_col, inc_col, age_col]
    for idx, col in enumerate(cols):
        sns.boxplot(x = col, y = sex_col, data = data, ax = ax[idx])
        sns.scatterplot(x = cols[idx], y = conj[idx], 
                        hue = sex_col, data = data, ax = ax[idx + 3])
        sns.histplot(x = col, hue = sex_col, data = data, 
                     kde = True, ax = ax[idx + 6])
    plt.show()
    
    #fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 4))
    plt.rcParams["figure.figsize"] = (18, 4)
    plt.subplot(121); 
    ax = sns.heatmap(data.corr(), annot=True, cmap='viridis')
    plt.subplot(122)
    ax = sns.countplot(x = sex_col, data = data)
    for p in ax.patches:
        cnt = p.get_height()
        cnt = np.where(np.isnan(cnt), 0, cnt) 
        ax.annotate(f'\n{cnt}', 
                        xy = (p.get_x() + p.get_width() / 2, p.get_height()),
                        ha = 'center', 
                        va = 'top', 
                        color = 'white', 
                        size = 12)
    plt.show()
    
# /=================================================================================================\    
def scaling_data(data, set_index_col, drop_num_cols, type_of_scaling):
    """
        This function is used to scaling your numeric-dataset
        Parameters
            - data : input dataframe
            
            - drop_num_col : determine which numeric column to drop, such as the constant_column or the un-importance info such as, customer_id, company_id, stock_code, etc.
                             if you don't want to drop any column, please set drop_num_cols = [] 
                             
            - set_index_col : the column take the unique_values, for example, the customer_id;
                             if you don't want to set any column as the index, please set set_idx_cols = None 
                             
            - type_of_scaling (norm, robust, min_max)
            - epsilon : in case that you apply min_max and your dataset has the maximize_value = 0
    """
    
    data = data.drop(columns = drop_num_cols)
    from sklearn.preprocessing import StandardScaler
    
    if set_index_col == 'None':
        data = data
    else:
        data = data.set_index(set_index_col)
        
    num_df = data._get_numeric_data()
    str_cl = list(set(data.columns) - set(num_df.columns))
    str_df = pd.get_dummies(data[str_cl], prefix_sep='_is_')
    
    if type_of_scaling == 'norm':
        scaler = StandardScaler()
        #num_df = scaler.fit_transform(num_df)
        
        # This equivalent to
        num_df = (num_df - num_df.mean())/num_df.std()
        
    elif type_of_scaling == 'min_max':
        num_df = (num_df - num_df.min()) / (num_df.max() - num_df.min())
        
    elif type_of_scaling == 'robust':
        q1 = num_df.quantile(0.25)
        q3 = num_df.quantile(0.25)
        num_df = (num_df - q1) / (q3 - q1)
        
    else:
        raise ValueError("the 'type_of_scaling' must be {'norm', 'robust', 'min_max'}")
        
    end_df = pd.concat([num_df, str_df], axis = 1)
    
    return end_df

# /=================================================================================================\    
def anomallies_removed(data, anm_rmv_col):
    """
        This function is used to remove the outliers at a given column in the dataset.
        Parameters
            - data : dataframe
            - anm_rmv_col: column that contains outlier to remove
    """
    rmv_data = data[anm_rmv_col]
    Q1 = rmv_data.quantile(0.25)
    Q3 = rmv_data.quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5*IQR
    upper_limit = Q3 + 1.5*IQR
    indexes = rmv_data[~((rmv_data >= lower_limit) & (rmv_data <= upper_limit))].index
    rmv_data = data.drop(indexes)

    return rmv_data

# /=================================================================================================\    
def clusters_scored(data):
    """
        This function is used to score the number of clusters in your dataset by viewing the Elbow method and Silhouette_metrics
        The higher Silhoutte and the lower elbow (that stops decreasing drastically) is the better.
    """
    X = data.copy()
    k_clusters = range(2, 13)
    silh0u_score = []
    elb0w_score = []

    #fig, ax = plt.subplots(2, 4, figsize = (20, 5))
    for k in k_clusters:
        k_means = KMeans(n_clusters = k).fit(X)
        labels = k_means.fit_predict(X)
        silh0u_score.append(silhouette_score(X, labels = labels))
        elb0w_score.append(k_means.inertia_)

    fig, ax = plt.subplots(1, 2, figsize = (20, 5))
    ax[0].plot(k_clusters, silh0u_score)
    ax[0].set_title('silhouette_score')
    ax[1].plot(k_clusters, elb0w_score)
    ax[1].set_title('Elbow method')
    
# /=================================================================================================\    
def cluster_views(data, n_clusters, x1_name, x2_name, x3_name):
    """
        This function is used to verify the number of clusters that you assume this is the best in your clustering-model
    """

    X = data
    x_list = [x1_name, x2_name, x3_name]
    y_list = [x2_name, x3_name, x1_name]

    n_rows = len(n_clusters)
    
    fig, ax = plt.subplots(n_rows, 3, figsize = (20, int(n_rows*5.5)))
    ax = ax.ravel()

    for idx, k_cluster in enumerate(n_clusters):
        k_cluster_df = data.copy()
        k_means = KMeans(n_clusters = k_cluster).fit(X)
        labels = k_means.fit_predict(X)
        k_cluster_df['clusters'] = ['cluster_'+str(k + 1) for k in labels]
        
        for k, col in enumerate(x_list):
            sns.scatterplot(x = col, y = y_list[k], 
                            hue = 'clusters', data = k_cluster_df, ax = ax[3*idx + k])
            ax[3*idx + k].set_title("Number_of_clusters = {}".format(k_cluster))  
            
# /=================================================================================================\ 
def add_labels(data, drop_cols, nb_cluster):
    """
        Add label into your final model
    """
    keep = data[drop_cols]
    data = data.drop(columns = drop_cols)
    k_means = KMeans(n_clusters = nb_cluster).fit(data)
    labels = k_means.fit_predict(data)
    data['clusters'] = ['cluster_'+str(k + 1) for k in labels]
    
    return pd.concat([keep, data], axis = 1)

# /=================================================================================================\ 
def final_market_analytics__type_1_(clusters_df, id_col, sex_col):
    """
    
    """
    df_add_label = clusters_df.set_index(id_col)
    avg_data = df_add_label.groupby(['clusters'], as_index=False).mean()
    cols = avg_data.drop(columns = 'clusters').columns
    fig, ax = plt.subplots(2, 2, figsize=(20, 11))
    ax = ax.ravel()
    for k, col in enumerate(cols):
        sns.barplot(x = 'clusters', y = col, 
                    palette="plasma" , data = avg_data, ax = ax[k])
        for p in ax[k].patches:
            cnt = p.get_height()
            cnt = np.where(np.isnan(cnt), 0, cnt)
            cnt = np.round(cnt, 3)
            ax[k].annotate(f'\n{cnt}', 
                            xy = (p.get_x() + p.get_width() / 2, p.get_height()),
                            ha = 'center', 
                            va = 'top', 
                            color = 'white', 
                            size = 12)
            ax[k].set_title("Average_{} by each cluster".format(col))

    sns.countplot(x = 'clusters', hue = 'Gender', palette="plasma", 
                  data = df_add_label, ax = ax[3])
    for p in ax[3].patches:
            cnt = p.get_height()
            cnt = np.where(np.isnan(cnt), 0, cnt) 
            ax[3].annotate(f'\n{cnt}', 
                            xy = (p.get_x() + p.get_width() / 2, p.get_height()),
                            ha = 'center', 
                            va = 'top', 
                            color = 'white', 
                            size = 12)
            ax[3].set_title("gender_count by each cluster")
            
# /=================================================================================================\                
def view_top(data, product_col, trans_col, client_col, quan_col, sale_date, top_N = 10):
    """
        - data (dataframe)
        - product_col : columns that display the product is sold or not
        - trans_col : transaction column (related invoice_date)
        - client_col : the id of client
        - quan_col : quantity of the product sold
    """
    print("{}\nNumber of users, transaction and products.\n{}".format(100*"=", 100*"="))
    display(pd.DataFrame([{'products': len(data[product_col].value_counts()),    
                           'transactions': len(data[trans_col].value_counts()),
                           'customers': len(data[client_col].value_counts()),  
                          }], 
                         columns = ['products', 'transactions', 'customers'], 
                         index = [quan_col]
                       )
           )
    print("{}\nNumber of products purchased in every transaction (to top {}).\n{}".format(100*"=", top_N, 100*"="))
    temp = data.groupby(by=[client_col, trans_col], as_index=False)[sale_date].count()
    nb_products_per_basket = temp.rename(columns = {sale_date: 'Number of products'})
    display(nb_products_per_basket[:top_N].sort_values(client_col))
    
    nb_products_per_basket['order_canceled'] = nb_products_per_basket['InvoiceNo'].apply(lambda x:int('C' in x))
    
