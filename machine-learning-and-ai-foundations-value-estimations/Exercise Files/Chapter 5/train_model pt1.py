import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
# from sklearn.externals import joblib

# Load the data set
df = pd.read_csv("ml_house_data_set.csv")
print(df.head(1))
# Remove the fields from the data set that we don't want to include in our model
df.drop(['house_number', 'unit_number', 'street_name', 'zip_code'], axis=1, inplace=True)
print(df.head(1))

# Replace categorical data with one-hot encoded data
features_df = pd.get_dummies(df, columns=['garage_type', 'city'])
print(features_df.head(1))
#
# # Remove the sale price from the feature data

features_df.drop(['sale_price'], axis=1, inplace=True)
print(features_df.head(1))

# # Create the X and y arrays
X = features_df.to_numpy()
y = df['sale_price'].to_numpy()
