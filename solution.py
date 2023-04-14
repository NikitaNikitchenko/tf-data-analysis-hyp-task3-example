
import pandas as pd
import numpy as np
from scipy.stats import  mannwhitneyu

chat_id = 784664358 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return mannwhitneyu(x, y, alternative='greater').pvalue < 0.09 # Ваш ответ, True или False
