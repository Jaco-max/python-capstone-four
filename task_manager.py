# Modules used in the methods below are imported

import pandas
from datetime import datetime as dt
from tabulate import tabulate

# Some of the global variables used are initialised below

log_in = False
user_selection = False
exit_selection = False
admin_user = False
user_details = []
users = []
tasks = []
number_of_tasks = int(0)
my_num_tasks = int(0)
my_tasks_list = []
admin_logged_in = False
log_out_select = False

# Function menu_selection allows user to select different menu options
# based on whether they are the admin or not


def menu_selection():
    menu_option = ''

    if admin_logged_in != True:
        menu_option = input(
            str('\nMAIN MENU\n'
                '\nPlease select one of the following options: \n'
                'VA - View all tasks\n'
                'VM - View my tasks\n'
                'L - Log Out\n'))
        menu_option = menu_option.upper()

    elif admin_logged_in == True:
        menu_option = input(
            str('\nMAIN MENU\n'
                '\nPlease select one of the following options: \n'
                'R - Register user\n'
                'A - Add task\n'
                'VA - View all tasks\n'
                'VM - View my tasks\n'
                'GR - Generate Reports\n'
                'DS - Display Statistics\n'
                'L - Log Out\n'))
        menu_option = menu_option.upper()

    return(menu_option)

# Function read_users reads data from user.txt into a list and returns the list


def read_users():
    all_users = []
    file_user = open('user.txt', 'r+')
    for line in file_user:
        line = line.strip()
        temp_line = line.split(', ')
        all_users.append(temp_line)
    file_user.close()

    return(all_users)

users = read_users()

# Function read_tasks reads data from user.txt into a list and returns the list


def read_tasks():
    all_tasks = []
    file_tasks = open('tasks.txt', 'r')
    for line in file_tasks:
        line = line.strip()
        temp_line = line.split(', ')
        all_tasks.append(temp_line)
    file_tasks.close()

    return(all_tasks)

tasks = read_tasks()

# Function get_number_of_tasks returns the total number of tasks for all users


def get_number_of_tasks():
    v = int(0)
    file_tasks = open('tasks.txt', 'r')
    for line in file_tasks:
        v += 1

    return(v)

number_of_tasks = get_number_of_tasks()

# Function reg_user allows the admin to register a new user


def reg_user():

    user_exists = False
    password_conf = False
    existing_user = False
    new_username = ''
    new_password = ''
    password_confirm = ''

    while existing_user != True:
        print('Please enter the new username: ')
        new_username = str(input())

        v = int(0)

        for i in users:
            if new_username == users[v][0]:
                print('Username exists')
                existing_user = False
            else:
                existing_user = True
            v += 1

    while password_confirm != True:
        print('Please enter a new password: ')
        new_password = str(input())
        print('Please confirm the password: ')
        new_password_confirm = str(input())

        if new_password == new_password_confirm:
            password_confirm = True
            file_user = open('user.txt', 'a+')
            file_user.write(new_username + ', ' +
                            new_password + '\n')
            file_user.close()
            print('--User added--')

        else:
            print('Passwords do not match')

# Function add_task allows the admin to assign a task to a
# specific user


def add_task():
    user_exists = False
    user_name_new = ''
    task_title = ''
    task_due = ''
    task_complete = ''
    task_description = ''

    while user_exists != True:
        print('Please enter the username to recieve a task: ')
        user_name_new = str(input())
        v = int(0)
        for i in users:

            if user_name_new == users[v][0]:
                user_exists = True
            v += 1

        if user_exists == True:
            print('Please enter the Title of the task: ')
            task_title = str(input())
            print('Please enter a description of the task: ')
            task_description = str(input())
            print('Please enter a due date for the task,'
                  'eg. 20-10-2020: ')
            task_due = str(input())

            task_complete = str('No')

            file_tasks = open('tasks.txt', 'a+')
            file_tasks.write(user_name_new + ', ' + task_title +
                             ', ' + task_description +
                             ', ' + task_due +
                             ', ' + task_complete + '\n')
            file_tasks.close()
            print('\n--Task Added--\n')

        else:
            user_exists = False
            print('\nUser does not exist\n')

# Check_user checks if the user that logged in is the admin or not.
# Check_user returns a boolean


def check_user(x):

    check_if_admin = False
    user_admin_temp = ''

    user_admin_temp = str(x)
    if user_admin_temp == 'admin':
        check_if_admin = True
    else:
        check_if_admin = False

    return check_if_admin

# log_in allow the user to log in. It returns the username and
# password of the user.


