# Capitalize all letters of the given string expression. Put space instead of comma, separate them word by word.

text = "The goal is to turn data into information, and information into insight."
new_text = text.upper()
list1 = new_text.split()
print(list1)

"""
Step1: See the number of elements in the given list. 
Step2: Call the elements in the zeroth and tenth index. 
Step3: Create a list["D", "A", "T", "A"] from the given list. 
Step4: Delete the element in the eighth index.
Step5: Add a new element. 
Step6: Add element "N" again to the eighth index.
"""

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step1
element_num = len(lst)
print(element_num)

# Step2
print(lst[0], lst[10])

# Step3
new_lst = lst[0:4]
print(new_lst)

# Step4
lst.remove(lst[8])
print(lst)

# Step5
lst.append("X")
print(lst)

# Step6
lst.insert(8, "N")
print(lst)

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

"""
Step1: Access the key values. 
Step2: Access the values. 
Step3: Update the value 12 of the Daisy key to 13. 
Step4: Add a new value whose Key value is the value of Ahmet [Turkey,24]. 
Step5: Delete Antonio from the dictionary.
"""

# Step1 & Step2
print(dict.keys())
print((dict.values()))

# Step3
dict['Daisy'] = ["England", 13]
print(dict)

# Step4
new_key = 'Ahmet'
new_value = ["Turkiye", 24]
dict[new_key] = new_value
print(dict)

del dict['Antonio']
print(dict)

# Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns those lists.
def func(list1):

    even_list = []
    odd_list = []

    for i in range(0, len(list1)):
        if list1[i] % 2 == 0:
            even_list.append(list1[i])
        else:
            odd_list.append(list1[i])

    return even_list, odd_list


l = [2, 13, 18, 93, 22]
print(func(l))

# In the list given below are the names of the students who received degrees in engineering and medicine faculties. Respectively, the first three students represent the success rank of the engineering faculty, while the last three students belong to the rank of the medical faculty. Print the student's degrees specific to the faculty using Enumarate.

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
engineering = students[:3]
medicine = students[-3:]
for index, student in enumerate(engineering, start=1):
    print(f"Engineering Faculty {index}. Student: {student}")

for index, student in enumerate(medicine, start=1):
    print(f"Medicine Faculty {index}. Student: {student}")

# Three lists are given below. In the lists, there is a course code, credit and quota information, respectively. Print course information using zip.

lesson_code = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

new_list = list(zip(credit, lesson_code, quota))
print(new_list)

for i, j, k in new_list:
    print(f"Kredisi {i} olan {j} kodlu dersin kontenjanı {k} kişidir.")

# Below are 2 sets. What is requested from you is that if the 1st cluster includes the 2nd cluster, then the common elements of the 2nd cluster1 if it does not. You are expected to define the function that will print the difference from the set.

cluster1 = set(["data", "python"])
cluster2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if cluster1.issuperset(cluster2):
    print(cluster1.intersection(cluster2))
else:
    print(cluster2.difference(cluster1))

# Using the List Comprehension structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.

import seaborn as sns
df = sns.load_dataset("car_crashes")

num_col = ["NUM_" + col.upper() for col in df.columns if df[col].dtype != "0"]
print(num_col)

# Using the List Comprehension structure, write "FLAG" after the names of the variables that do not contain "number" in their names in the car_crashes data.

without_no = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
print(without_no)

# Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new data frame.

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df)
