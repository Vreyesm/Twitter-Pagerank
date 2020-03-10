from io_lib import write_file
from random import randint

n = int(input('Number of nodes: '))

print(f'Generating {n} labels')

labels = []
for i in range(n):
    labels.append([i, i])

write_file(labels, path='./data/sample_labels.csv')

n_edges = randint(int(n/2.0) , n)

print(f'Generating {n_edges} edges')

edges = []
for i in range(n):
    a = randint(0, n - 1)
    b = randint(0, n - 1)

    while b == a or [a, b] in edges or [b, a] in edges:
        b = randint(0, n - 1)

    

    edges.append([a, b])

write_file(edges, path='./data/sample_edges.csv')