person={'name':'Divyansh',"age":16}

print("HEllo my name is "+ person['name']+" and i am "+str(person['age'])+" years old")

#above is a bad way of writing the formatting and we can use a better way to write this line

print("HEllo my name is {} and i am {} years old".format(person['name'],person['age']))
print("HEllo my name is {0} and i am {1} years old".format(person['name'],person['age']))

print("HEllo my name is {0[name]} and i am {0[age]} years old".format(person))

# here we placed the indexes of format column which one is need at which position
# which can also be used multiple times and as

print("{0}{1}{0}{1}".format(person["name"],person["age"]))


#another way is using f and writing the name of variable in the parenthesis

print(f"HEllo my name is {person["name"]} and i am {person["age"]} years old")



for i in range(1,11):
    sentence=("the value of i is {:03}".format(i))
    print(sentence)

pi=3.142857
print("value of pi in two decimals is {:.2f}".format(pi))    
print("value of pi in three decimals is {:.3f}".format(pi))    #it also rounds off  the value


sentence_2="1 mb is equal to {:,}".format(10**8)
print(sentence_2)


import datetime
my_date=datetime.datetime(2024,6,5,18,37,45)
print(my_date)


#also another date format is using formatting in that above written date

sem="{:%B %d %Y}".format(my_date)
print(sem)

# if you want to display anything in  any format then look for the documentation and place it right there