import os
import json
import pickle
import numpy as np
import pandas as pd


imputation_methods = ['carry_forward','forward_filling','zero_imputation','gaussian_process','linear_interpolation','indicator_imputation']


imputation_methods_json = {
        'carry_forward': 0,
        'forward_filling': 0,
        'zero_imputation': 0,
        'gaussian_process': 0,
        'linear_interpolation': 1,
        'indicator_imputation': 0,
        }
path_csv = f'./csv_data'
if not os.path.exists(path_csv):
        os.makedirs(path_csv)

for im in imputation_methods:
    if imputation_methods_json[im] == 1:
        path_data_or = f'./data/{im}'
        path_data_des = f'./csv_data/{im}'
        if not os.path.exists(path_data_des):
            os.makedirs(path_data_des)
        with open(f'./data/{im}/train_data', 'rb') as f:
            train_data = pickle.load(f)
        train_data_ML = train_data[1]
        train_data_etiqueta = train_data[2]
        pd.DataFrame(train_data_ML).to_csv(f'./csv_data/{im}/train_data_ML.csv')   
        pd.DataFrame(train_data_etiqueta).to_csv(f'./csv_data/{im}/train_data_etiqueta.csv')   

        with open(f'./data/{im}/test_data', 'rb') as f:
            test_data = pickle.load(f)
        test_data_ML = test_data[1]
        test_data_etiqueta = test_data[2]
        pd.DataFrame(test_data_ML).to_csv(f'./csv_data/{im}/test_data_ML.csv')   
        pd.DataFrame(test_data_etiqueta).to_csv(f'./csv_data/{im}/test_data_etiqueta.csv')   
        
        with open(f'./data/{im}/val_data', 'rb') as f:
            val_data = pickle.load(f)
        val_data_ML = val_data[1]
        val_data_etiqueta = val_data[2]
        pd.DataFrame(val_data_ML).to_csv(f'./csv_data/{im}/val_data_ML.csv')   
        pd.DataFrame(val_data_etiqueta).to_csv(f'./csv_data/{im}/val_data_etiqueta.csv') 


