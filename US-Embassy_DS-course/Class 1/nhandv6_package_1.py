import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold

# /=================================================================================================\
def MAPE(y_true, y_pred):
    """
        Compute the MAPE (mean absolute percentage error)
        Input
            y_true (series/ list/ array): actual value
            y_pred (series/ list/ array): forecast value
        Return 
            MAPE_score
        |/==========================================================================\
        |
        |  Example.
        |
        |=========================================================================
        | >>> MAPE(y_true = [1,2,3], 
        |          y_pred = [2,3,4]
        |         )
        | 0.5
        |-----------------------------------------------------------------------------
        | >>> MAPE(y_true = [1, 0, 3, 3],
        |          y_pred = [1, 0, 2, 0]
        |          )
        |----------------------------------------------------------------------------- 
        | your actual_values contains many zero values, make the MAPE values won't be correct
        | 0.4444444444444444
        |
        | >>> MAPE(y_true = pd.Series([1,0,3,3]), 
        |          y_pred = [1, 0, 2, 2]
        | your actual_values contains many zero values, make the MAPE values won't be correct
        | 0.2222222222222222
        |--------------------------------------------------------------------------------\
        |/=================================================================================
    )
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    if len(y_true[y_true==0]) > 0:
        print("your actual_values contains many zero values, make the MAPE values won't be correct")
        y_tr = y_true[y_true != 0]
        y_pr = y_pred[y_true != 0]
        res = np.mean(np.abs(y_tr - y_pr) / y_tr)
    
    else:        
        res = np.mean(np.abs(y_true - y_pred) / y_true)
        
    return res

def MAE(y_true, y_pred):
    """
        Compute the MAE (mean absolute error)
        Input
            y_true : actual value
            y_pred : forecast value
        Return 
            MAE_score
    """
    return np.mean(np.abs(y_true - y_pred))

def MSE(y_true, y_pred):
    """
        Compute the MSE (mean square error)
        Input
            y_true : actual value
            y_pred : forecast value
        Return 
            MAPE_score
    """    
    return np.mean((y_true - y_pred)**2)

def RMSE(y_true, y_pred):
    """
        Compute the RMSE (root mean square error)
        Input
            y_true : actual value
            y_pred : forecast value
        Return 
            MAPE_score
    """    
    return np.sqrt(MSE(y_true, y_pred))

# /=================================================================================================\
def regression_compare(df_train, df_test, target_col, h = 5):
    """
        This function is used to compare the basic_charts in regression problems.
        Paramters:
            - df_train, df_test (dataframes)
            - target_col (str) : target column from the dataset
            - h (float) : the height of each cell_image
            
        Return / Display : 
            - scatter plot of all the input-feature and target column, and,
            - heatmaps of the correlation matrix to the target 
            - distribution plots of the target column
    """
    df_train['flg'] = 'train-set'
    df_test['flg'] = 'test-set'
    df_full = pd.concat([df_train, df_test])
    df_full = df_full.reset_index()

    rem_cols = list(df_full.corr()[[target_col]].sort_values(by=target_col, ascending = False).index)
    temp_df = df_full.drop(columns = ['index', target_col])
    cols = temp_df._get_numeric_data().columns
    if len(cols) % 2 == 0:
        cols = cols
    else:
        cols = list(set(cols) - set(rem_cols[-1]))
    
    nrows = 1 + len(cols) // 2
    height = h*nrows
    fig, ax = plt.subplots(nrows = nrows, ncols = 2, figsize = (20, height))
    ax = ax.ravel()
    
    for idx, col in enumerate(cols):
        if idx < 2*(nrows - 1):
            sns.scatterplot(x = col, y = target_col, hue = 'flg', data = df_full, ax = ax[idx])

    sns.heatmap(df_train.corr(), annot=True, cmap='Reds', fmt='.3g', ax = ax[2*(nrows - 1)])
    ax[2*(nrows - 1)].set_title('train-set')
    sns.heatmap(df_test.corr(), annot=True, cmap='Reds', fmt='.3g', ax = ax[1 + 2*(nrows - 1)])
    ax[2*(nrows - 1) + 1].set_title('test-set')
    
    sns.displot(data = df_full, x = target_col, hue = 'flg', kind='kde', fill=True, height=5, aspect=3)

# /=================================================================================================\
def count_null_show(data_train, data_test, figsize = (20, 6), rotation = 30):
    """
        This function is used to show the null_values at each column in train and test-set
        Parameters:
            - data_train, data_test (dataframes) : your input dataframe as train and test-sets
            - figsize (tuple) : figure size = width x height (inches)
            - rotation (int) : the rotation angle of the x_label and the column_names
        Returns:
            - "count of misssing value"
            - "percentage of missing value"
    """
    null_count_df = pd.DataFrame({'column': data_train.isnull().sum().index,
                                  'train-set': data_train.isnull().sum().values,
                                  'test-set': data_test.isnull().sum().values
                         })

    null_percn_df = pd.DataFrame({'column': data_train.isnull().sum().index,
                                  'train-set': 100*data_train.isnull().sum().values / len(data_train),
                                  'test-set': 100*data_test.isnull().sum().values / len(data_test)
                             })
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 6))
    data = [null_count_df, null_percn_df]
    titles = ['count of missing value', 'percentage of missing value']
    for k in range(2):
        data[k].plot(x = 'column', kind = 'bar', ax = ax[k], rot = rotation)
        ax[k].set_title(titles[k])
        ax[k].set_xlabel('column_names')
    plt.show()
   
# /=================================================================================================\
def count_unique_and_mode(df_train, df_test):
    """
        Print out the dataframe of the number of unique, statistical_mode-value from the input datasets.
        Parameters:
            df_train, df_test (dataframes) : input dataframe
        Return :
            dataframe that contains the info of column_types, column_name, number of unique and
                                                statistical_mode-value at each input dataset,
                                                if all the category_value in test-set is contained in train-set?
    """

    data = pd.DataFrame(columns = ['col_name', 'col_type',                                    
                                   '(mode-vl, freq, Nb_unique)_train-set',
                                   '(mode-vl, freq, Nb_unique)_test-set',
                                   'is_all-test_contained_in_train ?'
                           ])
    data['col_name'] = df_train.columns
    data = data.set_index('col_name')
    for col in df_train.columns:

        data.loc[col, 'col_type'] = df_train[col].dtype
        train_mode_values = df_train[col].value_counts().reset_index()
        test_mode_values = df_test[col].value_counts().reset_index()

        data.loc[col, '(mode-vl, freq, Nb_unique)_train-set'] = train_mode_values.loc[0, 'index'], train_mode_values.loc[0, col], len(df_train[col].unique())
        data.loc[col, '(mode-vl, freq, Nb_unique)_test-set'] = test_mode_values.loc[0, 'index'], test_mode_values.loc[0, col], len(df_test[col].unique())
        
        if df_train[col].dtype != 'object':
            data.loc[col, 'is_all-test_contained_in_train ?'] = 'Ignored! This column is numeric'
        else:
            in_test_not_in_train = set(df_test[col].unique()) - set(df_train[col].unique())
            if len(in_test_not_in_train) > 0:
                data.loc[col, 'is_all-test_contained_in_train ?'] = False, in_test_not_in_train
            else:
                data.loc[col, 'is_all-test_contained_in_train ?'] = True

    return data

# /=================================================================================================\
def Q_Q_plot(model, X_train, X_test, y_train, y_test):
    """
        A Q-Q plot is a plot of the quantiles of the first data set against the quantiles of the second data set.
        Input
            - model : trained model
            - X_train, X_test, y_train, y_test : your datasets
        Return
            compare the quantile-quantile plot of (actual, forecast) on train and test-set.
        The more the data-points scattered arround the diagonal, the better your model.
    """
    from sklearn.metrics import r2_score
    
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 6))
    X = [X_train, X_test]
    y = [y_train, y_test]
    tiltes = ['train-set', 'test-set']
    scores = [r2_score(y_train, model.predict(X_train)),
              r2_score(y_test, model.predict(X_test))
             ]
    
    for k in range(2):
        ax[k].plot(y[k], model.predict(X[k]), '.')
        ax[k].plot(y[k], y[k], '-')
        ax[k].set_title("Q-Q plot - {}, R2_score = {}".format(tiltes[k], scores[k]))
        ax[k].set_xlabel('actual')
        ax[k].set_ylabel('forecast')

# /=================================================================================================\        
def load_data(data, fill_vl = None, 
              target_col = 'price', 
              inp_col_names = ['age', 'area', 'nb_bedroom', 'nb_bathroom']):
    """
        |\=====================================================================================================/
        | This function is used to load dataset and impute the missing values, also drop the duplicates values
        | Input
        |    data (dataframe) : data to load
        |    fill_vl (str or None): which values filled in the missing place
        |    target_col (column name) : column of the target in your model.
        |    inp_col_names (column names): input column names
        | Output
        |    cleaned data and its target.    
        |/======================================================================================================\
        |
        | Example.
        |
        |\******************************************************************************************************/
        | >>> data = pd.DataFrame({'x': [1, 2, 1, 0, 2],
        |                          'y': [1, 3, 1, '', 3],
        |                          'z': [1, 2, 1, 3, 2]
        |                         })
        | >>> data
        |
        |     |-----------|
        |     | x | y | z |
        |     |---+---+---|
        |  0  | 1 | 1 | 1 |
        |  1  | 2 | 3 | 2 |
        |  2  | 1 | 1 | 1 | 
        |  3  | 0 |   | 3 |
        |  4  | 2 | 3 | 2 |
        |     |-----------|
        |
        | >>> load_data(data)
        |   
        | (  |-------|
        |    | x | y |
        |    |---+---|
        |  0 | 1 | 1 |
        |  1 | 2 | 3 |
        |  3 | 0 | 3 |
        |    |-------| ,
        |
        |  0    1
        |  1    2
        |  3    2
        | Name: z, dtype: int64)
        | 
        |/==========================================================================================================\        
    """
    data = data.drop_duplicates()
    X = data[inp_col_names]
    if (fill_vl != None).all():
        X = X.fillna(fill_vl)
    else:
        X = X.fillna(X.median())

    y = data[target_col]

    return X, y

# /=================================================================================================\
def load_data2(data, 
               fill_vl = None, 
               target_col = 'price', 
               x1_name = 'age', x2_name = 'area', x3_name = 'nb_bedroom', x4_name = 'nb_bathroom',
               new_feat_name = 'area_p_rm',
               c1 = 1, c2 = 100):
    """
        |\=====================================================================================================/
        |   This function is used to load dataset and impute the missing values, also drop the duplicates values,
        | also generated the new features in many specified cases, that will transform the regression model like
        |     
        |    Y = a0 + a1 * X1 + a2 * X2 + a3*X3 + a4*X4
        |
        | into
        |
        |   log(Y) = b0 + b1*log(X1 + c1) + b2*log(X2 + c2) + b3*(X2/(X3 + X4))
        | 
        |--------------------------------------------------------------------------------------------------------
        | Input
        |    data (dataframe) : data to load
        |    fill_vl (str or None): which values filled in the missing place
        |    target_col (column name) : column of the target in your model.
        |    x1_name, ..., x4_name : your input column_names that affect to your model's assumption
        |    new_feat_name : name of the new feature generated by X2/(X3 + X4)
        |    c1, c2 (constants) : the constant added to the algorithm
        | Output
        |    cleaned data and its target.    
        |/======================================================================================================\
        |
        | Example.
        |
        |\******************************************************************************************************/
        | Read the specific example on my github!
        |      https://github.com/Nhan121/Lectures_notes-teaching-in-VN-/tree/master/US-Embassy_DS-course/Class%201
        |/======================================================================================================\
        
    """
    inp_col_names = [x1_name, x2_name, x3_name, x4_name]
    data = data.drop_duplicates()
    X = data[inp_col_names]
    y = data[target_col]
    if (fill_vl != None).all():
        X = X.fillna(X.median())
    else:
        X = X.fillna(fill_vl)

    X[x1_name] = np.log(X[x1_name] + c1) / np.log(10)
    X[new_feat_name] = X[x2_name] / X[[x3_name, x4_name]].sum(axis=1)
    X[x2_name] = np.log(X[x2_name] + c2)

    y = np.log(y) / np.log(10)
    X = X.drop(columns = [x3_name, x4_name])
    
    return X, y

# /=================================================================================================\
def avg_std_KFold_plot_(model, nb_folds_min, nb_folds_max, 
                        X_train , y_train):
    """
        This function is used to plot the avg(score) and stdev(score)
        Input
            - model (base estimators)
            - nb_folds_min (int)
            - nb_folds_max (int)
            - X_train, y_train : your train-set
        Return:
            charts of avg and stdev_score
    """
    model.fit(X_train, y_train)
    m_scores = []
    s_scores = []
    kfold_range = range(nb_folds_min, nb_folds_max + 1)
    for n_folds in kfold_range:
        kfold_cv = KFold(n_splits = n_folds, shuffle=True, random_state=53)
        kfold_scores = cross_val_score(estimator = model, X = X_train, y = y_train, cv = kfold_cv)
        m_scores.append(kfold_scores.mean())
        s_scores.append(kfold_scores.std())
    
    titles = ['avg_score on K-fold-cross_validate', 'std_score on K-fold-cross_validate']
    all_scores = [m_scores, s_scores]
    
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 6))
    for k in range(2):
        ax[k].plot(kfold_range, all_scores[k])
        ax[k].set_title(titles[k])
        ax[k].set_xlabel('number of folds')

# /=================================================================================================\        
def Grid_search_values(X_train, y_train, X_test, y_test, alg, grid_params, cv_kfolds):
    """
        |==============================================================================================
        | Input :
        |    - alg (algorithm) : Base Estimator
        |    - X, y (n-darray) : your dataset and the target, dependence vrs
        |    - grid_params (dictionary): dictionary of the parameters in your algorithm
        |    - cv_kfolds (kFolds) : decide cross-validation or KFold
        |
        | Output: list of
        |    -  alg_name,
        |    -  best_params, 
        |    -  mean_score_kfold_train, 
        |    -  std_score_kfold_train, 
        |    -  test_score
        |***********************************************************************************************
        | Example.
        |-----------------------------------------------------------------------------------------------
        | >>> clf = ExtraTreesRegressor()
        | >>> clf = ExtraTreesRegressor()
        | >>> kfold_cv = KFold(n_splits = 10, shuffle = True, random_state = 53)
        | >>> parameters = {
        |          'n_estimators': [50, 100],
        |          'criterion' : ["squared_error", "absolute_error"],
        |          'max_depth': [10, 25],
        |          'bootstrap' : [True]
        |         }
        | >>> X_train, X_test, y_train, y_test = .... # your input
        | >>> Grid_search_values(X_train, y_train, X_test, y_test, clf, parameters, kfold_cv)
        | ('ExtraTreesRegressor',
        |   61.82580804824829,
        |   {'bootstrap': True,
        |    'criterion': 'squared_error',
        |    'max_depth': 10,
        |    'n_estimators': 100},
        |   0.8763147692459108,
        |   0.6009990632494777,
        |   0.7235208047826717,
        |   0.03781580513159189)
        |===============================================================================================
    """
    # Timing the train_fit 
    import time
    t0 = time.time()

    # get the algorithm name
    alg_name = alg.__class__.__name__
    
    # Train and fitting
    kfold_scores = cross_val_score(estimator = alg, X = X_train, y = y_train, cv = cv_kfolds)
    grid_clf = GridSearchCV(alg, param_grid = grid_params, cv = cv_kfolds)
    grid_clf.fit(X_train, y_train)
    mean_kfold_score = kfold_scores.mean()
    stdv_kfold_score = kfold_scores.std()
    fit_time = time.time() - t0
    mins = int(fit_time // 60)
    secs = np.round(fit_time - 60*mins, 2)
    fit_time = "{} mins {} seconds".format(mins, secs)
    
    train_score = grid_clf.score(X_train, y_train)
    test_score = grid_clf.score(X_test, y_test)
    best_params = grid_clf.best_params_
    
    train_shape = X_train.shape, X_test.shape   
    y_pred = grid_clf.predict(X_test)
    mape = MAPE(y_test, y_pred)
    mae = MAE(y_test, y_pred)
    rmse = RMSE(y_test, y_pred)
    mse = MSE(y_test, y_pred)
    corr = np.corrcoef(y_test, y_pred)[0, 1]
    
    return alg_name, train_shape, fit_time, best_params, stdv_kfold_score, train_score, test_score, mape, mae, mse, corr

# /=================================================================================================\
def split_data(data, cate_cols, test_size):
    """
        Parameters
            - data (dataframe)
            - cate_cols (list of columns) : columns name that contain the category
            - test_size (float) : size of the test-set.
            
        Returns
            - train_set, test_set
    """
    from sklearn.model_selection import train_test_split
    X = data.drop(columns = cate_cols)
    y = data[cate_cols]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify = y)
    df_train = pd.concat([X_train, y_train], axis = 1)
    df_test = pd.concat([X_test, y_test], axis = 1)
    
    return df_train, df_test

# /=================================================================================================\
#                                                 THE END.
# /=================================================================================================\
def test_predict(train_db, test_db, inp_col_names, tar_col, 
                 model_hyp, algorithm, imputed_by, constant,
                 *new_values):
    """
        This function
        Input parameters
            - train_db
            - test_db
            - inp_col_names
            - model_hyp, 
            - algorithm
            - *new_values = (area, status, nb_bedroom, nb_bathroom, age) depends on your input_model
        
    """
    train_db = train_db.drop_duplicates()
    test_db = test_db.drop_duplicates()
    
    X_train = train_db[inp_col_names], y_train = train_db[tar_col]    
    X_test = test_db[inp_col_names], y_test = test_db[tar_col]    
    
    # imputed method
    if imputed_by == 'median':
        X_train = X_train.fillna(X_train.median())
        X_test = X_test.fillna(X_test.median())
        
    elif imputed_by == 'mean':
        X_train = X_train.fillna(X_train.mean())
        X_test = X_test.fillna(X_test.mean())
        
    elif imputed_by == 'constant':
        X_train = X_train.fillna(constant)
        X_test = X_test.fillna(constant)
    
    # decide the model
    if model_hyp == 'linear':
        X_train, y_train = X_train, y_train
        X_test, y_test = X_test, y_test
        
    elif model_hyp == 'log2':
        y_train = np.log(y_train + 1) / np.log(2)
        y_test = np.log(y_test + 1) / np.log(2)
        
    elif model_hyp == 'log10':
        y_train = np.log(y_train + 1) / np.log(10)
        y_test = np.log(y_test + 1) / np.log(10)

    elif model_hyp == 'log':
        y_train = np.log(y_train + 1)
        y_test = np.log(y_test + 1)
