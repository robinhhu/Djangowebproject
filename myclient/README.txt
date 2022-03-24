**********************************sc18y5h***************************************
##
##Client using instruction:
>>Move to the directory which contains the client.py file. It should be under 'sc18y5h/myclient/' directory
>>Activate the client program by typing into the shell 'python client.py'
##Command list:
>>register    This is used to allow a user to register to the service. After the command is invoked, the program 
prompts the user to enter username, email and password. If the username already exists, the program will prompt 
the user to enter another username. If the email address is not valid, which means not in a '***@***' form, the
program will ask the user to type in a valid email address. 
>>
>>login sc18y5h.pythonanywhere.com    This command is used to log in to the service. After the command is invoked,
the program will prompt the user to enter a username and password. If the identify is not authenticated successfully,
"Invalid username or password" will appear and the user should type in the username and password correctly. If the 
incorrect address is typed in, a 'Invalid address' will appear and the user should type in the right one
>>
>>logout    This allows the user to logout
>>
>>list    This command is used to view a list of all module instances and the professor teaching each of them
>>
>>view    This command is used to view the rating of all professors
>>
>>average professor_id module_code    The command is used to view the average rating of a certain professor in a 
certain module instance. For example, invoking 'average JE1 CD1' will appear the average rating of professor JE1 in 
module CD1. If one of the argument is missing, the program will ask the user to follow the format 
'average professor_id module_code'. Typing the wrong code that does not exist in the database will appear 
'Invalid code, try another one!'
>>
>>rate professor_id module_code year semester rating    This is used to rate the teaching of a certain professor in a 
certain module. However, if the user accidently mistype the argument, either 
'Follow the format 'rate professor_id module_code year semester rating' or 'Invalid object, try another one' will appear 
depending on the situation. The user should first login to activate the command. If the user is not logged in, the system 
will prompt the user to login first.
>>
>>exit    This command enables the user to exit the command line
>>
############################################################################################################################

##Name of the pythonanyther domain:  sc18y5h.pythonanywhere.com. But empty!!
>>If need to login to the admin site, enter directly

sc18y5h.pythonanywhere.com/admin

############################################################################################################################

##Admin username and password:

>>Username: csli
>>Pwd: 123456
