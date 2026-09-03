# #  modle9
# modle name = dictionary
# # coding exercises
# # Q 1


# # fruts = {"apple" : 100 , "mangoo" : 50 , "banana" : 30}
# # name = {"name" : "ali" , "hassan " : "ismail" }
# # fruts.update ({"apppppp" : 111111, "mangooooooooo" : 2222222 })
# # print(fruts)
# # print(type (fruts))

# # cars = {"BMW11" : "M5" , "BMW1" : "M4" , "BMW2" : 1983 , "BMW3" : "i7"}
# # countrys = {"karachi" : "NO 1" , "lahore" : "NO 2" , "islamabad" : "NO 3" ,}
# # print(cars["BMW11"])
# # # Q 2

# # fruts["fruts"] = "oringe"
# # fruts["banana"] = 1022
# # # Q3

# # print(fruts.get("karachiiiiiiiiiiiiiiiiiii"))      

# # # Q 4

# # print(fruts.keys())
# # print(fruts.values())

# # # Q 5

# # print(fruts.items())

# # for Fruts in fruts:
# #     print(fruts.items())


# # for keys , values in fruts:
# #     print(f"{keys}->{values}")

# # Q 6
# # apple = fruts.pop("apple")
# # print(fruts)
# # print(apple)

# # student = {"name" = "Ali", "age": 20} 
# # print(student) 
# # student = {"name" : "Ali", "age": 20}
# # print(student) 

# # Q 7

# # student = {
#     # "studentno1" : {"name" : "ismail" , "age" : 17  },
#     # "studentno2" : {"name" : "hizar" , "age" : 18  }
    
# # }
# # print(student["studentno1"]["name"])

# # Q 8

# student5 = {"name" : "hassan" , "age" : 11}
# student5.clear()
# print(student5)
# # debug 1
# # student = {"name": "Ali"} 
# # print(student["age"]) 

# # debug 2
# student = {"name": "Ali"}
# print(student.get("age")) 

# debug 3

# # student = {"name": "Ali", "age": 20} keys = student.keys()
# # print(keys[0]) 


# student = {"name": "Ali", "age": 20} 
# keys = student.keys() 
# print(keys) 


# mini assingmant
# employe

# Employee = {"name" : "ismail" , "department" : "googale" , "salry" : 10.00000 }
# print(f"Employee_dictionry: {Employee}")
# bonus_value = Employee.get("bonus,0")
# Employee.update({"salry" : 20.00000 , "tajurba" : "5 salll"})
# for  keys , value in Employee.items():
#     print (f"{keys} : {value}")
#     remove_fleid = Employee.pop("departmenyt")
#     print(f"")

# mini project

student = {
    "rollno01" :{"name" : "ismail" , "age" : 10 , "marks" : 100},
    "rollno02" :{"name" : "hizar" , "age" : 15 , "marks" : 99},
    "rollno03" :{"name" : "wasay" , "age" : 11 , "marks" : 15}
}

# print(["rollno1"])
# print(["rollno2"])
# print(["rollno3"])

numno01 = (input("enter your rolllno"))
name2 = (input ( "enter your name"))
age3 = int (input ("enter your age"))
marks4 = (input ("enter your marks"))

student.update({
    numno01:{
        "name" : name2,
        "age" : age3,
        "marks" :marks4,  
    }})

print("find a student")
serch_student = input ("enter your roll num to find a student /n")
serch_rollno = student.get(serch_student)
if serch_rollno == None:
    print("record not found")
else:
    print (F"{serch_rollno}")   
    
    
update_marks = input ("enter roll num to update marks")
if update_marks in student:
    update_number = input ("enter new number ")
    student[update_marks].update({"markes" : update_number})
    print(student[update_marks])
else:
    print("roll number not faound")   
     
# for loop descnary

for keys , value in student.items():
    print(keys ,"->" , value)
for keys , value in student["rollno01"].items():
    print(keys , "->" , value)    
    
    