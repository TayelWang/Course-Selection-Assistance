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





