"""
Corey Lambert
Date written: 8/30/2024
File Name: Student_GPA.py
    This Program is to calculate a students achievements via GPA
    It accepts a users input of last name and first name. Then accepts the students GPA. Tehn runs through a loop to test if
    it reaches the levels of Deans list or Honor roll. Outputing the result.
"""



def main():
    
    while True:
        last_name = input("Enter Student's Last Name, or (ZZZ to Quit):") # input prompt with quit key
        
        if last_name == 'ZZZ':
            break # break statement to end if quit key entered
        first_name = input("Input Student's First Name:")
        # prompt for GPA allowing float input
        student_gpa = float(input("Enter Student's GPA:")) #
        # Loop for testing if GPA meets Criteria
        if student_gpa >= 3.5:
            print(f"{first_name} {last_name} has acheived the Dean's List")
        
        elif student_gpa >= 3.25:
            print(f"{first_name} {last_name} has achieved the Honor Roll")
        # if neither criteria are met outputs names and Grade
        else:
            print(f"{first_name} {last_name} has a GPA of {student_gpa}")

if __name__ == "__main__":
    main()
