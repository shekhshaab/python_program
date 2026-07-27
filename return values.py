#Return Multiple Values from Function

def student_details():
 name = "Amaan"
 age = 19
 course = "BCA"
 return name, age, course

# Receiving multiple values
n, a, c = student_details()
print("Name:", n)
print("Age:", a)
print("Course:", c)