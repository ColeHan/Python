# coding: utf-8 

import pandas as pd
import numpy as np

ds = [{'one' : 4,'two':2},{'one' : 5,'two' : 3},{'one' : 6,'two' : 4},{'two' : 7,'three':10}]
dfs = pd.DataFrame(ds,index=['e','f','g','h'])
##构建一个新的DataFrame，dfs
df_t=pd.concat([ds,dfs])#合并两个DataFrame
print df_t