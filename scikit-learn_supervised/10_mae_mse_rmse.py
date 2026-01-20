'''
MAE(Mean Absolute Error)
-take total mistake difference
-remove the minus sign
-add
-devide

MSE(Mean Squared Error)
-square each mistake value
-add all
-Take average


RMSE(Root Mean Squared Error) = sqrt(MSE)

'''

from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import math

act_val = [90,60,80,100]
pred_val = [85,70,70,95]

mae = mean_absolute_error(act_val,pred_val)
print(mae)

mse = mean_squared_error(act_val,pred_val)
print(mse)

rmse = math.sqrt(mse)
print(rmse)
