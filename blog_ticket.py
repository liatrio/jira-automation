import os
import sys
import getpass
from jira import JIRA

def init_jira():
    user_name = input('Username: ')
    password = getpass.getpass('Password: ') 
    jira = JIRA('https://liatrio.atlassian.net', basic_auth=(user_name, password))
    return jira

def populate_users(file_name):
    user_list = []
    if os.path.exists(file_name):
        for line in open(file_name, 'r'):
            user_list.append(line.strip())
        return user_list
    else:
        print("File is missing, please try again")
        sys.exit()


def create_blog(user, jira):
    pass



if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print("Please enter a file name to use, try again...")
        sys.exit(1)
    user_list = populate_users(file_name)

    jira = init_jira()

    for user in user_list:
        create_blog(user, jira)
    
