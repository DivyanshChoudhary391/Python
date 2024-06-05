welcome="Hello world"

print(welcome.lower())
print(welcome.count("Hello"))  #how many times this substring appers in the string
print(welcome.count("l"))  #same as above
print(welcome.find('w')) #gives the index of word w in the string 
print(welcome.find('world')) #gives the index of word world in the string 
print(welcome.find('universe')) #gives the index of word universe in the string

welcome.replace("world","universe")
new_message=welcome.replace("world","universe") #here it will be done in the new message declaered and not in the original welcome variable

print(new_message)

greeting="Hello"
name="Michael"
message=greeting+ ", " + name + " .Welcome"

diff_message='{}, {}. Welcome!'.format(greeting,name)

different_message=f'{greeting}, {name}. Welcome!'
print(message)
print(diff_message)
print(different_message)


# now to check every method available to us to use for strings we use dir()

print(dir(name))
# print(dir(greeting))

print(help(str))