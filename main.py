# Author: Daniel Mikita djm6907@psu.edu

def getGradePoint(grade):
  if (grade == 'A'):
    return 4.0
  elif (grade == 'A-'):
    return 3.67
  elif (grade == 'B+'):
    return 3.33
  elif (grade == 'B'):
    return 3.0
  elif (grade == 'B-'):
    return 2.67
  elif (grade == 'C+'):
    return 2.33
  elif (grade == 'C'):
    return 2.0
  elif (grade == 'D'):
    return 1.0
  else:
    return 0.0 

def run():
  letter1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credits: ")
  credit1 = float(credit1)
  print(f"Grade point for course 1 is: {getGradePoint(letter1)}.")

  letter2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credits: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2 is: {getGradePoint(letter2)}.")
  

  letter3 = input("Enter your course 3 letter grade:  ")
  credit3 = input("Enter your course 3 credits: ")
  credit3 = float(credit3)
  print(f"Grade point for course 3 is:  {getGradePoint(letter3)}.")
  
  GPA = (getGradePoint(letter1) * credit1 + getGradePoint(letter2) * credit2 + getGradePoint(letter3) * credit3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}")
  

if __name__== "__main__" :
  run()
