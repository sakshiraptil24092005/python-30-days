email = input("enter your email:")
if "@" in email:
    username,domain = email.split("@",1)
    print( f"username:{username}")
    print( f"domain: {domain}")
else:
    print("invalid email")
