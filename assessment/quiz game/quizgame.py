
d={}

a="                 WELCOME TO QUIZ GAMING CHALLENGE               "
print(a)

# while True:
menu="""
            select your role : 

                        -> Quiz master  (press 1)
                        -> Quiz cracker (press 2)


         """
print(menu)

n=int(input("enter your role :"))
if n==1:
 print("---------------WELCOME MASTER--------------")
 print(" SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS..")

 while True:
  menu="""
    press 1 for add questions
    press 2 for view questions
    press 3 for delete questions 
    press 4 for exit
        """
  print(menu)
  choice=int(input("Which operation you want to perform : "))

  if choice==1:
        q_no=int(input("enter question number :"))
        question=input("Enter question : ")
        optionA=input("Enter op 1 : ")
        optionB=input("Enter op 2 : ")
        ans=input("Enter right answer : ") 

        d[q_no] = {
           'question':question,
           'B':optionA,
           'A':optionB,
           'ans':ans
           }
        print("question added sucessfully !!")

  elif choice==2:
           if not d:
               print(" no questions added yet. ")
           else:   
            print("quetions are : ")
           
           for no,data in d.items():
               print(f"{no}) {data['question']}")
               print(f" A: {data['A']}")
               print(f" B: {data['B']}")
               print(f" right ans: {data['ans']}")


               
           
  elif choice==3:
      enter=int(input("enter the quetions number for delete : "))
      if enter in d:
          
          confirm = input("sure to delete qiestio? (yes/no):")
          
          if confirm=="yes":

            d.pop(enter)
            print("delete sucessfully !!")

          else:
              print("cancelled.")
      else:
          print("quetion is not found ")



  elif choice==4:
      print("thank you !!")
      break
  else :
      print("invalid choice !! ")

else :
    print("invalid choice")