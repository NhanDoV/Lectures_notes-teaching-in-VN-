import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold

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
            in_test_not_in_train = set(df_train[col].unique()) - set(df_train[col].unique())
            if len(in_test_not_in_train) > 0:
                data.loc[col, 'is_all-test_contained_in_train ?'] = False, in_test_not_in_train
            else:
                data.loc[col, 'is_all-test_contained_in_train ?'] = True

    return data


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
        | Example.
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
    X = (X - X.mean()) / X.std()
    y = data[target_col]

    return X, y

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
        | Example.
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

    X[x1_name] = np.log(X[x1_name] + c1)
    X[new_feat_name] = X[x2_name] / X[[x3_name, x4_name]].sum(axis=1)
    X[x2_name] = np.log(X[x2_name] + c2)
    X = (X - X.mean()) / X.std()
    y = np.log(y) / np.log(2)
    
    return X, y

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
    
    train_score = grid_clf.score(X_train, y_train)
    test_score = grid_clf.score(X_test, y_test)
    best_params = grid_clf.best_params_
    
    return alg_name, fit_time, best_params, train_score, test_score, mean_kfold_score, stdv_kfold_score
