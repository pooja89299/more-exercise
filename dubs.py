 
def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("list that doesntco", num_list_sub_20) 



sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
print(sentence.split())




 
# words = "navgurukul is great"
# counter = 0
# a=[]
# while counter < len(words):
#     a.append(words[counter])
#     counter=counter+1 
# print(a)












# a = "my*name*is*python"
# print(a.split(" * " , 3))





# a = "Edureka is the biggest edtech company, it has many cutting edge courses to learn"
# b = "Sunday*Monday*Tuesday*Wednesday*Thursday*Friday*Saturday"
# print(a.split(" , "))
# print(b.split(" * "))




# a = "my name is python"
# b = "CatDogAntCarTap"
# c = "python was made by Guido van rossum"
# d = " this , will , be , in , output, this will be not"
# print(a.split())

# print([b[ i : i+3] for i in range(0 , len(b) , 3)])
 
# print(c.split(" #", 6))
 
# print(d.split(" , " , 4))



# a = "We are Edureka, we have cutting edge tutorials and certification programs to upskill your knowledge"
# print(a.split())