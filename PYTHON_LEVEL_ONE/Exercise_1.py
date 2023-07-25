# GIVEN String :
string = 'django'

print(string[0]) # print d
print(string[-1]) # print o
print(string[:4]) # print djan
print(string[4:]) # print go

list = [3,7,[1,4,'hello']]

list[2][2] = 'goodbye'
print(list)

d1 = {'simple_key' : 'Hello'}
d2 = {'k1' : {'k2' : 'Hello'}}
d3 = {'k1' : [{'nest_key' : ['this is deep',['Hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])


mylist = [1,1,1,1,2,2,2,4,4,4,3,3,3,3]
converted  =set(mylist)
print(converted)

age = 4
name = "Sammy"

text = "Hello my dog's name is {dog_name} and he is {dog_age} years old.".format(dog_name=name,dog_age=age)

print(text)