def log_in():
    user_admin = False

    check_username = False
    check_password = False

    passwords = []
    user_names = []
    users = read_users()
    tasks = read_tasks()

    v = int(0)
    for i in users:
        passwords.append(users[v][1])
        v += 1

    v = int(0)
    for i in users:
        user_names.append(users[v][0])
        v += 1

    while (check_username != True) or (check_password != True):
        print('Please enter your username:')
        user_name = str(input())

        print('Please enter your password:')
        user_password = str(input())

        if user_name in user_names:
            check_username = True
        else:
            print('\nUsername not found\n')

        if user_password in passwords:
            check_password = True
        else:
            print('\nPassword incorrect\n')

        if (check_username) and (check_password):
            log_in = True

    if log_in:
        print('\n--Logged In--\n')

    return [user_name, user_password]

# view_all displays all the tasks using the read_tasks function
# tabulate is also used to display the information in a meaningful manner


def view_all():

    all_tasks = read_tasks()

    print('')

    print(tabulate(all_tasks, headers=['User', 'Task', 'Task Description',
                                       'Due date', 'Completed']))

    print('')

# view_mine returns the tasks of the user that is logged in, in a list.


def view_mine():
    my_task_length = int(0)
    users = read_users()
    my_tasks = []
    num_tasks = int(1)
    my_tasks_print = ''
    user_selection = ''
    task_index = int(0)
    task_change = ''
    total_task_list = []

    file_tasks = open('tasks.txt', 'r+')

    total_tasks = int(0)
    my_task_number = int(0)

    for line in file_tasks:
        line = line.strip()
        temp_line = line.split(', ')

        if user_name == temp_line[0]:
            my_tasks.append(temp_line)
            del my_tasks[my_task_length][0]
            my_task_length += 1

    v = int(0)

    for i in my_tasks:
        v += 1
        my_tasks[v-1].append(str(v))

    file_tasks.close()

    return(my_tasks)

# my_number_of_tasks returns the number of tasks assiged to the user
# that is logged in


def my_number_of_tasks():
    n = int(0)
    for i in my_tasks_list:
        n += 1

    return(n)

# ammend_task allows the user to mark a specific task completed or
# assign a specific task to another user


def ammend_task():

    username_selection = ''
    task_selection = ''
    task_selection_int = int(0)
    main_menu_chosen = False
    ammend_option = ''
    new_line = ''
    new_line_temp = ''
    new_line_length = int(0)
    task_range = False
    task_completed = False

    while main_menu_chosen != True:

        while task_range != True:
            task_selection = input(
                str('\nPlease select one of the tasks listed above ' +
                    'or enter -1 to return to the main menu\n' +
                    '\nPlease enter only the number of the task .eg 1:\n'))

            task_selection_int = int(task_selection)

            if (task_selection_int > 0) and (task_selection_int <= my_num_tasks):

                task_range = True

            elif task_selection_int == int(-1):
                task_range = True

            else:
                print('\nINCORRECT INPUT\n')
                task_range = False

        if task_selection_int == int(-1):
            main_menu_chosen = True
            break

        if str(my_tasks_list[task_selection_int-1][3]) == 'Yes':
            task_completed = True
            print('\n--Task has been completed previously--\n')
            break

        ammend_option = str(
            input('\nWould you like to mark the task as completed (M)'
                  '\nor\n'
                  'would you like to assign the task to another user (A)?\n'))
        ammend_option = ammend_option.upper()

        if (ammend_option == 'M') and (task_completed == False):

            v = int(0)

            for i in range(0, number_of_tasks):
                if (user_name == tasks[v][0]) and (tasks[v][1] == my_tasks_list[task_selection_int-1][0]):

                    tasks[v][4] = str('Yes')
                v += 1

            file_tasks = open('tasks.txt', 'r+')
            v = int(0)
            file_tasks.seek(0)
            for v in range(0, number_of_tasks):
                new_line_temp = (str(tasks[v]))
                new_line_length = len(new_line_temp)
                new_line_temp = new_line_temp.replace('[', '')
                new_line_temp = new_line_temp.replace(']', '')
                new_line_temp = new_line_temp.replace('\'', '')
                new_line = new_line_temp
                file_tasks.write(new_line + '\n')
                v += 1
            file_tasks.close()
            main_menu_chosen = True
            print('\n--Task has been completed!--\n')

        elif (ammend_option == 'A') and (task_completed == False):
            username_selection = input(
                '\nPlease enter the user to which the task must be assigned\n')
            v = int(0)

            for i in range(0, number_of_tasks):
                if my_tasks_list[task_selection_int-1][0] == tasks[v][1]:
                    tasks[v][0] = str(username_selection)
                v += 1

            file_tasks = open('tasks.txt', 'r+')
            v = int(0)
            file_tasks.seek(0)
            for v in range(0, number_of_tasks):
                new_line_temp = (str(tasks[v]))
                new_line_length = len(new_line_temp)
                new_line_temp = new_line_temp.replace('[', '')
                new_line_temp = new_line_temp.replace(']', '')
                new_line_temp = new_line_temp.replace('\'', '')
                new_line = new_line_temp
                file_tasks.write(new_line + '\n')
                v += 1
            file_tasks.close()
            main_menu_chosen = True
            print('\n--Task has been assigned to another user!--\n')

        else:
            print('PLEASE CHOOSE ONLY (A), (M) OR (-1)')
            main_menu_chosen = False

