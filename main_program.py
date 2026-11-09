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

    mgr.add_course(Course(
        course_code="COMP2090SEF",
        course_title="Data Structures, Algorithms & Problem Solving",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="Staff",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP2020SEF",
        course_title="Java Programming Fundamentals",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="Staff",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP2640SEF",
        course_title="Discrete Mathematics",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="Ren SiJie",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP2030SEF",
        course_title="Intermediate Java Programming & User Interface Design",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3200SEF",
        course_title="Database Management",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="Zhang TianTian/Wang WeiMing",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3500SEF",
        course_title="Software Engineering",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="EZEAMUZIE NDUDI/LI YISHU/CHAN PAK YUEN PATRICK",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3130SEF",
        course_title="Mobile Application Programming",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3510SEF",
        course_title="Software Project Management",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4820SEF",
        course_title="Data Mining & Analytics",
        credit=3,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3920SEF",
        course_title="Machine Learning",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP3810SEF",
        course_title="Server-Side Technologies & Cloud Computing",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4330SEF",
        course_title="Advanced Programming & AI Algorithms",
        credit=3,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4930SEF",
        course_title="Deep Learning",
        credit=3,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4610SEF",
        course_title="Data Science Project",
        credit=6,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4210SEF",
        course_title="Advanced Database & Data Warehousing",
        credit=3,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="COMP4600SEF",
        course_title="Advanced Topics in Data Mining",
        credit=3,
        course_level=4000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="IT1020SEF",
        course_title="Computing Fundamentals",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="Danni",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="IT1030SEF",
        course_title="Introduction to Internet Application Development",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="IT2900SEF",
        course_title="Human Computer Interaction & User Experience Design",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="MATH1410SEF",
        course_title="Algebra & Calculus",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="MATH1410SEF",
        course_title="Linear Algebra",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT1510SEF",
        course_title="Probability and Distribution",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT2510SEF",
        course_title="Statistical Data Analysis",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT2520SEF",
        course_title="Applied Statistical Methods",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT2610SEF",
        course_title="Data Analytics with Applications",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT2630SEF",
        course_title="Big Data Analytics with Applications",
        credit=3,
        course_level=2000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT3110SEF",
        course_title="Time Series Analysis & Forecasting",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="STAT3660SEF",
        course_title="SAS Programming",
        credit=3,
        course_level=3000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="ENGL1101AEF",
        course_title="University English: Reading and Writing",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))

    mgr.add_course(Course(
        course_code="ENGL1202EEF",
        course_title="University English: Listening and Speaking",
        credit=3,
        course_level=1000,
        course_type="core",
        prerequisite=[],
        professor="",
        remark=""
    ))
load_all_course()

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





