import pandas as pd
url="http://zh.wikipedia.org/wiki/%E7%9C%81%E4%BC%9A"
dfs=pd.read_html(url, attrs={'class': 'wikitable'})
print dfs[0].head()