# generate_reports generates statistics based on the users.txt textfile and the
# tasks.txt textfile. It writes the information to user_overview.txt and
# task_overview.txt


def generate_reports():

    today = dt.today()
    due_date = dt.today()
    due_date_str = ''

    total_tasks = int(0)

    completed_tasks = int(0)
    uncompleted_tasks = int(0)
    overdue_tasks = int(0)
    not_overdue = int(0)
    percentage_incomplete = float(0.00)
    percentage_overdue = float(0.00)
    task_stats = []
    delimeter = ', '

    v = int(0)

    for i in tasks:
        total_tasks += 1
        if tasks[v][4] == 'Yes':
            completed_tasks += 1
        elif tasks[v][4] == 'No':
            uncompleted_tasks += 1

        due_date_str = tasks[v][3]
        due_date = dt.strptime(due_date_str, "%d-%m-%Y")

        if due_date < today:
            overdue_tasks += 1
        else:
            not_overdue += 1

        v += 1

    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100
    percentage_incomplete = round(percentage_incomplete, 2)

    percentage_overdue = (overdue_tasks / uncompleted_tasks) * 100
    percentage_overdue = round(percentage_overdue, 2)

    task_overview = open('task_overview.txt', 'w+')
    task_overview.write(str(total_tasks) + delimeter + str(completed_tasks) +
                        delimeter + str(uncompleted_tasks) +
                        delimeter + str(percentage_incomplete) +
                        delimeter + str(overdue_tasks) +
                        delimeter + str(percentage_overdue))

    task_overview.close()

###########################################################################

    total_users_created = len(users)
    user_stats = []
    user_tasks_completed = int(0)
    user_tasks_not_completed = int(0)
    user_percentage = float(0.00)
    user_percentage_complete = float(0.00)
    user_percentage_incomplete = float(0.00)
    user_tasks_overdue = int(0)
    user_percentage_overdue = float(0.00)
    v = int(0)
    t = int(0)
    user_tasks = int(0)

    user_overview = open('user_overview.txt', 'w+')
    user_overview.write(str(total_users_created) +
                        '\n' +
                        str(total_tasks) +
                        '\n')

    for i in users:

        user_tasks = int(0)
        t = int(0)
        user_tasks_completed = int(0)
        user_tasks_not_completed = int(0)
        overdue_tasks = int(0)
        not_overdue = int(0)

        for s in tasks:

            if (users[v][0]) == (tasks[t][0]):
                user_tasks += 1
                if tasks[t][4] == 'Yes':
                    user_tasks_completed += 1

                elif tasks[t][4] == 'No':
                    user_tasks_not_completed += 1

                due_date_str = tasks[t][3]
                due_date = dt.strptime(due_date_str, "%d-%m-%Y")

                if due_date < today:
                    overdue_tasks += 1
                else:
                    not_overdue += 1

            t += 1

        user_percentage = (user_tasks / total_tasks) * 100
        user_percentage = round(user_percentage, 2)

        user_percentage_complete = (user_tasks_completed / user_tasks) * 100
        user_percentage_complete = round(user_percentage_complete, 2)

        if user_tasks > 0:
            user_percentage_complete = ((user_tasks_completed / user_tasks)*100)
            user_percentage_complete = round(user_percentage_complete, 2)

            user_percentage_incomplete = ((user_tasks_not_completed /
                                          user_tasks)*100)
            user_percentage_incomplete = round(user_percentage_incomplete, 2)
        else:
            user_percentage_incomplete = float(0.00)

        if user_tasks_not_completed > 0:
            user_percentage_overdue = ((overdue_tasks /
                                       user_tasks_not_completed)*100)
            user_percentage_overdue = round(user_percentage_overdue, 2)
        else:
            user_percentage_overdue = float(0.00)

        user_overview.write(users[v][0] + delimeter +
                            str(user_tasks) + delimeter +
                            str(user_percentage) + delimeter +
                            str(user_percentage_complete) +
                            delimeter + str(user_percentage_incomplete) +
                            delimeter +
                            str(user_percentage_overdue) + '\n')
        v += 1

    user_overview.close()
    print('')
    print('--Reports have been generated--')

