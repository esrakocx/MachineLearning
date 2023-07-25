# Before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# After:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns

""" Classical Solution
df = sns.load_dataset("car_crashes")

A = []

for col in df.columns:
    A.append(col.upper)

df.columns = A
"""

# With List Comprehensions
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]
print(df.columns)
