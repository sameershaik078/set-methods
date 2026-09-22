# Question 1: Unique Categories 
categories = ['A','B','A']

print(set(categories))

# Question 2: Add Category
category = {'A','B'}
category.add('C')
print(category)

# Question 3: Remove Category

category = {'A','B'}
category.remove('A')
print(category)

# Question 4: Common Skills

skill1= {'Python', 'SQL'}
skill2 = {'Excel', 'Python'}
common_skill = skill1.intersection(skill2)
print(common_skill)

# Question 5: All Skills
 
A = {'python'}
B = {'sql'}
print(A.union(B))

# Question 6: Only First Skills

frist = {'python','sql'}
second = {'sql'}
only_frist = frist.difference(second)
print(only_frist)

# Question 7: Exclusive Skills
skills1 = {'Python', 'SQL'}
skills2 = {'SQL', 'Excel'}
exclusive_skills = skills1.symmetric_difference(skills2)
print(exclusive_skills)

# Question 8: Membership Check
skills = {'A', 'B'}
value = 'A'
if value in skills:
    print('Present')
else:
    print('Absent')

# Question 9: Unique Regions
regions = ['south','north','south']
unique_regions = set(regions)
print(len(unique_regions))

# Question 10: Common Customers
customers1 = {1,2,3}
customers2 = {2,3,4}
common_customers = customers1.intersection(customers2)
print(common_customers)

# Question 11: New Customers
present = {1,2,3}
old = {2,3}
new_customers = present-old
print(new_customers)

# Question 12: Lost Customers
old = {2,3}
present = {1,2,3}
result = present - old 
print(result)

# Question 13: Exclusive Respondents
A = {1,2,3}
B = {3,4}
exclusive = A.symmetric_difference(B)
print(exclusive)

# Question 14: Category Coverage
A = {'A','B','C'}
B = {'A','B','C'}
if A.issubset(B):
    print("complete")
else:
    print("incomplete")  

# Question 15: Duplicate Detection
A = {1,2,3}
if len(set(A)) < len(A):

    print("duplicates")
else:
    print("no duplicates")   

# Question 16: Shared Locations
skill1 = {'delhi','hyderabad'}
skill2 = {'delhi','mumbai'}  
shared_locations = skill1.intersection(skill2)
print(shared_locations)   

# Question 17: Exclusive Products
A = {1,2,3}
B = {3,4}
Exclusive_products = A.symmetric_difference(B)
print(Exclusive_products)

# Question 18: Distinct Scores
scores = [80,90,80,70]
Distinct_scores = set(scores)
print(len(Distinct_scores))

# Question 19: Set Size After Addition
num = [1,2,1,3]
number_set = set()
for value in num:
    number_set.add(value)
print(len(number_set)) 

# Question 20: Common and Unique Sizes

set1 = {1, 2}
set2 = {2, 3}

common_size = len(set1.intersection(set2))
unique_size = len(set1.union(set2))

result = (common_size, unique_size)

print(result)