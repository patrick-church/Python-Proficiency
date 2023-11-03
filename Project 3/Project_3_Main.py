from Project_3 import *

e = feature_extract('tortoise_tweets.txt', '@')
print(e)

t = feature_extract('tortoise_tweets.txt', '#')
print(t)

u = feature_extract('umbrella_tweets.txt', '@')
print(u)

c = feature_extract('umbrella_tweets.txt', '#')
print(c)

z = set(u.keys())
b = set(e.keys())
s = z.intersection(b)
print(s)

h = set(t.keys())
m = set(c.keys())
d = h.difference(m)
print(d)
