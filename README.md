# Djangowebproject
The Django server code is uploaded to pythonanywhere. The backend service is now running on sc18y5h.pythonanywhere.com（but the server may have expired）. Courses and professors can be added here using admin account

## project structure
backend-Django

frontend-command line

## how to use(if the account is still active!)
Move to the directory which contains the client.py file. It should be under 'sc18y5h/myclient/' directory. Then activate the client program by typing into the shell 'python client.py'.
1.	**register** is used for users to register. The program prompts the user to enter username, email and password. If the username already exists, the program will prompt the user to enter another username. If the email address is not valid (in '***@***'), the program will ask the user to type in another valid email address. 
2.	**login sc18y5h.pythonanywhere.com** is used to log in to the service. The program will prompt the user to enter a username and password. If the identify is not authenticated, "Invalid username or password" will appear and the user should type in the username and password correctly. If the incorrect address is typed in, a 'Invalid address' will appear and the user should type in the right one
3.	**logout** allows the user to logout
4.	**list** is used to view a list of all module instances and the professor teaching each of them
5.	**view** is used to view the rating of all professors
6.	**average professor_id module_code** is used to view the average rating of a certain professor in a certain module instance. E.g. ‘average JE1 CD1' show the average rating of professor JE1 in module CD1. The program will ask the user to follow the format 'average professor_id module_code' if the format is wrong. Typing the professor or module code that does not exist will appear 'Invalid code, try another one!'
7.	**rate professor_id module_code year semester rating** is used to rate the teaching of a certain professor in a certain module. However, if the user accidently mistypes the argument, either 'Follow the format 'rate professor_id module_code year semester rating' or 'Invalid object, try another one' will appear. If the user is not logged in, the system will prompt the user to login first.
8.	**exit** enables the user to exit the command line
