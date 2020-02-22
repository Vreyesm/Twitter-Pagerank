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
                prin('error')
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

            if (user_followed_key not in users):
                #new_user = User(user_followed_key, user_followed_key)
                #users[user_followed_key] = new_user
                continue
            if (user_follower_key not in users):
                #new_user = User(user_follower_key, user_follower_key)
                #users[user_follower_key] = new_user
                continue

            followed = users[user_followed_key]
            follower = users[user_follower_key]
            followed.followers.append(follower)
        print (f'Number of edges: {edges_counter}')
        print (f'Final number of users: {len(users)}')
    
    #with open (files_path + users_output_file, 'wb') as users_output:
    #    pickle.dump(users, users_output, pickle.HIGHEST_PROTOCOL)


def PR(user, N, d = 0.85):
    base = (1 - d) / N

    sum = 0
    for in_user in user.followers:
        sum += in_user.rank
    return base + sum


if __name__ == '__main__':
    files_path = './data/'
    #labels_file = 'labels.csv'
    #edges_file = 'edges.csv'

    labels_file = 'sample_labels.csv'
    edges_file =  'sample_edges.csv'


    ensure_dir(files_path)


    print('Number of iterations', end=': ')
    n = int(input())

    if ( not load_users() ):
        load_edges()


    n_users = len(users)
    
    

    initial_rank = 1.0 / len(users)
    print(f'Initial rank for all users {initial_rank}')

    print('Initializing users rank')
    for key in users:
        user = users[key]
        user.rank = initial_rank
        
        #print(f'User {user.tag} has {len(user.followers)} followers')

    exit

    print('Running Pagerank')

    iteration = 0
    while iteration < n:
        for key in users:
            user = users[key]
            user.rank = PR(user, n_users)
        iteration += 1

    users_list = [ u for u in users.values() ]
    users_list.sort(key=lambda u: u.rank, reverse=True)

    ranks = [ x.rank for x in users_list ]
    top_10 = ranks[0:10]

    top_users = users_list[0:10]

    for user in top_users:
        #print(parse_double(str(top)))
        print(f'{user.tag}: {user.rank}')

    input("\nPress enter to finish\n")
    