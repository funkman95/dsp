[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable `NUMKDHH` to construct the actual distribution for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in the household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use `chap03ex.ipynb`.

**Actual Distribution for the number of children under 18 in the household**  
![Actual](https://github.com/funkman95/dsp/blob/master/img/actual.png?raw=true)

**Actual vs. Biased Distribution for the number of children under 18 in the household**  
![Actual vs Biased](https://github.com/funkman95/dsp/blob/master/img/biased.png?raw=true)

Actual mean: 1.02420515504  
Biased mean: 2.40367910066

```Python
import nsfg
import thinkstats2 as ts
import thinkplot

df = nsfg.ReadFemResp()

pmf = ts.Pmf(df.numkdhh, label='numkdhh')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of children', ylabel='pmf')
thinkplot.SaveFormat('/Users/samfunk/ds/metis/metisgh/prework/dsp/img/actual', fmt='png')

def BiasPmf(pmf, label):
    bias = pmf.Copy(label=label)

    for val, p in pmf.Items():
        bias.Mult(val, val)

    bias.Normalize()
    return bias

bias_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, bias_pmf])
thinkplot.Config(xlabel='Number of children', ylabel='pmf')
thinkplot.SaveFormat('/Users/samfunk/ds/metis/metisgh/prework/dsp/img/biased', fmt='png')

print('Actual mean:', pmf.Mean())
print('Biased mean:', bias_pmf.Mean())
```
