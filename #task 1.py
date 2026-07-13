#task 1


mainpassword ="Mo@1234"
tries = 4

inputpassword = input ("Enter your password :")
while  inputpassword !=  mainpassword  :
    tries -=1
    if tries == 0:
         print("All tries is finished")
         break
     
    print(f"wronge information , {'last'if tries==0 else tries} chance left")
    inputpassword = input ("Enter your password :")
if inputpassword == mainpassword :
    print("correct password , welcom!")


