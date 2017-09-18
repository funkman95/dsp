[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> In the BRFSS the distribution of heights is roughly normal with parameters mu = 178 cm and sigma = 7.7 cm for men, and mu = 163 cm and sigma = 7.3 cm for women. In order to join Blue Man Group, you have to be male between 5'10" and 6'1". What percentage of the U.S. male population is in this range? Hint: use `scipy.stats.norm.cdf`.  

N(mu, sigma): (low, high, high - low)
population: (48.964, 83.238, 34.275)  
sample: (48.625, 82.948, 34.323)  

Assuming the distribution of heights for U.S. men is normally distributed with an average (mu) height of 178 cm and a standard deviation (sigma) of 7.7 cm, 48.964% of all men are at most 5'10" and 83.238% of all men at most 6'1". Taking the difference of these two subsets, 34.275% of all U.S. men fall between 5'10" and 6'1" and are therefore eligible to join the Blue Man Group. Using the BRFSS data, the CDF is almost identical to the one that uses the normally distributed population mu and sigma.

```Python
import brfss
import scipy.stats as stats

df = brfss.ReadBrfss()

spread = [(5,10), (6,1)]
height = []
for i in spread:
    cm = (i[0]*12 + i[1]) * 2.54
    height.append(round(cm,2))

mu, sigma = 178, 7.7
dist = stats.norm(loc=mu, scale=sigma)
low = 100*dist.cdf(height[0])
high = 100*dist.cdf(height[1])
print('population:', (low, high, high - low))

men = df[df.sex == 1]
xbar = men.htm3.mean()
s = men.htm3.std()
sdist = stats.norm(loc=xbar, scale=s)
low = 100*sdist.cdf(height[0])
high = 100*sdist.cdf(height[1])
print('sample:', (low, high, high - low))
```
