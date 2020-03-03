import os
import csv

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(nodes, path = './data/output.csv'):
    with open( path, 'w', encoding='utf8', newline='\n') as f:
        writer = csv.writer(f, delimiter=';')
        #writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(nodes)