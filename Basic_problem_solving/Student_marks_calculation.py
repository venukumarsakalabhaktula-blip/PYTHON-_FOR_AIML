# Student Marks Calculation

# Read marks of five subjects
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

# Calculate total
total = m1 + m2 + m3 + m4 + m5

# Calculate average
average = total / 5

# Calculate percentage
# (Assuming each subject is out of 100)
percentage = (total / 500) * 100

# Print results
print("\n----- Result -----")
print("Total Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")
