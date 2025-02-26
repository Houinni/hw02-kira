import pandas as pd
import statsmodels.api as sm

# Load and clean data: keep only rows with 'Full Shadow' or 'No Shadow' and drop missing values
phil_data = pd.read_csv('phil.csv')
phil_clean = phil_data[phil_data['Punxsutawney Phil'].isin(['Full Shadow', 'No Shadow'])].dropna()

# Create a binary outcome variable: 0 for 'Full Shadow' and 1 for 'No Shadow'
phil_clean['Punxsutawney Phil'] = (phil_clean['Punxsutawney Phil'] == 'No Shadow').astype(int)

# Define predictors for each region
predictors_overall = ['February Average Temperature', 'March Average Temperature']
predictors_ne = ['February Average Temperature (Northeast)', 'March Average Temperature (Northeast)']
predictors_mw = ['February Average Temperature (Midwest)', 'March Average Temperature (Midwest)']
predictors_pa = ['February Average Temperature (Pennsylvania)', 'March Average Temperature (Pennsylvania)']

# Add constant term to each predictor set
x_overall = sm.add_constant(phil_clean[predictors_overall])
x_ne = sm.add_constant(phil_clean[predictors_ne])
x_mw = sm.add_constant(phil_clean[predictors_mw])
x_pa = sm.add_constant(phil_clean[predictors_pa])

# Outcome variable
y = phil_clean['Punxsutawney Phil']

# Fit logistic regression models for each region
model_overall = sm.Logit(y, x_overall).fit()
model_ne = sm.Logit(y, x_ne).fit()
model_mw = sm.Logit(y, x_mw).fit()
model_pa = sm.Logit(y, x_pa).fit()

# Print model summaries
print("Overall Model Summary:")
print(model_overall.summary())

print("\nNortheast Model Summary:")
print(model_ne.summary())

print("\nMidwest Model Summary:")
print(model_mw.summary())

print("\nPennsylvania Model Summary:")
print(model_pa.summary())
