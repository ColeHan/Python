
import re
f=open('baby2006.html', 'r')
txt = f.read()
print txt
names=[]

#get the year
years = re.findall(r'Popularity in (\d+)', txt)
if not:
names.append(years[0])
tuples = re.findall(r'<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', txt)
sorted
for id_tuple in tuples:
    (id, boyname, girlname) = id_tuple
    if boyname not in
print result
f.close()