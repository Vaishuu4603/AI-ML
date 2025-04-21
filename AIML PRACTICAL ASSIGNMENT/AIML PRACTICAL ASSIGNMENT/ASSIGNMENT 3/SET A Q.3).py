"""
Write a python program to implement Reshaping/Transform data- Conversion of 
Categorical values in Numeric format for a given dataset.( LabelEncoder or One –Hot 
Encoder).[use any dataset]
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Sample dataset (can be replaced with pd.read_csv())
data = {
    'Country': ['France', 'Spain', 'Germany', 'Spain', 'Germany', 'France'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    'Purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# ------------------- Label Encoding -------------------
label_encoder = LabelEncoder()

# Encode the 'Gender' column
df['Gender_Encoded'] = label_encoder.fit_transform(df['Gender'])
# Encode the 'Purchased' column
df['Purchased_Encoded'] = label_encoder.fit_transform(df['Purchased'])

print("\nAfter Label Encoding:\n", df)

# ------------------- One-Hot Encoding -------------------
# Apply OneHotEncoder to 'Country' column only
column_transformer = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(drop='first'), ['Country'])  # drop='first' to avoid dummy variable trap
    ],
    remainder='passthrough'  # Keep other columns as is
)

df_encoded = column_transformer.fit_transform(df[['Country', 'Gender_Encoded', 'Purchased_Encoded']])
df_encoded = pd.DataFrame(df_encoded, columns=['Germany', 'Spain', 'Gender_Encoded', 'Purchased_Encoded'])

print("\nAfter One-Hot Encoding:\n", df_encoded)
