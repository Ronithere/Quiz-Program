# Created by = Ronit
# github username = Ronithere
from time import sleep
print("Welcome To Quiz Program In Hindi by Ronit")
print('\n')
name=(input("Tumhara Name Kya Hai : "))
print("Hi",name,"Jawab de paoge ? ")
Ques=("Q. PUBG PC konse coding language me banaya tha ? ?")
option=(" \n python \n c++ \n java \n None")
enter=input("Enter Ha or Nahi:")
if [enter=="Haa","Haa"]:
    print("badhiya toh yeh hai sawal: ")
    print("loading...")
    sleep(2)
    print(Ques)

elif (enter=="Nahi","Nahi"):
    print("koi baat nahi, Bye")

print(option)
Answer=input("Sahi option choose kar:")
if(Answer=='c++'):
    print("ruk...")
    sleep(2)
    print("sahi jawab \n Tumhe 100 points milte hai")
else:
    print("ruk...")
    sleep(2)
    print("Galat jawab \n Tum Hargaye")
