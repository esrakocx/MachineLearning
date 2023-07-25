import seaborn as sns

df = sns.load_dataset("car_crashes")

dict = {}
agg_list = ["mean", "min", "max", "var"]

# only numerical columns
num_cols = [col for col in df.columns if df[col].dtype != "O"]

for col in num_cols:
    dict[col] = agg_list

# short way
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()
df[num_cols].agg(new_dict)

