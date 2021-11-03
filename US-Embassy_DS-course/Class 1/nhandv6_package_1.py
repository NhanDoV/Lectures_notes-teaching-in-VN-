def load_data(data, fill_vl = None, 
              target_col = 'price', 
              inp_col_names = ['age', 'area', 'nb_bedroom', 'nb_bathroom']):
    """
        |=====================================================================================================
        | This function is used to load dataset and impute the missing values, also drop the duplicates values
        | Input
        |    data (dataframe) : data to load
        |    fill_vl (str or None): which values filled in the missing place
        |    target_col (column name) : column of the target in your model.
        |    inp_col_names (column names): input column names
        | Output
        |    cleaned data and its target.    
        |======================================================================================================
        | Example.
        |******************************************************************************************************
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
        |********************************************************************************************************
    """
    data = data.drop_duplicates()
    X = data[inp_col_names]
    if fill_vl == None:
        fill_vl = X.mean()
        X = X.fillna(fill_vl)
    else:
        X = X.fillna(fill_vl)
    X = (X - X.mean()) / X.std()
    y = data[target_col]

    return X, y

def load_data2(data, c1 = 1, c2 = 100):
    """
    
    """
    data = data.drop_duplicates()
    X = data[['age', 'area', 'nb_bedroom', 'nb_bathroom']]
    y = data['price']
    X = X.fillna(fill_vl)

    X['age'] = np.log(X['age'] + c1)
    X['area_p_rm'] = X['area'] / X[['nb_bedroom', 'nb_bathroom']].sum(axis=1)
    X['area'] = np.log(X['area'] + c2)
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
    kfold_scores = cross_val_score(estimator = clf, X = X_train, y = y_train, cv = cv_kfolds)
    grid_clf = GridSearchCV(alg, param_grid = parameters, cv = cv_kfolds)
    grid_clf.fit(X_train, y_train)
    mean_kfold_score = kfold_scores.mean()
    stdv_kfold_score = kfold_scores.std()
    fit_time = time.time() - t0
    
    train_score = grid_clf.score(X_train, y_train)
    test_score = grid_clf.score(X_test, y_test)
    best_params = grid_clf.best_params_
    
    return alg_name, fit_time, best_params, train_score, test_score, mean_kfold_score, stdv_kfold_score
