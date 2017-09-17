[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

>> On average, first babies are about 1.7% lighter than all other babies. Using Cohen's d, this difference is about 0.0887 standard deviations, which is a fairly small effect size.
The difference for pregnancy length is much smaller. First babies are 0.2% longer than all others, on average. The Cohen d is 0.0289 standard deviations, which a very small effect size.
The effect size for both variables are small and significant differences would be hard to detect.


```Python
import nsfg
from math import sqrt

df = nsfg.ReadFemPreg()

live = df[df.outcome == 1]
first = live[live.birthord == 1]
other = live[live.birthord != 1]

def CohenD(A, B):
    mean_A, mean_B = A.mean(), B.mean()
    var_A, var_B = A.var(), B.var()
    nA, nB = len(A), len(B)

    s = (nA * var_A + nB * var_B) / (nA + nB)
    d = abs(mean_A - mean_B) / sqrt(s)

    return d

print(first.totalwgt_lb.mean(), other.totalwgt_lb.mean())
print((other.totalwgt_lb.mean() - first.totalwgt_lb.mean()) / first.totalwgt_lb.mean())
print(CohenD(first.totalwgt_lb, other.totalwgt_lb))

print(first.prglngth.mean(), other.prglngth.mean())
print((first.prglngth.mean() - other.prglngth.mean()) / other.prglngth.mean())
print(CohenD(first.prglngth, other.prglngth))
```  
