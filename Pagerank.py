from io_lib import *
from User import *
import pickle

users = {}

def parse_double(number):
    lead, power = number.split("e-")
    a, b = lead.split(".")
    number = "0." + "0"*(int(power)-1) + a + b
    return number

#
# Delete user with 0 followers
#
def delete_users():
    print('Deleting users with no followers')
        
    count = 0
    print('0 Users removed')
    deleted = []
    while True:
        
        to_delete = []
        for user_key in users:
            user = users[user_key]
            if len(user.followers) == 0:
                #print(f'user {user.tag} has no followers')
                to_delete.append(user_key)

        if len(to_delete) == 0:
            break

        
        for key in to_delete:
            if key == '748549452':
                print('this is the key')
                input()
            #print(f'User to delete {user.tag}')
            
            for user_key in users:
                user = users[user_key]
                try:
                    user.followers.remove(key)
                    
                    #if len(user.followers) == 0:
                    #    print(f'user {user.tag} has now 0 followers')
                except ValueError:
                    continue
            del users[key]
            count += 1
            clear()
            print(f'{count} Users deleted')


#
# @return True if has loaded data from previous file, otherwise, False
#
def load_users():
    global users
    try:
        with open (files_path + 'users.pkl', 'rb') as users_input:
            print('Loading previous users data')
            users = pickle.load(users_input)
            print('Loaded previous users data')
        return True
    except FileNotFoundError:
        print('Generating dictionary of [key: user_tag]')
        with open (files_path + labels_file, 'r', encoding='utf8') as f:
            for line in f:
                line = line.rstrip()
                values = line.split(';')
                key = values[0]
                tag = values[1]
                user = User(key, tag, [])
                
                users[key] = user            
            print (f'Number of users: {len(users)}')
        for key in users:
            user = users[key]
            if (key != user.key):
                print('error')
        return False

def load_edges():
    global users

    users_output_file = 'users.pkl'

    print('Reading nodes from file')
    with open (files_path + edges_file, 'r', encoding='utf8') as f:
        
        edges_counter = 0
        for line in f:
            edges_counter += 1
            line = line.rstrip()
            values = line.split(';')

            user_follower_key = values[0]
            user_followed_key = values[1]

            if (user_followed_key not in users) or (user_follower_key not in users):
                continue
            
            followed = users[user_followed_key]
            followed.followers.append(user_follower_key)
            users[user_followed_key] = followed
        
        print (f'Number of edges: {edges_counter}')
        print (f'Final number of users: {len(users)}')


    #with open (files_path + users_output_file, 'wb') as users_output:
    #    pickle.dump(users, users_output, pickle.HIGHEST_PROTOCOL)


def PR(user, N, d = 0.85):
    global users
    base = (1 - d) / N

    s = 0
    
    #print(f'User {user.tag} has {len(user.followers)} followers')

    for in_user_key in user.followers:
        follower = users[in_user_key]
        C = len(follower.followers)
        # print(f'followed by: {follower.tag}')
        s += (follower.rank_prev) / C
    #print(f'Sum of all followers {s}')
    return base + s

def history(n):
    global users



    data = []

    iteration = []
    iteration.append('Iteration')
    data.append(iteration)
    
    for i in range(n):
        iteration.append(n + 1)

    #for key in users:
    #    user = users[key]
    #    row = []
    #    row.append(user.tag)
    #    row.append(user.history)
    #    data.append(row)

    #list(map(list, zip(*data)))
    write_file(data, 'history.csv')

if __name__ == '__main__':
    files_path = './data/'
    labels_file = 'labels_new.csv'
    edges_file = 'edges_new.csv'

    #labels_file = 'sample_labels.csv'
    #edges_file =  'sample_edges.csv'


    ensure_dir(files_path)


    print('Number of iterations', end=': ')
    n = int(input())

    #if ( not load_users() ):
    #    load_edges()
    load_users()
    load_edges()

    n_users = len(users)
    
    initial_rank = 1.0  / len(users)
    print(f'Initial rank for all users {initial_rank}')

    print('Initializing users rank')
    for key in users:
        user = users[key]
        user.rank = initial_rank
        
        #print(f'User {user.tag} has {len(user.followers)} followers')

    print('\n\nRunning Pagerank\n\n')

    iteration = 0
    while iteration < n:
        for key in users:
            user = users[key]
            user.rank = PR(user, n_users)
        iteration += 1
        for key in users:
            user = users[key]
            user.rank_prev = user.rank
            user.history.append(user.rank)

    users_list = [ u for u in users.values() ]
    users_list.sort(key=lambda u: u.rank, reverse=True)

    ranks = [ x.rank for x in users_list ]
    top_10 = ranks[0:10]

    top_users = users_list[0:10]

    for user in top_users:
        #print(parse_double(str(top)))
        print(f'{user.tag}: {user.rank}')

    write_history(users_list[0:10], n)

    users = None
    #input("\nPress enter to finish\n")
    