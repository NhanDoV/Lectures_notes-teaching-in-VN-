import pandas as pd
import numpy as np

def email_mapper(user_df):
    coded_dict = dict()
    cter = 1
    email_encoded = []
    
    for val in user_df['email']:
        if val not in coded_dict:
            coded_dict[val] = cter
            cter+=1
        
        email_encoded.append(coded_dict[val])
    return email_encoded

def create_user_item_matrix(df):
    '''
    INPUT:
    df - pandas dataframe with article_id, title, user_id columns
    
    OUTPUT:
    user_item - user item matrix 
    
    Description:
    Return a matrix with user ids as rows and article ids on the columns with 1 values where a user interacted with 
    an article and a 0 otherwise
    '''
    # Fill in the function here
    user_article_idx = df.groupby(by=['user_id', 'article_id']).agg(lambda x: 1)
    user_article_mtx = user_article_idx.unstack()
    user_item = user_article_mtx.fillna(0)
    
    return user_item # return the user_item matrix 

def find_similar_users(user_id, user_item, users):
    '''
    INPUT:
    user_id - (int) a user_id
    user_item - (pandas dataframe) matrix of users by articles: 
                1's when a user has interacted with an article, 0 otherwise
    
    OUTPUT:
    similar_users - (list) an ordered list where the closest users (largest dot product users)
                    are listed first
    
    Description:
    Computes the similarity of every pair of users based on the dot product
    Returns an ordered
    
    '''
    # initialize the similarity
    sims = []
    
    # Loop through each users
    for user in user_item.index:
        sims.append(np.dot(user_item.loc[user_id, :], user_item.loc[user, :]))

    dfs = pd.DataFrame({'user': users,
                       'similarity': sims
                       })    

    dfs = dfs.sort_values(by = ['similarity', 'user'], 
                          ascending = [False, True]
                         )
    most_similar_users = [val for val in dfs['user'].values]
    
    # Remove
    most_similar_users.remove(user_id)
    
    return most_similar_users # return a list of the users in order from most to least similar

def get_article_names(article_ids, df):
    '''
    INPUT:
    article_ids - (list) a list of article ids
    df - (pandas dataframe) df as defined at the top of the notebook
    
    OUTPUT:
    article_names - (list) a list of article names associated with the list of article ids 
                    (this is identified by the title column)
    '''
    article_names = [df[df['article_id'] == float(idx)]['title'].values[0] for idx in article_ids]
    
    return article_names # Return the article names associated with list of article ids

def get_user_articles(user_id, user_item):
    '''
    INPUT:
    user_id - (int) a user id
    user_item - (pandas dataframe) matrix of users by articles: 
                1's when a user has interacted with an article, 0 otherwise
    
    OUTPUT:
    article_ids - (list) a list of the article ids seen by the user
    article_names - (list) a list of article names associated with the list of article ids 
                    (this is identified by the doc_full_name column in df_content)
    
    Description:
    Provides a list of the article_ids and article titles that have been seen by a user
    '''
    article_ids = [str(idx) for idx in list(user_item.loc[user_id][user_item.loc[user_id]==1].title.index)]
    article_names = get_article_names(article_ids)  # recalled article_names from the previous function
    
    return article_ids, article_names # return the ids and names

def user_user_recs(user_id, the_user_articles, m = 10):
    '''
    INPUT:
    user_id - (int) a user id
    m - (int) the number of recommendations you want for the user
    
    OUTPUT:
    recs - (list) a list of recommendations for the user
    
    Description:
        Loops through the users based on closeness to the input user_id
        For each user - finds articles the user hasn't seen before and provides them as recs
        Does this until m recommendations are found

        Notes:
        Users who are the same closeness are chosen arbitrarily as the 'next' user

        For the user where the number of recommended articles starts below m 
            and ends exceeding m, the last items are chosen arbitrarily
    '''
    # Your code here
    the_most_similar_users = find_similar_users(user_id)  # recall the most_similar_users
    user_articles, article_names = get_user_articles(user_id) # called the user_articles & aricle_names
    # Loops through the users based on closeness to the input user_id
    for user in the_most_similar_users:
        article_ids, article_names = get_user_articles(user)
        recs = [idx for idx in article_ids if idx not in user_articles]
        if len(recs) >= m:
            break
    if len(recs) < m:
        recs = [idx for idx in str(df['article_id']) if idx not in the_user_articles]    
    return recs[: m] # return your recommendations for this user_id    

