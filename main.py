# Import
import sys
import os
from datetime import datetime

# Statement
my_courses= []
todo_list = []
users= {}
current_user=""
input_path =sys.argv[1]
output_path =sys.argv[2]

# Utility function
def add_course(courselist,course):
    courselist.append(course)

def remove_course(courselist,code):
    fd = search_code(courselist,code)
    if fd is None:
        input("Course not exist\nPress return to continue")
        return False
    courselist.remove(fd)
    return True

def search_code(courselist,code):
    target_code=code.upper()
    for tmp in courselist:
        if tmp["course_code"].upper()==target_code:
            return tmp       #return the staff or None
    return None

def search_keyword(courselist,keyword):
    kw = keyword.lower()
    out=[]
    for tmp in courselist:
        if kw in tmp["course_title"].lower():
            out.append(tmp)
    return out

# File/System Function Area
def read_input(path):
    f = open(path)

    line_no = 0
    for line in f:
        line_no=line_no+1
        text = line.strip()
        if text=="":
            continue
        attri = text.split("|")
        # C|username|code|title|term|professor|status|remark
        if len(attri) != 8 or attri[0] != "C":
            continue
        username, code, title, term, professor, status, remark = attri[1:]
        level = 0
        for i in code:
            if i.isdigit():
                level = int(i) * 1000
                break

        add_course(my_courses, {
            "username": username.strip(),
            "course_code": code.strip(),
            "course_title": title.strip(),
            "credit": 3,
            "course_level": level,
            "term": term.strip(),
            "professor": professor.strip(),
            "status": status.strip(),
            "remark": remark.strip()
        })
    f.close()

def save_input():
    kept = []
    f = open(input_path, "r")
    for line in f:
        text = line.strip()
        if text == "":
            continue
        attri = text.split("|")
        if attri[0] == "U":
            continue
        if attri[0] == "C" and len(attri) >= 2 and attri[1] == current_user:
            continue
        if attri[0] == "T" and len(attri) >= 2 and attri[1].strip() == current_user:
            continue
        kept.append(text)
    f.close()

    f = open(output_path, "w")
    for username in users:
        f.write("U|" + username + "|" + users[username] + "\n")
    for text in kept:
        f.write(text + "\n")
    for course in my_courses:
        line = "|".join([
            "C",
            course["username"],
            course["course_code"],
            course["course_title"],
            course["term"],
            course["professor"],
            course["status"],
            course["remark"],
        ])
        f.write(line + "\n")
    for item in todo_list:
        line = "|".join([
            "T",
            current_user,
            item["date"].strftime("%Y-%m-%d"),
            item["thing"],
            item["class_name"],
        ])
        f.write(line + "\n")
    f.close()

# Read accounts from the input file. Each account line is U|username|password.
def load_users():
    users.clear()
    try:
        f = open(input_path, "r")
    except OSError:
        print("Cannot open input file: " + input_path)
        sys.exit()

    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) >= 3 and parts[0] == "U":
                # Second field is the username, third is the password.
                username = parts[1]
                password = parts[2]
                users[username] = password
    f.close()

def read_todos(path):
    f = open(path)
    today = datetime.now().date()
    for line in f:
        text = line.strip()
        if text == "":
            continue
        attri = text.split("|")
        if len(attri) != 5 or attri[0] != "T":
            continue
        if attri[1].strip() != current_user:
            continue
        try:
            event_date = datetime.strptime(attri[2].strip(), "%Y-%m-%d")
        except ValueError:
            continue
        if event_date.date() < today:
            continue
        todo_list.append({
            "date": event_date,
            "thing": attri[3].strip(),
            "class_name": attri[4].strip()
        })
    f.close()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.environ["TERM"] = "xterm-256color"    #pretend error alarm
        os.system("clear")




# core function pls put here in order
# 1 WANG Ziwen
def courseinfo_function():

    print("                  ==MY COURSES==                     ")
    
    print("add courses(a)   remove courses(r)   specific info(s)\n")
    
    #show all of my courses
    for course in my_courses:
        print(f"{course['course_code']:<14}{course['course_title']}")
    print()
    print("Quit(q)")
    ch = input("What's next? ")

    if ch == "a":
        code = input("Input course code: ")
        level = 0
        for i in code:
            if i.isdigit():
                level = int(i) * 1000
                break
        add_course(my_courses, {
            "username": current_user,
            "course_code": code,
            "course_title": input("Input course name: "),
            "credit": 3,
            "course_level": level,
            "term": input("Input term: "),
            "professor": input("Input professor: "),
            "status": input("Input status: "),
            "remark": None
        })
        clear_screen()
        courseinfo_function()
    elif ch == "r":
        code = input("Input course code: ")
        if remove_course(my_courses, code):
            print("Removed")
        else:
            print("Course not found")
        clear_screen()
        courseinfo_function()
    elif ch == "s":
        string = input("Input course code or title: ")
        if string[-4].isdigit():
            tmp="cod"
        else:
            tmp="key"
        if tmp == "cod":
            fc = search_code(my_courses, string)
            if fc is None:
                print("Not found?")
            else:
                print("=========================================================")
                print(fc["course_code"])
                print(fc["course_title"])
                print("---------------------------------------------------------")
                print("Credit : ",fc["credit"],"\t","Level : ",fc["course_level"])
                print("Term : ",fc["term"])
                print("Prof : ",fc["professor"])
                print("Status : ",fc["status"])
                print("Remark : ",fc["remark"])
            input("Press to return")
        elif tmp == "key":
            fc = search_keyword(my_courses,string)
            if fc == []:
                print("Course not found")
            else:
                for course in fc:
                    print("=========================================================")
                    print(course["course_code"])
                    print(course["course_title"])
                    print("---------------------------------------------------------")
                    print("Credit : ",course["credit"],"\t","Level : ",course["course_level"])
                    print("Term : ",course["term"])
                    print("Prof : ",course["professor"])
                    print("Status : ",course["status"])
                    print("Remark : ",course["remark"])
                    print()
            input("Press Enter to go back")
        clear_screen()
        courseinfo_function()
    else:
        return

