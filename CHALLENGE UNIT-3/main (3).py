class student:
     def __init__(self,name,roll_no,cgpa):
        self.name=name
        self.roll_no=roll_no
        self.cgpa=cgpa
def sort_students(student_list):
    sorted_students=sorted(student_list,
                              key=lambda student:student.cgpa,reverse=True)
    return sorted_students
print("\n\t\t\tSORTING THE LIST IN DESCENDING ORDER BASED ON cgpa")
print("\n\t\t\t********************************************************")
students=[student("GRACILIN","A1234",9.1),student("KALAI SELVI","A1235",8.9),student("SARANYA","A1236",9.2),student("HEMA","A1237",8.0)]
sorted_students=sort_students(students)
for student in sorted_students:
    print("NAME:{},ROLL_NO:{},CGPA:{}".format(student.name,student.roll_no,student.cgpa))