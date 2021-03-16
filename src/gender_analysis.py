from scipy.stats import binom_test
import pandas as pd
import numpy as np
from functools import reduce

df = pd.read_csv('results/science-awardees.tsv', sep='\t').drop_duplicates()
df_pivot = df.pivot_table(index=['AWARD', 'DESCRIPTION'], values='DATE', columns=['GENDER'], aggfunc='count').fillna(0)
df_pivot['p_value'] = df_pivot.apply(lambda row: binom_test(row['female'], row['female']+row['male'], p=0.5, alternative='less'), axis=1)
print(df_pivot)
df_pivot.to_csv('bio-awards-summary.tsv', sep='\t')
df_persons = df.groupby(['AWARD', 'DESCRIPTION']).agg({'PERSON': lambda x: ('; '.join(x))[0:1000]})
df_mindate = df.groupby(['AWARD', 'DESCRIPTION']).agg({'DATE': 'min'}).rename(columns={'DATE': 'start_date'})
df_maxdate = df.groupby(['AWARD', 'DESCRIPTION']).agg({'DATE': 'max'}).rename(columns={'DATE': 'end_date'})
dfs = [df_pivot, df_mindate, df_maxdate, df_persons]
#dfs = [df_pivot, df_mindate, df_maxdate]
df = reduce(lambda left,right: pd.merge(left,right,on=['AWARD', 'DESCRIPTION']), dfs)
print(df)
df.to_csv('results/science-awards-summary.tsv', sep='\t')
