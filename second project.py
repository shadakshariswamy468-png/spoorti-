def add_student():
    name=(input("Enter student name:"))
    marks=[]
    for i in range(3):
        mark=int(input("Enter subject {i+1} marks:"))
        marks.append(mark)
    total=sum(marks)
    percentage=total/3
    if all (mark>=35 for mark in marks):
        result="pass"
    else:   
        reasult = "fail"
    student={"name":name,"total":total,"percentage":percentage}  
    students.append(student)
    print("student add successfully!")
    
    def view_student():
        if not students:
            print("no student records founded")
        else:
           for student in students:
               print("\nName:" ,student["name"])
               print("Total:",student["total"])
               print("Percentage:" ,student["percentage"])
               print("Result:",student["result"])
while True:
    print("\n----Student Menu----" ) 
    print("1.Add student")   
    print("2.view students") 
    print("3.Exit") 
    choice=input("Enter choice:")
    if choice=="1":
          add_student()
    elif choice=="2":
           view_studnts()
    elif choice=="3":
            print("thank you!") 
            break;
    else:
            print("invalid choice") 
               

output 
----Student Menu----
1.Add student
2.view students
3.Exit
Enter choice: