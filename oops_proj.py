class chatbook:
    def __init__(self):
        self.username= ''
        self.password= ''
        self.logged= False
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
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

obj = chatbook()