# display_stats uses the information from user_overview.txt and
# task_overview.txt and displays it all in a meaningful manner
# using the pandas module


def display_stats():

    tasks_stats_list = []
    tasks_stats_headers = ['Total tasks',
                           'Completed Tasks',
                           'Uncompleted Tasks',
                           '% Incomplete',
                           '% Incomplete and Overdue',
                           '% Overdue']
    temp_line = []
    user_stats_list = []
    main_heading_tasks = ['TASK OVERVIEW']

    tasks_overview = open('task_overview.txt', 'r')

    for line in tasks_overview:
        line = line.strip()
        temp_line = line.split(', ')
        tasks_stats_list = temp_line

    tasks_overview.close()

    print('\n---Task Statistics---\n')

    print(pandas.DataFrame(tasks_stats_list, tasks_stats_headers,
                           main_heading_tasks))

    print('')
    print('---------------------')

#############################################################################

    i = ''
    s = int(0)

    line = ''
    temp_line = []

    main_heading_users = ['USER OVERVIEW']

    user_stats_list = []
    stats_headers = ['Total Number of users',
                     'Total Number of tasks']

    user_stats_headers = ['USERNAME',
                          'NUMBER OF TASKS ASSIGNED',
                          '% OF TOTAL TASKS ASSIGNED',
                          '% COMPLETED',
                          '% INCOMPLETE',
                          '% INCOMPLETE AND OVERDUE']

    users_overview = open('user_overview.txt', 'r')

    for line in users_overview:
        line = line.strip()
        temp_line = line.split(', ')
        user_stats_list.append(temp_line)

    users_overview.close()

    print('\n---User Statistics---\n')
    s = int(0)
    for i in stats_headers:
        print(stats_headers[s])
        print('')
        s += 1
        temp_str = str(user_stats_list[s-s])[2:-2]
        print(temp_str)
        print('')
        del user_stats_list[0]

    i = ''
    s = int(0)
    v = int(0)
    t = int(0)
    p = int(0)

    for i in range(0, len(user_stats_list)):
        print('')
        print(pandas.DataFrame(user_stats_list[s], user_stats_headers,
                               main_heading_users))
        print('')
        print('---- ----')
        s += 1

    print('')

# log_in is called so that the user can log in

# user_name and password are both assigned

# the username is also checked if it is the
# admin

user_details = log_in()
user_name = user_details[0]
password = user_details[1]
admin_logged_in = check_user(user_name)

# the while loop runs until the user logs out

# the while loop checks which option the user chooses and calls
# the appropriate functions, defined above

while log_out_select != True:
    menu_option_chosen = str(menu_selection())

    if (admin_logged_in == True) and (menu_option_chosen == 'R'):

        users = read_users()
        tasks = read_tasks()
        number_of_tasks = get_number_of_tasks()

        reg_user()
        log_out_select = False

    elif (admin_logged_in == True) and (menu_option_chosen == 'A'):
        users = read_users()
        tasks = read_tasks()
        number_of_tasks = get_number_of_tasks()

        add_task()
        log_out_select = False

    elif menu_option_chosen == 'VA':
        users = read_users()
        tasks = read_tasks()

        number_of_tasks = get_number_of_tasks()

        view_all()
        log_out_select = False

    elif menu_option_chosen == 'VM':
        users = read_users()
        tasks = read_tasks()

        my_tasks_list = view_mine()
        number_of_tasks = get_number_of_tasks()
        my_num_tasks = my_number_of_tasks()

        print('')
        print(tabulate(my_tasks_list, headers=['Task', 'Task Description',
                                               'Due date', 'Completed',
                                               'Task number']))
        print('')

        ammend_task()

        log_out_select = False

    elif (admin_logged_in == True) and (menu_option_chosen == 'GR'):
        users = read_users()
        tasks = read_tasks()

        my_tasks_list = view_mine()
        number_of_tasks = get_number_of_tasks()
        my_num_tasks = my_number_of_tasks()

        generate_reports()

    elif (admin_logged_in == True) and (menu_option_chosen == 'DS'):
        users = read_users()
        tasks = read_tasks()

        my_tasks_list = view_mine()
        number_of_tasks = get_number_of_tasks()
        my_num_tasks = my_number_of_tasks()

        display_stats()

    elif menu_option_chosen == str('L'):
        print('\n--You have logged out--\n')
        log_out_select = True

    else:
        print('Please select from the options in the menu below')
