# Question 1: Get Student Mark
student = {'A':80,'b':70}
name = 'A'
if  name in student:
    print(student[name])
else:
    print("not found")

# Question 2: Add Product Price
product = {'pen':20}
product['book'] = 50
print(product)

# Question 3: Remove Employee
product = {'A':30000,'B':40000}
product.pop('A')
print(product)

# Question 4: Total Marks
product = {'A':80,'b':70}
total = sum(product.values())
print(total)

# Question 5: Average Marks
marks = {'A':80,'b':70}
average = sum(marks.values()) / len(marks)
print(average)

# Question 6: Count Passing Students
student = {'A':35,'B':70,'C':40}
count = 0
for i in student.values():
    if i >= 40:
        count += 1
print(count)    

# Question 7: Highest Mark Student
marks = {'A': 80, 'B': 95, 'C': 70}
highest = max(marks.values())
print(highest)

# Question 8: Lowest Price Product
marks = {'Pen': 20, 'Book': 50, 'Bag': 30}
lowest = min(marks.values())
print(lowest)

# Question 9: Count High Prices
price = {'A': 200, 'B': 600, 'C': 700}
count = 0
for i in price.values():
    if i >= 500:
        count += 1
print(count)        

# Question 10: Employee Department
employee = {'A': 'HR', 'B': 'IT'}
name = 'A'

if name in employee:
    print(employee[name])
else:
    print("Unknown")

# Question 11: Inventory Total
product = {'Pen': 10, 'Book': 5}
total = sum(product.values())
print(total)  

# Question 12: Count Zero Stock
zero = {'A': 0, 'B': 4, 'C': 0}
count = 0
for i in zero.values():
    if i == 0:
        count += 1
print(count)     

# Question 13: Filter Passing Students
students = {'A': 35, 'B': 70, 'C': 40}
result = {}
for name, mark in students.items():
    if mark >= 40:
        result[name] = mark
print(result)

# Question 14: Increase Prices
products = {'A': 20, 'B': 30}
result = {}
for name in products:
    result[name] = products[name] + 10
print(result)

# Question 15: Count Department
department = {'A': 'IT', 'B': 'HR', 'C': 'IT'}
count = 0
for i in department.values():
    if i == 'IT':
        count += 1    
print(count)    

# Question 16: Dictionary Entry Count
data = {'A': 1, 'B': 2}
count = 0
for key in data:
        count += 1
print(count)        

# Question 17: Total Product Sales
product = {'Pen': 100, 'Book': 250}
total = sum(product.values())
print(total)

# Question 18: Best-Selling Product
data = {'Pen': 100, 'Book': 250}
highest = max(data.values())
for product in data:
    if data [product] == highest:
        print(product)
        break
# Question 19: Customer Exists
data = {101: 'A', 102: 'B'}
customer_id = 101
if customer_id in data:
    print("Exists")
else:
    print("Missing")
# Question 20: Update Attendance
data = {'A': 70, 'B': 80}
student = 'A'
data[student] = data[student] + 5
print(data)