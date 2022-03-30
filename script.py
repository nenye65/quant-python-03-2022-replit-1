#open read csv file
import pandas as pd
surveys_df = pd.read_csv('surveys.csv')
#describe weight column
weight = surveys_df['weight'].describe()
#print out summary statistics
print(weight)git