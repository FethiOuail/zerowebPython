

email = input('Enter your email: ').strip().lower()

username = email[:email.index("@")]
website = email[email.index("@")+1: ]



print(f'hello {username}' )

print(f'Your web site is  {website}' )


