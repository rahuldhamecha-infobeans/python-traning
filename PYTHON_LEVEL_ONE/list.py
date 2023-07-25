list = ['rahul','vishal', 'sagar', 'sunit']

print(list);

print("Append Item : ")
list.append('Darsh')
print(list)

print('Extend the list : ')
list.extend(['Krushan', 'Mayur', 'Harsh'])
print(list)

print('Pop the last item :')
pop_item = list.pop()
print(pop_item)
print(list)

print('Reverse the list :')
list.reverse()
print(list)


print('List Comprehension')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[2] for row in matrix]
print(first_col)