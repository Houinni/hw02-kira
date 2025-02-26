import numpy as np
from ISLP import load_data

import statsmodels.api as sm

from statsmodels.stats.outliers_influence \
import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm

from ISLP.models import (ModelSpec as MS,
summarize,
poly)

def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs)

publication = load_data('Publication')
newPublication = publication[publication['status'] == 1]  # Filter the dataset to only clinical trials that have been published
newPublication['mech'] = newPublication['mech'].cat.remove_unused_categories() # Remove used category

x1 = MS(['posres', 'multi', 'clinend', 'mech', 'sampsize', 'budget','time']).fit_transform(newPublication)
y = newPublication['impact']

model1 = sm.OLS(y, x1)
results1 = model1.fit()

# print(results1.summary())

x2 = MS(['clinend', 'time']).fit_transform(newPublication)

model2 = sm.OLS(y,x2)
results2 = model2.fit()

#print(results2.summary())

corr = MS(['posres', 'multi', 'clinend', 'sampsize', 'budget', 'time']).fit_transform(newPublication) 
corr_matrix = corr.corr()
#print(corr_matrix)

x3 = MS(['posres', 'multi', 'mech', 'budget','time']).fit_transform(newPublication)
model3 = sm.OLS(y,x3)
results3 = model3.fit()
print(results3.summary())
