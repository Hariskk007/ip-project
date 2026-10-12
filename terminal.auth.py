import database_control as db
print("===========================================")
print("     THE FORGE | SYSTEM AUTHENTICATION     ")
print("===========================================")

run_system = True

while run_system:
    print("\n--- MAIN MENU ---")
    print("1. INITIALIZE UPLINK (Login)")
    print("2. NEW OPERATOR (Register)")
    print("3. EXIT")
    
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print("\n--- LOGIN SEQUENCE ---")
        email = input("Enter Email (athlete@gmail.com): ").strip()
        username=input("Enter your user_name").strip()
        password = input("Enter Access Code: ")

        if password == "ENTERASADMIN" and username=="admin":
            "main.admin()"
        # Validation checks
        if email == "" or password == "" or username == "":
            print("ERROR: INCOMPLETE DATA")
        
        else:
            print("VERIFYING CREDENTIALS...")
            a=db.find(username,password)
            if a:
                print("ACCESS GRANTED. WELCOME BACK,", username.upper())
            else:
                print("THE USER DOES NOT EXIST")



    elif choice == '2':
        print("\n--- REGISTRATION PROTOCOL ---")
        email = input("Enter New Email (athlete@gmail.com): ").strip()
        username=input("Enter your user_name").strip()  
        new_pass = input("Create Access Code: ")
        confirm_pass = input("Confirm Access Code: ")
                
        if len(new_pass) < 4:
            print("ERROR: CODE TOO SHORT")
        elif new_pass != confirm_pass:
            print("ERROR: CODES DO NOT MATCH")
        else:
            print("IDENTITY FORGED. RETURNING TO UPLINK...")
            db.create_user(email, username, confirm_pass, role)


    elif choice == '3':
        print("SHUTTING DOWN SYSTEM...")
        run_system = False
        
    else:
        print("INVALID INPUT. PLEASE ENTER 1, 2, OR 3.")
