import os
import csv
import sys

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(nodes, path = './data/output.csv'):
    with open( path, 'w', encoding='utf8', newline='\n') as f:
        writer = csv.writer(f, delimiter=';')
        #writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(nodes)

def clear():
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def write_history(users, n):
    with open ('./PageRank-History/history.csv', 'w', encoding='utf8', newline='\n') as f:
        print('\nWriting history file...\n')

        writer = csv.writer(f, delimiter=';')

        header = []
        header.append('Iteration')
        for user in users:
            header.append(user.tag)
        writer.writerow(header)


        for i in range(n):
            
            row = []
            row.append(f'{i}')
            index = 1
            for user in users:
                clear()
                print(f'Writing iteration {i} for user {user.tag}')
                if user.tag != header[index]:
                    print('ERROR WRITING HISTORY')
                index += 1
                row.append(f'{user.history[i]}')
            writer.writerow(row)
        
        clear()
        clear()
        print('Writing history file completed\n')
