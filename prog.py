import sys



print("\n")
print("Course Selection Assistance\n")
print("Login / Sign up(1)\n")
print("Course Information Inquiry(2)\n")
print("Timetable(3)\n")
print("Credit Calculation Plan(4)\n")
print("GEN Subject Suggestion(5)\n")
print("Personal Data Overview(6)\n")

ans = input()


if ans == 1:
    login_function()
elif ans == 2:
    courseinfo_function()
elif ans == 3:
    time_function()
elif ans == 4:
    credit_function()
elif ans == 5:
    gen_function()
elif ans == 6:
    overview_function()
else:
    sys.exit()



