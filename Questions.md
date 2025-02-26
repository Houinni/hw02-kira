PART 1
1. Start by fitting a linear regression that models impact as a function of all other variables. 
                        OLS Regression Results                            
==============================================================================
Dep. Variable:                 impact   R-squared:                       0.578
Model:                            OLS   Adj. R-squared:                  0.526
Method:                 Least Squares   F-statistic:                     11.11
Date:                Tue, 25 Feb 2025   Prob (F-statistic):           1.77e-18
Time:                        22:39:33   Log-Likelihood:                -598.91
No. Observations:                 156   AIC:                             1234.
Df Residuals:                     138   BIC:                             1289.
Df Model:                          17                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
intercept         21.3248      4.391      4.856      0.000      12.642      30.007
posres             1.3377      2.165      0.618      0.538      -2.943       5.619
multi              5.2765      3.504      1.506      0.134      -1.651      12.204
clinend           13.7810      3.161      4.359      0.000       7.530      20.032
mech[K01]        -12.5754     12.598     -0.998      0.320     -37.485      12.334
mech[K23]        -13.3533     12.594     -1.060      0.291     -38.256      11.550
mech[P01]         -4.6003      9.276     -0.496      0.621     -22.942      13.741
mech[P50]         -1.0123     12.623     -0.080      0.936     -25.972      23.947
mech[R01]         -4.7608      3.870     -1.230      0.221     -12.412       2.891
mech[R18]         -7.5671     12.604     -0.600      0.549     -32.490      17.356
mech[R21]        -14.8721     12.674     -1.173      0.243     -39.932      10.188
mech[R24, K24]    -5.5038     12.600     -0.437      0.663     -30.417      19.409
mech[R44]         -2.0387      9.231     -0.221      0.826     -20.292      16.214
mech[U01]          5.9249      3.840      1.543      0.125      -1.669      13.518
mech[U54]          4.7060     12.707      0.370      0.712     -20.420      29.832
sampsize         6.55e-05      0.000      0.362      0.718      -0.000       0.000
budget            -0.0425      0.036     -1.196      0.234      -0.113       0.028
time              -0.3299      0.067     -4.903      0.000      -0.463      -0.197
==============================================================================
Omnibus:                        9.615   Durbin-Watson:                   1.847
Prob(Omnibus):                  0.008   Jarque-Bera (JB):                9.977
Skew:                           0.506   Prob(JB):                      0.00682
Kurtosis:                       3.714   Cond. No.                     1.41e+05
==============================================================================



2. Based on the summary of this model should you keep all of the predictors in the model? If not, which should you drop and why? 
No because there are some predictors that are not statistically significant by looking at their p value. Therefore, we should drop
predictors where the p-value is greater than 0.05. These include 'multi', 'mech', 'sampsize', 'posres' and 'budget'

3. If you decided to drop any predictors, fit a new model that does not include them and assess whether it is better than the original. 
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 impact   R-squared:                       0.475
Model:                            OLS   Adj. R-squared:                  0.468
Method:                 Least Squares   F-statistic:                     69.16
Date:                Tue, 25 Feb 2025   Prob (F-statistic):           4.02e-22
Time:                        23:14:42   Log-Likelihood:                -615.93
No. Observations:                 156   AIC:                             1238.
Df Residuals:                     153   BIC:                             1247.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
intercept     20.1241      2.141      9.401      0.000      15.895      24.353
clinend       19.0389      2.477      7.685      0.000      14.145      23.933
time          -0.3530      0.070     -5.078      0.000      -0.490      -0.216
==============================================================================
Omnibus:                       20.129   Durbin-Watson:                   1.741
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               24.313
Skew:                           0.830   Prob(JB):                     5.25e-06
Kurtosis:                       3.992   Cond. No.                         77.9
==============================================================================


The new model isn't any better than the first brcause the first model has an adjusted R-squared of 0.526, and the second model has a lower adjusted R-squared of 0.468.  

4. Next, take a look at the correlation between your variables. Do you see any issues? Which variables are most highly correlated? Investigate and describe the relationship between the two sets of highest correlated variables. 
           intercept    posres     multi   clinend  sampsize    budget      time
intercept        NaN       NaN       NaN       NaN       NaN       NaN       NaN
posres           NaN  1.000000 -0.242713 -0.347171 -0.232702 -0.177944  0.124236
multi            NaN -0.242713  1.000000  0.445261  0.181366  0.369388 -0.298522
clinend          NaN -0.347171  0.445261  1.000000  0.507468  0.345001 -0.400694
sampsize         NaN -0.232702  0.181366  0.507468  1.000000  0.594168 -0.231833
budget           NaN -0.177944  0.369388  0.345001  0.594168  1.000000 -0.198679
time             NaN  0.124236 -0.298522 -0.400694 -0.231833 -0.198679  1.000000

Some predictor pairs exhibit high correlations, potentially causing multicollinearity that obscures the distinct impact of each variable. In particular, the 'sampsize' and 'budget' variables show the strongest correlation (0.594168). This relationship is intuitive since experiments with larger sample sizes generally require higher budgets due to the increased costs associated with managing more participants. The second highest correlation is observed between 'clinend' and 'sampsize' (0.507468). This suggests that trials focusing on a clinical endpoint tend to involve larger sample sizes. This makes sense because studies designed to evaluate specific clinical outcomes usually require a broader range of participants to capture the necessary diversity.

5. Fit another linear regression model that includes all variables except for one in each pair of most highly correlated variables. How well does this model fit the data? How does this compare to your earlier models? 

