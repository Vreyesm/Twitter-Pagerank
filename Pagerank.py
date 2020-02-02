from io_lib import *
from User import *


if __name__ == '__main__':
    files_path = './data/'
    labels_file = 'labels.csv'
    edges_file = 'edges.csv'

    users = {}

    ensure_dir(files_path)

    with open (files_path + labels_file, 'r', encoding='utf8') as f:
        for line in f:
            line = line.rstrip()
            values = line.split(';')
            key = values[0]
            tag = values[1]
            user = User(key, tag)
            #print(f'KEY: {key}\nTag:{tag}')
            
            users[key] = user
        
        print (f'Number of users: {len(users)}')
    
    with open (files_path + edges_file, 'r', encoding='utf8') as f:
        
        edges_counter = 0
        
        for line in f:
            edges_counter += 1
            line = line.rstrip()
            values = line.split(';')

            user_follower_key = values[1]
            user_followed_key = values[0]

            if (user_followed_key not in users):
                new_user = User(user_followed_key, user_followed_key)
                users[user_followed_key] = new_user
            if (user_follower_key not in users):
                new_user = User(user_follower_key, user_follower_key)
                users[user_follower_key] = new_user

            followed = users[user_followed_key]
            follower = users[user_follower_key]
            followed.followers.append(follower)

    print (f'Number of edges: {edges_counter}')
    print (f'Final number of users: {len(users)}')
    
    input("Press enter to finish")
    