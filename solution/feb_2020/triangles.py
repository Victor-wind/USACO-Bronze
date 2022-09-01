vertices = []
dict_x = {}
dict_y = {}

with open('triangles.in') as f:
    lines = f.readlines()

# print(f'{lines=}')

N = int(lines[0])

for i in range(1, N+1):
    v = [ int(x) for x in lines[i].split() ]
    vertices.append(v)

#print(f'{vertices}')

for vertex in vertices:
    x, y = vertex[0], vertex[1]
    if x not in dict_x:
        dict_x[x] = []        
    dict_x[x].append(y)
    if y not in dict_y:
        dict_y[y] = []        
    dict_y[y].append(x)


max_area = 0
for vertex in vertices:
    x, y = vertex[0], vertex[1]
    for y_i in dict_x[x]:
        delta_y = abs(y_i-y)
        for x_i in dict_y[y]:
            delta_x = abs(x_i-x)
            area = delta_y * delta_x
            max_area = max(max_area, area)

#print(max_area)

with open('triangles.out', 'w') as f:
    f.write(f'{max_area}\n')