Fitting a new regression model by removing one variable from each pair of highly correlated predictors yields mixed results:
Excluding just 'sampsize':
The adjusted R-squared increased slightly from 0.526 to 0.529, indicating a modest improvement in model fit.
Excluding both 'budget' and 'sampsize':
The adjusted R-squared remained essentially unchanged at 0.526, suggesting no improvement over the original model.
Excluding 'budget' and 'clinend':
The adjusted R-squared dropped significantly to 0.458, meaning the model’s explanatory power worsened.
Excluding 'clinend' and 'sampsize':
The adjusted R-squared further decreased to 0.454, indicating an even poorer fit.

In summary, while removing 'sampsize' alone provides a slight improvement over the original model, eliminating other combinations of predictors results in a noticeably poorer fit compared to earlier models.
model worse slightly: the adjusted R-squa


PART 2
Overall Model Summary:
                           Logit Regression Results                           
==============================================================================
Dep. Variable:      Punxsutawney Phil   No. Observations:                  115
Model:                          Logit   Df Residuals:                      112
Method:                           MLE   Df Model:                            2
Date:                Tue, 25 Feb 2025   Pseudo R-squ.:                 0.07100
Time:                        23:48:59   Log-Likelihood:                -41.368
converged:                       True   LL-Null:                       -44.529
Covariance Type:            nonrobust   LLR p-value:                   0.04235
================================================================================================
                                   coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------------------------
const                          -13.4326      5.097     -2.636      0.008     -23.422      -3.443
February Average Temperature     0.1793      0.096      1.872      0.061      -0.008       0.367
March Average Temperature        0.1258      0.099      1.273      0.203      -0.068       0.319
================================================================================================

Northeast Model Summary:
                           Logit Regression Results                           
==============================================================================
Dep. Variable:      Punxsutawney Phil   No. Observations:                  115
Model:                          Logit   Df Residuals:                      112
Method:                           MLE   Df Model:                            2
Date:                Tue, 25 Feb 2025   Pseudo R-squ.:                0.006570
Time:                        23:48:59   Log-Likelihood:                -44.237
converged:                       True   LL-Null:                       -44.529
Covariance Type:            nonrobust   LLR p-value:                    0.7464
============================================================================================================
                                               coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------------------------------------
const                                       -3.7030      2.552     -1.451      0.147      -8.705       1.299
February Average Temperature (Northeast)     0.0355      0.068      0.520      0.603      -0.098       0.169
March Average Temperature (Northeast)        0.0302      0.073      0.415      0.678      -0.112       0.173
============================================================================================================

Midwest Model Summary:
                           Logit Regression Results                           
==============================================================================
Dep. Variable:      Punxsutawney Phil   No. Observations:                  115
Model:                          Logit   Df Residuals:                      112
Method:                           MLE   Df Model:                            2
Date:                Tue, 25 Feb 2025   Pseudo R-squ.:                0.008016
Time:                        23:48:59   Log-Likelihood:                -44.172
converged:                       True   LL-Null:                       -44.529
Covariance Type:            nonrobust   LLR p-value:                    0.6998
==========================================================================================================
                                             coef    std err          z      P>|z|      [0.025      0.975]
----------------------------------------------------------------------------------------------------------
const                                     -4.0179      3.134     -1.282      0.200     -10.160       2.124
February Average Temperature (Midwest)     0.0477      0.062      0.771      0.441      -0.074       0.169
March Average Temperature (Midwest)        0.0124      0.062      0.201      0.841      -0.108       0.133
==========================================================================================================

Pennsylvania Model Summary:
                           Logit Regression Results                           
==============================================================================
Dep. Variable:      Punxsutawney Phil   No. Observations:                  115
Model:                          Logit   Df Residuals:                      112
Method:                           MLE   Df Model:                            2
Date:                Tue, 25 Feb 2025   Pseudo R-squ.:                0.003810
Time:                        23:48:59   Log-Likelihood:                -44.360
converged:                       True   LL-Null:                       -44.529
Covariance Type:            nonrobust   LLR p-value:                    0.8440
===============================================================================================================
                                                  coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------------------------
const                                          -3.2695      2.712     -1.205      0.228      -8.585       2.046
February Average Temperature (Pennsylvania)     0.0312      0.065      0.483      0.629      -0.095       0.158
March Average Temperature (Pennsylvania)        0.0147      0.066      0.221      0.825      -0.115       0.145
===============================================================================================================
6. What do your models tell you about Phil's predictions across various regions? Do you think Phil is good at his job of predicting spring?  
The Northeast, Midwest, and Pennsylvania models all exhibit very low pseudo R-squared values (0.006570, 0.008016, and 0.003810, respectively), indicating that these models explain only a minimal amount of the variability in the outcomes. Moreover, their high LLR p-values (0.7464, 0.6998, and 0.8440) suggest that these models are not significantly better than a null model with no predictors.

In contrast, the overall model has an LLR p-value of 0.04235, meaning that it is statistically significantly better than a null model and that the observed relationship is unlikely due to chance. This improvement may stem from the overall temperature measures effectively “smoothing out” the noise present in the regional data by capturing a broader trend.

However, even the overall model has a low pseudo R-squared value of 0.07100, similar to the regional models, which indicates that it still explains only a limited portion of the variation in the response variable. This limited explanatory power is further underscored by the imbalanced dataset, where the majority of observations correspond to 'Full Shadow', potentially biasing the model toward predicting that outcome.