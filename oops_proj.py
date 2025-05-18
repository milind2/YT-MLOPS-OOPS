class chatbook:
    def __init__(self):
        self.username= ''
        self.password= ''
        self.loggedin= False
        self.menu()
    
    def menu(self):
        user_input = input('''welcome to chatbook !! , How would you like to proceed ? 
        1.Press 1 for signup  
        2.Press 2 for signin 
        3.Press 3 for write a post
        4.Press 4 to message friend
        5.Press any other key to exit'''
        )

        if user_input == '1':
            self.signup()
            pass
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

    def signup(self):
        email = input('enter your email here -->')
        pwd = input('setup your password here -->')
        self.username = email
        self.password = pwd
        print('YOu have signed up   successfully')
        print("/n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print('sigup first by pressing 1 in main menu')
        else:
            uname = input('enter your email/username here -->')
            pwd = input('enter your password  here -->')
            if self.username == uname and self.password == pwd:
                print("you have signed in successfully")
                self.loggedin = True
            else:
                print("Please enter correct credentials")
        print("\n")
        self.menu()

obj = chatbook()