# 2 Li
# T|username|date|thing|class_name
def time_function():
    global todo_list

    def refresh_list():
        global todo_list
        today = datetime.now().date()
        kept = []
        for item in todo_list:
            event_day = item["date"].date()
            if event_day < today:
                print("Date has passed, removed: " + str(event_day) + "  " + item["thing"])
            else:
                kept.append(item)
        todo_list = kept

        print("\n===== Todo List =====")
        if len(todo_list) == 0:
            print("(empty)")
            print("-" * 50)
            return

        todo_list.sort(key=lambda item: item["date"])

        for item in todo_list:
            event_day = item["date"].date()
            line = str(event_day) + "\t\t" + item["thing"] + "\t\t" + item["class_name"]
            if event_day == today:
                print("\033[91m" + line + "\033[0m")
            else:
                print(line)
        print("-" * 50)

    print("To Do List")
    print("add new items (a) \t remove items (r) \t quit (q)")
    print("***********************************************************")
    refresh_list()

    while True:
        choice = input("any decision or quit (q): ").strip().lower()

        if choice == "q":
            print("Bye")
            break

        elif choice == "a":
            date_text = input("please put your date (YYYY-MM-DD): ").strip()
            thing = input("put the things: ").strip()
            class_name = input("put the class name: ").strip()

            try:
                event_date = datetime.strptime(date_text, "%Y-%m-%d")
            except ValueError:
                print("Wrong date format, please use YYYY-MM-DD")
                continue

            if "|" in thing or "|" in class_name:
                print("Please do not use |.")
                continue

            todo_list.append({
                "date": event_date,
                "thing": thing,
                "class_name": class_name
            })
            print("Added successfully")

        elif choice == "r":
            date_text = input("which day's item do you want to remove (YYYY-MM-DD): ").strip()
            same_day = []
            for item in todo_list:
                if str(item["date"].date()) == date_text:
                    same_day.append(item)

            if len(same_day) == 0:
                print("No item on this day")
                continue

            print("Items on " + date_text + ":")
            number = 1
            for item in same_day:
                print(str(number) + ". " + item["thing"] + " | " + item["class_name"])
                number = number + 1

            # One item on that day can be removed directly. More than one, ask which number.
            if len(same_day) == 1:
                target = same_day[0]
            else:
                number_text = input("Enter the number you want to delete (0 = cancel): ").strip()
                if number_text.isdigit() == False:
                    print("Invalid input")
                    continue
                number = int(number_text)
                if number == 0:
                    print("Cancelled")
                    continue
                if number < 1 or number > len(same_day):
                    print("No such number")
                    continue
                target = same_day[number - 1]

            todo_list.remove(target)
            print("Removed successfully")

        else:
            print("Unknown command, please type a / r / q")

        refresh_list()

# 3 Aiden Chen

# 4

