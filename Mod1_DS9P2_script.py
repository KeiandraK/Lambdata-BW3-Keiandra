import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

causes_death=pd.read_csv('https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD')
causes_death.shape

causes_death.isnull().sum()
causes_death.head()

from sklearn.model_selection import train_test_split
train, test = train_test_split(causes_death, train_size=0.80, test_size=0.20, 
                              random_state=42)
                              
print(train.shape)
print(test.shape)