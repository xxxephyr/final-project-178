# Hi
from ucimlrepo import fetch_ucirepo 
import numpy as np

# fetch dataset 
diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296) 

# data (as pandas dataframes) 
X = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets 

# for i in X:
#     column = eval(f"X.{i}")    #Each column has ID and Feature
#     #print(column)


print(X.shape)
print(y.shape)
# metadata 
#print(diabetes_130_us_hospitals_for_years_1999_2008.metadata) 
  
# variable information 
print(diabetes_130_us_hospitals_for_years_1999_2008.variables)