# 5 Andy
def overview_function():
    while True:
        clear_screen()

        total_courses = len(my_courses)
        total_credits = 0
        term_credits = {}
        term_counts = {}
        status_counts = {}

        for course in my_courses:
            cred = course["credit"]
            total_credits = total_credits + cred

            term = course["term"]
            if term == "":
                term = "Unknown"
            if term not in term_credits:
                term_credits[term] = 0
                term_counts[term] = 0
            term_credits[term] = term_credits[term] + cred
            term_counts[term] = term_counts[term] + 1

            status = course["status"]
            if status == "":
                status = "Unknown"
            if status not in status_counts:
                status_counts[status] = 0
            status_counts[status] += 1
            status_counts[status] = status_counts[status] + 1

        print("=========================================================")
        print("              ==PERSONAL DATA OVERVIEW==                 ")
        print("=========================================================")
        print("User Name      : " + current_user)
        print("Total Courses  : " + str(total_courses))
        print("Total Credits  : " + str(total_credits))
        print("---------------------------------------------------------")

        print("[Credits by Term]")
        if total_courses == 0:
            print("No course records yet.")
        else:
            for term in term_credits:
                c_num = term_counts[term]
                c_cred = term_credits[term]
                warning = ""
                if c_cred < 12:
                    warning = " (Below 12 credits)"
                elif c_cred > 18:
                    warning = " (Over 18 credits)"
                print(
                    "  " + term + " : "
                    + str(c_num) + " course(s), "
                    + str(c_cred) + " credits"
                    + warning
                )

        print("---------------------------------------------------------")
        print("[Courses by Status]")
        if total_courses == 0:
            print("No status records yet.")
        else:
            for st in status_counts:
                print("  " + st + " : " + str(status_counts[st]) + " course(s)")

        print("---------------------------------------------------------")
        print("[Selected Courses Summary]")
        if total_courses == 0:
            print("(Empty)")
        else:
            print("Code | Title | Term | Credit | Status")
            print("---------------------------------------------------------")
            for course in my_courses:
                print(
                    course["course_code"] + " | "
                    + course["course_title"] + " | "
                    + course["term"] + " | "
                    + str(course["credit"]) + " | "
                    + course["status"]
                )
        print("=========================================================")
        print()
        print("Export to txt(e)   Quit(q)")
        ch = input("What's next? ")

        if ch == "e":
            export_name = "overview_" + current_user + ".txt"
            f = open(export_name, "w")
            f.write("=========================================================\n")
            f.write("              ==PERSONAL DATA OVERVIEW==                 \n")
            f.write("=========================================================\n")
            f.write("User Name      : " + current_user + "\n")
            f.write("Total Courses  : " + str(total_courses) + "\n")
            f.write("Total Credits  : " + str(total_credits) + "\n")
            f.write("---------------------------------------------------------\n")
            f.write("[Credits by Term]\n")
            for term in term_credits:
                f.write(
                    "  " + term + " : "
                    + str(term_counts[term]) + " course(s), "
                    + str(term_credits[term]) + " credits\n"
                )
            f.write("---------------------------------------------------------\n")
            f.write("[Courses by Status]\n")
            for st in status_counts:
                f.write("  " + st + " : " + str(status_counts[st]) + " course(s)\n")
            f.write("---------------------------------------------------------\n")
            f.write("[Selected Courses Summary]\n")
            for course in my_courses:
                line = (
                    course["course_code"] + " | "
                    + course["course_title"] + " | "
                    + course["term"] + " | "
                    + str(course["credit"]) + " credits | "
                    + course["status"] + "\n"
                )
                f.write(line)
            f.close()
            print("Saved to " + export_name)
            input("Press Enter to continue")
        elif ch == "q":
            return




#Sign up/ Login from Jerry
def login_function():
    global current_user
    load_users()

    while True:
        print("\n--- Login System ---")
        print("1. Create account")
        print("2. Log in")
        print("3. Log out")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            # Ask for a new username and password.
            username = input("Enter a new username: ").strip()
            password = input("Enter a new password: ").strip()

            # Check the details before creating the account.
            if username == "" or password == "":
                print("Username and password cannot be empty.")
            elif "|" in username or "|" in password:
                print("Please do not use |.")
            elif username in users:
                print("This username already exists.")
            else:
                # Keep the new account in memory. It is written to the output file on save.
                users[username] = password
                print("Account created!")

        elif choice == "2":
            if current_user != "":
                print("Please log out first.")
            else:
                username = input("Username: ").strip()
                password = input("Password: ").strip()

                # Check that the username exists and the password matches.
                if username in users and users[username] == password:
                    current_user = username
                    print("Welcome, " + current_user + "!")
                    return current_user
                else:
                    print("Incorrect username or password.")

        elif choice == "3":
            if current_user == "":
                print("You are not logged in.")
            else:
                # Clear the login status without deleting the account.
                current_user = ""
                print("You have logged out.")

        elif choice == "4":
            print("Goodbye!")
            return ""

        else:
            print("Please enter 1, 2, 3, or 4.")
login_function()
clear_screen()
if current_user == "":
    save_input()
    sys.exit()



#Some Set up
read_input(input_path)
mine = []
for course in my_courses:
    if course["username"] == current_user:
        mine.append(course)
my_courses = mine
read_todos(input_path)



# Main interface
while True:
    print("\n")
    print("       ========Study Information Assistance========       \n")
    print("               Course Information Inquiry(1)\n")
    print("               To-do list(2)\n")
    print("               Timetable(3)\n")
    print("               GEN Subject Suggestion(4)\n")
    print("               Personal Data Overview(5)\n")

    ans = input()
    clear_screen()

    if ans == "1":
        courseinfo_function()
        save_input()
        clear_screen()
    elif ans == "2":
        time_function()
        save_input()
    elif ans == 3:
        credit_function()
    elif ans == 4:
        gen_function()
    elif ans == "5":
        overview_function()
        clear_screen()
    else:
        save_input()
        sys.exit()




'''        
被遗弃的计划/代码
def write_output(path):
    f = open(path, "w")
    for course in my_courses:
        line = "|".join([
            course["course_code"],
            course["course_title"],
            course["term"],
            course["professor"],
            course["status"],
            course["remark"],
        ])
        f.write(line + "\n")
    f.close()
'''