def get_top_sorted_users(user_id, df, user_item):
    '''
    INPUT:
    user_id - (int)
    df - (pandas dataframe) df as defined at the top of the notebook 
    user_item - (pandas dataframe) matrix of users by articles: 
            1's when a user has interacted with an article, 0 otherwise
    
            
    OUTPUT:
    neighbors_df - (pandas dataframe) a dataframe with:
                    neighbor_id - is a neighbor user_id
                    similarity - measure of the similarity of each user to the provided user_id
                    num_interactions - the number of articles viewed by the user - if a u
                    
    Other Details - sort the neighbors_df by the similarity and then by number of interactions where 
                    highest of each is higher in the dataframe
     
    '''
    users = []
    sims = []
    nb_intact = []
    for user in user_item.index:
        if user == user_id:
            continue
        users.append(user)  
        sims.append(np.dot(user_item.loc[user_id, :], user_item.loc[user, :])) 
        nb_intact.append(df[df['user_id'] == user]['article_id'].count())
    neighbors_df = pd.DataFrame({'neighbor_id': users, 
                                 'similarity': sims, 
                                 'num_interactions': nb_intact})
    
    neighbors_df.sort_values(by = ['similarity', 'num_interactions'], 
                             ascending = [False, True], 
                             inplace = True)

    return neighbors_df

def get_top_articles(n, df):
    '''
    INPUT:
    n - (int) the number of top articles to return
    df - (pandas dataframe) df as defined at the top of the notebook 
    
    OUTPUT:
    top_articles - (list) A list of the top 'n' article titles 
    
    '''
    # Your code here
    draft = df.groupby(by='title').count().sort_values(by='user_id', ascending=False)
    top_articles = list(draft.head(n).index)
    
    return top_articles # Return the top article titles from df (not df_content)

def get_top_article_ids(n, df):
    '''
    INPUT:
    n - (int) the number of top articles to return
    df - (pandas dataframe) df as defined at the top of the notebook 
    
    OUTPUT:
    top_articles - (list) A list of the top 'n' article titles 
    
    '''
    # Your code here
    draft = df.groupby(by='article_id').count().sort_values(by='user_id', ascending=False)
    top_articles = list(draft.head(n).index)
    
    return top_articles # Return the top article ids

def user_user_recs_part2(user_id, m = 10):
    '''
    INPUT:
    user_id - (int) a user id
    m - (int) the number of recommendations you want for the user
    
    OUTPUT:
    recs - (list) a list of recommendations for the user by article id
    rec_names - (list) a list of recommendations for the user by article title
    
    Description:
    Loops through the users based on closeness to the input user_id
    For each user - finds articles the user hasn't seen before and provides them as recs
    Does this until m recommendations are found
    
    Notes:
    * Choose the users that have the most total article interactions 
    before choosing those with fewer article interactions.

    * Choose articles with the articles with the most total interactions 
    before choosing those with fewer total interactions. 
   
    '''
    neighbors_df = get_top_sorted_users(user_id)
    user_articles, article_names = get_user_articles(user_id)
    for user in neighbors_df['neighbor_id']:
        article_ids, article_names = get_user_articles(user)
        recs = [idx for idx in article_ids if idx not in user_articles] 
        if len(recs) >= m:
            break
    idx_str = [str(id) for id in get_top_article_ids(100)]
    if len(recs) < m:
        recs = [idx for idx in idx_str if idx not in user_articles]
    rec_names = get_article_names(recs)[: m]
    
    return recs, rec_names