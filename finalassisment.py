# school_name = "MHK Academy"
# total_marks = 300
# pass_percentage = 50
# subject_pass_marks = 40
 
# students = {
#     101: {"name": "  ali raza ",   "math": 78, "english": 65, "science": 82},
#     102: {"name": "SARA KHAN",     "math": 92, "english": 88, "science": 95},
#     103: {"name": "bilal ahmed  ", "math": 45, "english": 38, "science": 50},
#     104: {"name": "hina sheikh",   "math": 60, "english": 72, "science": 55}
# }
# # task 1 
# def clen_name(name):
#  return name.strip().title()

# # task 2
# def make_email(name):
#     return name.lower().replace(" " , ".")+"@mhk.com"
  
# # task 3
# def calulate_totel (m1 ,m2 ,m3):
#     return m1+m2+m3

# # task 4
# def calulate_paercentage (total , out_of):
#     return round(total / out_of * 100 , 1) 

# # task 5
# def get_grade(percentage):
#  if percentage > 90  and percentage < 100 :
#    return "A"
#  elif percentage > 80 and percentage < 90 :
#      return "B"
#  elif percentage > 70 and percentage < 80 :
#      return "C"
#  elif percentage > 60 and percentage < 70 :
#      return "D"
#  else:
#      return "fall"
    
# # task 6 
# def get_result (m1 , m2 , m3 , percentage):
#     if percentage >= pass_percentage and m1 >= subject_pass_marks and m2 >= subject_pass_marks and m3 >=subject_pass_marks
    
# # task 7
# def find_student(roll):
#  record = students.get(roll)
#  if record is None:
#   return "record not faund"
#  else: return (f"{record["name"]}: grede{get_grade()}")    
