#This is code of kbc we get reward if the correct answer and lost when its wrong

print("Welcome To Kaun Banega Corepati")
print('\n')
name=(input("Enter Your Name:"))
print("Hi",name,"Are You Ready To Play")
Ques=("Q1.When Does India Got Its Independence ?")
option=(" \n a)1956 \n b)1947 \n c)1950 \n d)None Of The Above")
enter=input("Enter Yes or No:")
if [enter=="Yes","yes"]:
print(Ques)

elif (enter=="No","no"):
print("ThankYou Have A Nice Day ")

print(option)
Answer=input("Enter The Correct Option:")
if(Answer=='1947'):
print("The Answer is Correct\n \n You Won 100 rupees Cheque")
else:
print("The Answer is Wrong \n \n You Lost The Game")
