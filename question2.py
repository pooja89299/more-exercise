# student=int(input("enter a number"))
# if student<=50:
#     print("hum budget ke ander hai")
# else:
#     print("hum budget ke bahar hai")



# Python implementation of above approach
def checkHarshad(n):
    
    # Converting integer to string
    st = str(n)
      
    # Initialising sum to 0
    sum = 0
    length = len(st)
  
    # Traversing through the string
    for i in st:
  
        # Converting character to int
        sum = sum + int(i)
          
    # Comparing number and sum
    if (n % sum == 0):
        return "True "
    else:
        return "False"
  
  
# Driver Code
number = 18
# passing this number to get result function
print(checkHarshad(number))