# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import preprocessing and clustering model
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv(
    r"C:\Users\HS TRADER\Desktop\internship tasks\test_Y3wMUE5_7gLdaTN.csv"
)

# Display first 5 rows
print(data.head())

# Display dataset information
print(data.info())

# Check missing values
print(data.isnull().sum())

# Fill missing categorical values using mode
data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)
data['Married'].fillna(data['Married'].mode()[0], inplace=True)
data['Dependents'].fillna(data['Dependents'].mode()[0], inplace=True)
data['Self_Employed'].fillna(data['Self_Employed'].mode()[0], inplace=True)
data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)

# Fill missing numerical values using median
data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)

# Visualize loan amount distribution
plt.figure(figsize=(8,5))
sns.histplot(data['LoanAmount'], bins=30, kde=True)
plt.title('Loan Amount Distribution')
plt.show()

# Visualize education count
plt.figure(figsize=(6,4))
sns.countplot(x='Education', data=data)
plt.title('Education Count')
plt.show()

# Visualize applicant income distribution
plt.figure(figsize=(8,5))
sns.histplot(data['ApplicantIncome'], bins=30, kde=True)
plt.title('Applicant Income Distribution')
plt.show()

# Convert categorical columns into numeric values
encoder = LabelEncoder()

columns = [
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area'
]

for col in columns:
    data[col] = encoder.fit_transform(data[col])

# Remove Loan_ID column because it is not useful for prediction
data.drop('Loan_ID', axis=1, inplace=True)

# Select all features
X = data

# Create KMeans clustering model
kmeans = KMeans(n_clusters=2, random_state=42)

# Create risk groups
data['Risk_Group'] = kmeans.fit_predict(X)

# Display some results
print(data[['ApplicantIncome', 'LoanAmount', 'Risk_Group']].head())

# Visualize risk groups
plt.figure(figsize=(8,5))

sns.scatterplot(
    x=data['ApplicantIncome'],
    y=data['LoanAmount'],
    hue=data['Risk_Group']
)

plt.title('Credit Risk Groups')
plt.show()

# Count applicants in each risk group
print(data['Risk_Group'].value_counts())