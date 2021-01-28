def my_function(**kwargs):
    return kwargs


print(my_function(Name=input('Name'), Second_name=input('Second name'), Date=int(input('Date')), city=input('City'),
                  email=input('Email'), phone=int(input('Phone'))))
