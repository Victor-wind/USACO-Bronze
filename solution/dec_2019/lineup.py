with open('lineup.in') as f:
    lines = f.readlines()

N = int(lines[0])
cows = ['Sue', 'Bessie', 'Buttercup', 'Belinda', 'Beatrice',
        'Bella', 'Blue', 'Betsy']

cows.sort()
nums = [i for i in range(1,9)]
cows_dic = dict(zip(cows,nums))

graph = [[] for _ in range(9)]
# print(cows_dic)
for i in range(N):
    words = lines[i+1].split()
    node_i = cows_dic[words[0]]
    node_j = cows_dic[words[-1]]
    graph[node_i].append(node_j)
    graph[node_j].append(node_i)

edge_nodes = [i for i in range(1, 9) if len(graph[i]) < 2]
# print(f'{graph=}')
# print(f'{edge_nodes=}')
result_num = list()
visited = [False] * 9
for i in edge_nodes:
    if visited[i]: continue
    # it should use queue, but in this problem, there is at most 1 element in queue, we can use list as stack
    st = list()
    st.append(i)
    while len(st) > 0:
        k = st.pop()
        visited[k] = True
        result_num.append(k)
        for j in graph[k]:
            if not visited[j]:
                st.append(j)
# print(f'{result_num=}')
num_to_cow = {v:k for k, v in cows_dic.items()}

with open('lineup.out', 'w') as f:
    for i in result_num:
        print(num_to_cow[i])
        f.write(num_to_cow[i]+'\n')
