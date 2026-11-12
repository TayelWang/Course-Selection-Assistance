import sys
from dataclasses import dataclass
import os


@dataclass
class Course:
    course_code: str
    course_title: str
    credit: int
    course_level: int
    course_type: str                      # core｜eng
    prerequisite: list[str]               # useless will be canceled
    professor: str
    remark: str                           # Note


class Manager:
    def __init__(self):
        self.all_courses = []             #create a space(list)

    def add_course(self,course):
        self.all_courses.append(course)   #initialized every Method

    def search_code(self,code):
        target_code=code.upper()
        for tmp in self.all_courses:      #go through the whole list
            if tmp.course_code.upper() == target_code:   #hardcode's fist valued whether equal to the target
                return tmp       #return the staff or None
        return None

    def search_keyword(self,keyword):
        kw = keyword.lower()
        out=[]
        for tmp in self.all_courses:
            if kw in tmp.course_title.lower():
                out.append(tmp)
        return out

mgr=Manager()


'''
def load_all_course():
    global mgr
    mgr.add_course(Course(
        course_code="COMP1080SEF",
        course_title="Introduction to Computer Programming",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="Au Yeung Siu Kei",
        remark=""
    ))
load_all_course()
'''



def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Sign up/ Login from Jerry
# Store usernames and passwords in a dictionary.
users = {}

# An empty string means nobody is logged in.
current_user = ""

# Create users.txt if it does not exist.
with open("users.txt", "a") as file:
    pass

# Read the saved accounts from the file.
with open("users.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            # Separate the username and password at the comma.
            username, password = line.split(",")
            users[username] = password

# Keep showing the menu until the user chooses Exit.
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
        elif "," in username or "," in password:
            print("Please do not use commas.")
        elif username in users:
            print("This username already exists.")
        else:
            # Add the account to the file without deleting old accounts.
            with open("users.txt", "a") as file:
                file.write(username + "," + password + "\n")

            # Also add the account to the dictionary.
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
        # Stop the menu loop.
        break

    else:
        print("Please enter 1, 2, 3, or 4.")
print("\n")
print("Study Information Assistance\n")
print("Course Information Inquiry(1)\n")
print("To-do list(2)\n")
print("Timetable(3)\n")
print("GEN Subject Suggestion(4)\n")
print("Personal Data Overview(5)\n")

ans = input()
clear_screen()








if ans == 1:
    courseinfo_function()
elif ans == 2:
    time_function()
elif ans == 3:
    credit_function()
elif ans == 4:
    gen_function()
elif ans == 5:
    overview_function()
else:
    sys.exit()





