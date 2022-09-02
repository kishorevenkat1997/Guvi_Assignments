import re                              
import string as s
def register():
    try:                              # this try and except is used because sometime user may dont have a database so i have created if there is none
        data = open("data.txt", "r")
    except:
        data = open("data.txt",'x')
    data.close()
    data = open("data.txt",'r')
    #username validation
    username = input("Enter New UserName:")
    letter = [x for x in s.ascii_letters]       # generated all letters using list comprehension
    if username[0] in ('0123456789'):
        print("Username should not start with a number")
        register()
    elif username[0] not in letter:
        print('Username should start with a letter')
        register()
    elif username[-1] not in letter:
        print('Use .com or valid extension dont use Number or special character[@$!%*#?&] At the End')
        register()
    count = 0
    for q in username:                                    #here i am counting only the username length
        if q =="@":
            break
        else:
            count += 1
    #print(count)
    if count < 5:
        print('Username is too short')
        register()
    elif count >16:
        print('username is too long')
        register()
    else:
        pass
    username_pattern = re.compile(r"([a-zA-z]+)([0-9]?)@([a-zA-Z]+)\.([a-zA-z+])")
    compile1 = username_pattern.search(username)
    if compile1:
            pass
    else:
        print("Invalid Username Use Proper Format")
        register()
    #password validation
    def password():
       pswd = input("Enter Password:")
       pswd1 = input('Enter Again To Conform:')

       reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
       match_re = re.compile(reg)
       res = re.search(match_re,pswd)
    # data entered in to the db
       if pswd == pswd1:
           if len(pswd) < 5:
               print("Paswword is too short")
               password()
           elif len(pswd) > 16:
               print("Password is too long")
               password()
           elif res:
             data = open('data.txt','a')
             data.write(username+','+pswd+'\n')
           else:
               print("Invalid Password!","\n"," Check Length and Use Minimum one uppercase ,one lowercase,one digit,one special character[@$!%*#?@] to validate your password","\n","Try again!")
               password()
       else:
          print("Password Doesn't Match","\n","try again!")
          password()
       return
    password()

    user_list = []
    pass_list = []
    for i in data:
        a,b = i.split(",")
        b = b.strip()
        user_list.append(a)
        pass_list.append(b)
    dict_data = dict(zip(user_list,pass_list))
    #print(dict_data)
    print("User Created Successfully! know You can Login!")
    a=input('If you want to continue to login? press 1 else press 2 to terminate:')
    if a == '1':
        access()
    else:
        pass
    return

def access():
    try:  # this try and except is used because sometime user may dont have a database so i have created if there is non
        data = open("data.txt", "r")
    except:
        data = open("data.txt", 'x')
    username = input("Enter Username:")
    password = input("Enter Password:")
    if not len(username or password) < 1:
        user_list = []
        pass_list = []
        data = open('data.txt','r')
        for i in data: #re creating the dict data to check login details
            if i in (' '):
                pass
            else:
                a, b = i.split(",")
                b = b.strip()
                user_list.append(a)
                pass_list.append(b)
    else:
        print('Username or Password cannot be left empty')
        access()
    dict_data = dict(zip(user_list,pass_list))
    try:
        if dict_data[username]:
            try:
                if password == dict_data[username]:
                    print('Login Successfull')
                    print("Hi",username)
                else:
                    print('incorrect password','\n','Press 1 to Retrive Original Password.','\n','Press 2 to make new Password.')
                    num = int(input("Enter A Number:"))
                    if num == 1:
                        again_name = input("Enter Username To Retrieve Old password:")
                        if dict_data[again_name]:
                            print('Your password is:',dict_data[again_name])
                        else:
                            print("User doesn't exit Redirecting to New User Registration." )
                            register()
                        access()
                    elif num ==2:
                        def newpass():
                            name_valid = input('Enter username to check in Database:')
                            if name_valid in dict_data:
                                new_pass = input('Enter Your New Password:')
                                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
                                match_re = re.compile(reg)
                                res = re.search(match_re, new_pass)
                                if res:
                                    with open('data.txt','r') as file:
                                        filedata = file.read()
                                    filedata = filedata.replace(username+','+dict_data[username],username+','+new_pass)
                                    with open('data.txt','w') as file:
                                        file.write(filedata)
                                        file.close()
                                else:
                                    print("Invalid Password!","\n","Use Minimum one uppercase ,one lowercase,one digit,one special character to validate your password","\n","Try again!")
                                    newpass()
                            else:
                                print('Username Was Not found in the Database!','\n','Redirecting to Registration Page!')
                                register()
                            print("New Password Updated Sucessfully.",'\n','Your new Password is:',new_pass,'\n','Run the Program again to login with New Password')
                            data.close()
                        newpass()
                    else:
                        print("You have entered invalid number.")
                        access()
            except:
                print('')
        else:
            print("Username Doesn't exit",'\n','Press 1 to Register (or) Press 2 to try login again:',)
            num1 = input('Enter:')
            if num1 == '1':
                print('You are Redirected To New User Registration!')
                register()
            elif num1 == '2':
                access()
            else:
                print('Invalid input')
                access()
    except:
        print("Username Doesn't exit", '\n', 'Press 1 to Register (or) Press 2 to try login again:', )
        num1 = input('Enter here:')
        if num1 == '1':
            print('You are Redirected To New User Registration!')
            register()
        elif num1 == '2':
            access()
        else:
            print('Invalid input.')
            access()
def welcome():
    print('Welcome to guvi sample login portal build on python.Submitted by Kishore Venkat','\n',"Press 1 to Register User",'\n',"Press 2 to login for existing user:")
    num = input("Choose your Option:")
    if num == '1' :
        register()
    elif num == '2' :
        access()
    else:
        print("invalid input")
        welcome()
# here i have created default user id and password
'''try:
    data = open("data.txt", "r")
except:
    data = open("data.txt",'x')
    try:
        data = open('data.txt','r')
    except:
        print('default user creation erro')
default_user = 'guvigeek@gmail.com,Guvi@123'
if default_user not in data:
    data = open('data.txt','a')
    data.write('guvigeek@gmail.com,Guvi@123'+'\n')
    data.close()'''
welcome()
