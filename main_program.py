# Import
import sys
import os

# Statement
my_courses= []
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

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.environ["TERM"] = "xterm-256color"    #pretend error alarm
        os.system("clear")




# core function pls put here in order
# 1
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


# 2

# 3

# 4

# 5





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
        # update the saving
        save_input()
        clear_screen()
    elif ans == 2:
        time_function()
    elif ans == 3:
        credit_function()
    elif ans == 4:
        gen_function()
    elif ans == 5:
        overview_function()
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


