# Accept the marks of 5 subjects
m1 = input(" Enter the Marks of first subject: ")
m2 = input(" Enter the Marks of second subject: ")
m3 = input(" Enter the Marks of third subject: ")
m4 = input(" Enter the Marks of forth subject: ")
m5 = input(" Enter the Marks of fifth subject: ")

# Total Marks
Total = int(m1)+int(m2)+int(m3)+int(m4)+int(m5)

#Percentage:
Percentage = (Total/500)*100

#Print the Answer
print(' Percentage is {0} %'.format(Percentage))
