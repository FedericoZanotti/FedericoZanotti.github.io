import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression, ARDRegression, BayesianRidge, ElasticNet, \
Hinge,Lasso, Ridge, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.svm import SVC, SVR, LinearSVR
import itertools
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score

import warnings
warnings.filterwarnings('ignore')

def get_round(ar, original_shape,treshold_dict):
  res=[]
  if len(ar.shape)==1:
    ar=np.round(ar,1)
    dec = np.round(ar%1,1)
    for i in range(ar.shape[0]):
      int_part = int(ar[i])
      t = treshold_dict[int_part]
      if dec[i]>=t:
          res.append(ar[i]+ (1-dec[i]))
      else:
          res.append(ar[i] - dec[i])
  else:
    ar=np.round(ar,1)
    for i in range(ar.shape[0]):
      dec = np.round(ar[i]%1,1)
      for j in range(ar[i].shape[0]):
        int_part = int(ar[i][j])
        t = treshold_dict[int_part]
        if dec[j]>=t:
            res.append(ar[i][j]+ (1-dec[j]))
        else:
            res.append(ar[i][j] - dec[j])
    
  res = np.asarray(res)
  return res.reshape(original_shape)


def my_accuracy(y_pred, y_true, treshold):
  y_pred_rounded = get_round(y_pred, y_pred.shape, treshold)
  ar=y_pred_rounded-y_true
  tot=(ar==0).sum(axis=0).sum()
  if len(y_true.shape)==1:
    return (tot/y_true.shape[0])*100, \
    np.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))
  else:
    return (tot/(y_true.shape[0]*y_true.shape[1]))*100, \
     np.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))
     
def my_accuracy_old(y_pred, y_true):
  ar=np.round(y_pred)-np.round(y_true)
  tot=(ar==0).sum(axis=0).sum()
  if len(y_true.shape)==1:
    return (tot/y_true.shape[0])*100, \
    np.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))
  else:
    return (tot/(y_true.shape[0]*y_true.shape[1]))*100, \
     np.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))

  
  

def data_prep(df, cf):
 
    
  #### Dishonest and honest numpy array #####

  df_array=df.iloc[:, :cf].to_numpy()
  df_array_1=df_array[225:,:]
  dishonest = df_array_1.astype("float32")


  df_array_2=df_array[:225]
  honest = df_array_2.astype("float32")
  honest.shape

  #### DataFrame honest and dishonest ####

  df_honest=df.iloc[:225,0:cf]
  df_dishonest=df.iloc[225:,0:cf]

  #### Standardize if needed ####

  from sklearn.preprocessing import MinMaxScaler
  t = MinMaxScaler(feature_range=(0,1))

  t.fit(df_array)

  dishonest_std= t.transform(dishonest.astype("float32"))
  honest_std = t.transform(honest.astype("float32"))
  X_train_r, y_train_r = dishonest[:160], honest[:160]
  X_test_r, y_test_r = dishonest[160:], honest[160:]
 

  return dishonest, honest, df_honest, df_dishonest, X_train_r, y_train_r, X_test_r, y_test_r

def create_structure(X_train, X_test, y_train, y_test, LIGHT, treshold_dict):

  result= {}
  all_dict = {}
  dict_for_models={}

  model_list = [XGBRegressor(objective ='reg:squarederror'),ExtraTreeRegressor(), \
                SVC(), SVR(), LinearRegression(), Ridge(), SGDRegressor(), Lasso(), ARDRegression(), \
                BayesianRidge(), KNeighborsRegressor(), LinearSVR(), DecisionTreeRegressor()]


  model_list_light=[ LinearRegression(), KNeighborsRegressor(), DecisionTreeRegressor()]
  if LIGHT:
    model_list = model_list_light
  model_list_str = [str(el) for el in model_list]
  l=list(range(X_train.shape[1]))
  print(l)
  for m in model_list:
    print("computing for model ", str(m))
    all_dict={}
    for k in range(y_train.shape[1]):
      print("-"*10)
      print("computing for column: ", k)
      result={}
      scores_dict={}
      for i in range(1,X_train.shape[1]):
        comb = list(itertools.combinations(l, i))
        for j in range(len(comb)):
          model = m
          cl=list(comb[j])
          model.fit(X_train[:,cl], y_train[:,k])
          y_pred = model.predict(X_test[:, cl])
          y_pred=np.clip(y_pred, 0,4)
          result[str(comb[j])] = my_accuracy(y_pred, y_test[:,k], treshold_dict)
      all_dict[k] = result

    dict_for_models[m]=all_dict

  return dict_for_models
    
    


def get_max(d, flag_max=True):
    
  max_values_acc={}
  min_values_mse={}
  max_values_ALL = {}
  min_values_ALL = {}
  best_model = ''
  res_max = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
  res_min = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
  
  if flag_max:
    maximum = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    minimum = [100,100,100,100,100,100,100,100,100]
  else: 
    maximum = [100,100,100,100,100,100,100,100,100]
    minimum = [100,100,100,100,100,100,100,100,100]


  for k1,v1 in d.items():
    max_values_acc={}
    min_values_mse={}
    for k, v in d[k1].items():
      if flag_max: 
        mx=max(v.values(), key=lambda x: x[0]) 
      else: 
        mx=min(v.values(), key=lambda x: x[0])
      mn=min(v.values(), key=lambda x: x[1])
      k_mx = list(d[k1][k].keys())[list(d[k1][k].values()).index(mx)]
      k_mn = list(d[k1][k].keys())[list(d[k1][k].values()).index(mn)]
      if flag_max:
        if mx[0] >= maximum[k]:
          maximum[k] = mx[0]
          best_model = k1
          res_max[k]=(best_model, maximum[k], k_mx)
      else:
        if mx[0] <= maximum[k]:
          maximum[k] = mx[0]
          best_model = k1
          res_max[k]=(best_model, maximum[k], minimum[k], k_mx)
      if mn[1] <= minimum[k]:
        minimum[k] = mn[1]
        best_model = k1
        res_min[k]=(best_model, minimum[k], maximum[k], k_mn)

      

      max_values_acc[k] = (mx, k_mx)
      min_values_mse[k] = (mn, k_mn)
    
    max_values_ALL[k1]=max_values_acc
    min_values_ALL[k1]=min_values_mse
  return res_max, res_min

