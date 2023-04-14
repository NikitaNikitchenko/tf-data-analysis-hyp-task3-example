
import pandas as pd
import numpy as np
from scipy.stats import  mannwhitneyu, permutation_test

chat_id = 784664358 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alternative = "greater"
    return permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis),
                                             vectorized=True,
                                             n_resamples=1000,
                                             alternative=alternative).pvalue < 0.09
