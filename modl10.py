# # # coding exersce

# # # Q 1

# # def average(num1, num2):
# #     return (num1 + num2) / 2
# # result = average(10, 20)
# # print(result)
# # print(average(60 , 40))
# # # Q 2
# # def python (a = 10  , b = 20, c =50):
# #     minus = a - b - c 
# #     print(minus)
# # python()   
    
    
# #     # Q 3
# # def max (*a):
# #     maxnumber = max(a)  
# #     print(maxnumber)  
# # max(60 , 30 ,70 ,100 ,555)

# # # Q 4
# # def studebt_info(**detalis):
# #     print(detalis)
# # studebt_info(name = "ismail", age = 10 , city = "karachi" )
    
# # # Q 5

# # cube = lambda a: a** 3
# # print(cube(2))

# # # Q 6

# # def sumofnumbers(numbers):
# #     if numbers == 0:
# #         return
# #     sumresult = 0
# #     sumresult += numbers
# #     print(sumresult)
# #     sumofnumbers(numbers - 1)
# # sumofnumbers(1)    
    
# def sum_tak(n):
#     if n <= 0:
#         return 0
#     return n + sum_tak(n - 1)

# number = 5
# print(f"1 se {number} tak ka sum: {sum_tak(number)}")


# # Q 7

# counters = 1 
# def updatecounter ():
#     global counters
#     counters += 1
# updatecounter()
# print(counters)