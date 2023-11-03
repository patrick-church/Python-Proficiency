import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Project_4 import *


vaccine = pd.read_csv('vaccine_data.csv', encoding = 'UTF8')
vaccine.columns = ['Region', 'Vaccine', 'Year', 'Percentage']
vaccine['Region'] = vaccine['Region'].str.replace('&','and').str.replace(' ','_')
vaccine['Year'] = vaccine['Year'].astype('str')

mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}

vaccine['Description'] = vaccine['Vaccine'].apply(lambda x: mappings[x])


BCG_2019 = make_subset(vaccine, vaccine = ['BCG'], year = ['2019'])
BCG2019_Series = BCG_2019.set_index('Region')
BCG2019_Series = BCG2019_Series['Percentage']
make_plot(BCG2019_Series)
DTP1_Years = make_subset(vaccine, region = ['East_Asia_and_Pacific'], vaccine = ['DTP1'])
DTP1_series = DTP1_Years.set_index('Year')
DTP1_series = DTP1_series['Percentage']
make_plot(DTP1_series, title = 'DTP1 Vaccinations by Year in East Asia and Pacific Region ', bar = False)
