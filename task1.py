import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList
belowFive = [elem for elem in ourList if elem < 5]
print(belowFive)
