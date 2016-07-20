# -*- coding: utf-8 -*-

print map(lambda x:x*2,range(1,11))#让列表每个元素乘以2

print sum(range(1,1001))#求列表所有元素之和

wordlist=["scala","akka","play framework","sbt","type-safe"]#判断一个字符串中是否存在某些词
tweet="This is an example tweet talking about scala and sbt."
print map(lambda x:x in tweet.split(),wordlist)

print open("yee-haw.py").readlines()#读取文件

print map(lambda x:"Happy Birthday to "+("you" if x!=2 else "dear Name"),range(4))#祝你生日快乐

print reduce(lambda (a,b),c:(a+[c],b) if c>60 else (a,b+[c]),[49,58,76,82,88,90],([],[]))#过滤列表中的数值

#from xml.dom.minidom import parse,parseString#获取XML web service数据并分析
#import urllib2
#print parse(urllib2.urlopen("http://search.twitter.com/search.atom?&q=python")).toprettyxml(encoding="utf-8")

print min([14,35,-7,46,98])#找到列表中最小或最大的一个数字
print max([14,35,-7,46,98])

import multiprocessing#并行处理
import math
print list(multiprocessing.Pool(processes=4).map(math.exp,range(1,11)))

n=50#we want to find prime numbers between 2 and 50#"Sieve of Eratosthenes"算法
print sorted(set(range(2,n+1)).difference(set((p*f) for p in range(2,int(n**0.5)+2) for f in range(2,(n/p)+1))))