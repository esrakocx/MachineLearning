# Add FLAG to columns which contain INS in it

import seaborn as sns

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]