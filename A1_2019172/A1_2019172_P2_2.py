import random

#here i take a password length btw 8 to 20 for my safe side
passWrdLen = random.randint(8,20)
# here i take all characters which have i used for creating a password
match = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&!0123456789'

upper = random.randint(1,passWrdLen-1) # for upper btw 1 to len-1
spChar = random.randint(1,passWrdLen-1) # same as above
digit = random.randint(1,passWrdLen-1)  # same as above

# i make while for checking a if any upper or spChar or digit have a same random
# number then it will change his index value 
while(upper == spChar or upper == digit or spChar == digit):
  if(upper == spChar):
    upper = random.randint(1,passWrdLen-1)
  elif(upper == digit):
    upper = random.randint(1,passWrdLen-1)
  elif(spChar == digit):
    digit = random.randint(1,passWrdLen-1)

password = '' # creating a empty password
# runs a loop for making a password
for i in range(passWrdLen):
  if(i==0 or i==passWrdLen-1):# if 0 or len-1 then it will added to lower in password
    password = password + match[random.randint(0,25)]
  elif(i==upper): # if upper then it will added to upper in password
    password = password + match[random.randint(26,51)]
  elif(i==spChar):  # if spChar then it will added to spcHar in password
    password = password + match[random.randint(52,56)]
  elif(i==digit): # if digit then it will added to digit in password
    password = password + match[random.randint(57,len(match)-1)]
  else: # else then it will added to any character in password
    password = password + match[random.randint(0,len(match)-1)]

print(password)   # print the password
#print(solve(password))    # it checks it correct or not but it always true 
                          # it generates a secure password
                          # solve function in A1_2019172_P2_1