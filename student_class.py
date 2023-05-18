# A Python program to inheritance
class Student():

    def __init__(self, Stuname, Stuage,StuGrade):
        self.Stuname = Stuname
        self.Stuage = Stuage
        self.StuGrade=StuGrade

    def Display(self):
        print("Dislaying Given Student details from Student class")
        #print(self.Stuname, self.Stuage,self.StuGrade)
        print("Student name is '{}' with age '{}' got grade '{}'".format(self.Stuname, self.Stuage,self.StuGrade))


# # Driver code
# stu = Student("Satyam", 16, "B")
# stu.Display()


class School(Student):

    def SchoolStudentDisplay(self):
        print("Inherited Class School from Student")


school_details = School("Mayank", 15, "A")

# calling parent class function
school_details.SchoolStudentDisplay()

# Calling child class function
school_details.Display()