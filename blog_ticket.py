# file: blog_ticket.py
# author: Justin Bankes
import os
import sys
import getpass
from jira import JIRA


def init_jira():
    jira_server = input('JIRA URL: ')
    user_name = input('username: ')
    password = getpass.getpass('password: ') 
    jira = JIRA(jira_server, basic_auth=(user_name, password))
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


def create_blog(jira, user, month):
    ticket_summary = f"{month} blog - {user}"
    ticket_desc = "_Please update with information about your blog._\n*Blog Title:*\n*Topic Desciption:*"
    new_issue = jira.create_issue(project='CHICO', summary=ticket_summary, 
            description=ticket_desc, issuetype={'name':'Task'}, 
            assignee={'name': user})


if __name__ == '__main__':
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        month = sys.argv[2]
    else:
        print("Please enter a file name to use, try again...")
        sys.exit(1)
    user_list = populate_users(file_name)

    jira = init_jira()

    for user in user_list:
        create_blog(jira, user, month)
 
