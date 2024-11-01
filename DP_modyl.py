grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron',}
gpa = float((sum(grades[0])) / len((grades[0])))
gpa1 = (sum(grades[1])) / len((grades[1]))
gpa2 = (sum(grades[2])) / len((grades[2]))
gpa3 = (sum(grades[3])) / len((grades[3]))
gpa4= (sum(grades[4])) / len((grades[4]))
res = sorted(students)
finih = {res[0]: gpa, res[1]: gpa1, res[2]: gpa2, res[3]: gpa3, res[4]: gpa4}
print(finih)
