class Student():

    def __init__(self,name,heigth):
        self.name=name
        self.height=heigth

    def getname(self):
        return self.name

    def getheight(self):
        return  self.height

    def __str__(self):
        print("-------------------------------------")
        return "Name:"+self.name+ ", Heigtht:"+str(self.height)
list_student=[]
def add_student_record():
    name=input("Enter student name \n")
    height=input("Enter student height \n")
    list_student.append(Student(name,height))

def print_details():
    n=1
    for elements in list_student :
        print(str(n)+ ":"+str(elements))

def search_student():
    std_name=("Enter student name ")

def no_recorded():
    return "Number of students recorded : "+str(len(list_student))
op=0
while op!=4:
    print("Enter 1 to add student details")
    print("Enter 2 to print recorded student list")
    print("Enter 3 to see headcount")
    op=int(input())
    print("************************************")

    if op==1:
        add_student_record()
    elif op==2:
        print_details()
    elif op==3:
        print(no_recorded())
        print("-----------------------------------")
    else:
        exit()
