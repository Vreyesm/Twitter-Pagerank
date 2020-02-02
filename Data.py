from os import listdir
from os.path import isfile, join
import os
import csv
from io_lib import *



if __name__ == "__main__":
    files_path = './files/'
    output_path = './data/'

    ensure_dir(files_path)
    ensure_dir(output_path)



    files = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    total_files = len(files)
    
    output = []
    labels = []

    print('Files to read: ' + str(total_files))

    file_count = 1
    for file in files:
        #print(f'File {file_count} of {total_files}')
        if not file.endswith('_friends.csv'):
                continue
        name = str(file).split('_friends.csv')[0]
        
        with open(files_path + file, 'r', encoding='utf8') as f:
            # skip the first line id of 'name'
            #next(f)
            count = 0
            tag = ''
            for line in f:
                if count == 0:
                    tag = line.rstrip()
                    labels.append([tag, name])
                    count += 1
                    continue
                output.append([line.rstrip(), tag]) # for friends tag,line.rstrip()
            f.close()       
        file_count += 1
    print('Total edges: ' + str(len(output)))
    print('Write the file...')
    write_file(output, path= output_path + 'edges.csv')
    write_file(labels, path= output_path + 'labels.csv')
