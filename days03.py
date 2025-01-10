# import os 


# os.mkdir ('folder02')
# a = os.listdir ('.')

# print(a)

# deleted file and remove the directry
# import os.path
# import os   

# x = os.pat    h.exists('susan.txt')
# print('the existance of file susan.txt id : ', x)
# a = os.listdir('.')

# os.rmdir('folder02')
# os.mkdir('folder01')



#input method  


# a = input("enter your name :")

# print("User Entered number:", a)

# age = int(input("ENTER YOUR AGE :  "))

# if age >= 18:
#     print("user is adult")
# # elif age == 18:
#     # print("user is adult")
# else:
#     print("user is not adult")


score = int(input("ENTER YOUR score :  "))

if score >= 100:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 50:
    print("Grade : C")
else:
    print("Grade : D")
