import cmd
import json
import getpass

import requests
from click._compat import raw_input

class Client(cmd.Cmd):
    intro = 'Start Rating Service...Prompt "exit" to exit...'
    prompt = 'sc18y5h>'

    def do_list(self, arg):
        self.list()

    def do_view(self, arg):
        self.view()

    def do_average(self, arg):
        try:
            args = arg.split()
            self.average(args[0], args[1])
        except Exception:
            print("Follow the format \'average professor_id module_code\'")

    def do_rate(self, arg):
        try:
            args = arg.split()
            self.rate(args[0], args[1], args[2], args[3], args[4])
        except Exception:
            print("Follow the format \'rate professor_id module_code year semester rating\'")

    def do_register(self, arg):
        try:
            username = raw_input("Enter your username:")
            email = raw_input("Enter your email: ")
            pwd = getpass.getpass(prompt="Enter your password: ")
            self.register(username, email, pwd)
        except Exception as error:
            print(error)

    def do_login(self,arg):
        if arg != 'sc18y5h.pythonanywhere.com' :
            print("Invalid address!")
        else:
            try:
                username = raw_input("Enter your username:")
                pwd = getpass.getpass(prompt="Enter your password: ")
                self.login(username,pwd)
            except Exception as error:
                print(error)

    def do_logout(self,arg):
        self.logout()

    def do_exit(self, _):
        'Exiting now...'
        exit(0)

    def list(self):
        url = "http://127.0.0.1:8000/listAll/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            content = json.loads(response.text)
            print('Code          Name                  Year      Semester             Taught by          ')
            for row in content:
                code = row['m_code']
                name = row['m_name']
                year = row['m_year']
                semester = row['m_semester']
                prof = row['prof']
                for p in prof:
                    prof_code = p['p_code']
                    prof_name = p['p_name']
                    print('%-6s%-30s%-13s%-13s%-3s, Professor %-10s' % (code, name, year, semester, prof_code,prof_name))
                    code = ''
                    name = ''
                    year = ''
                    semester = ''
                print('-------------------------------------------------------------------------------')
        else:
            print(response.text)

    def view(self):
        url = "http://127.0.0.1:8000/ratingAll/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            content = json.loads(response.text)
            for row in content:
                p_name = row['p_Name']
                p_code = row['p_code']
                p_rating = row['rating']
                print("The rating of Professor " + p_name + ' (' + p_code + ') is ' + str(p_rating))
        else:
            print(response.text)

    def average(self, arg1, arg2):
        url = "http://127.0.0.1:8000/averageRating/p" + arg1 + "m" + arg2 + "/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                response.encoding = "utf-8"
                content = json.loads(response.text)
                for row in content:
                    p_name = row['p_Name']
                    p_code = row['p_code']
                    m_name = row['m_name']
                    m_code = row['m_code']
                    rating = row['rating']
                    print("The rating of Professor " + p_name + ' (' + p_code + ')' + " in module " + m_name + ' (' + m_code + ')' + " is " + str(rating))
            except Exception:
                print("Invalid code, try another one!")
        else:
            print(response.text)

    def rate(self, arg1, arg2, arg3, arg4, arg5):
        url = "http://127.0.0.1:8000/rate/p" + arg1 + "m" + arg2 + "y" + arg3 + "s" + arg4 + "r" + arg5 + "/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print("failed")

    def register(self,username, email, pwd):
        url = "http://127.0.0.1:8000/register/"
        data = {
            "username": username,
            "email": email,
            "pwd": pwd
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.post(url, data=json.dumps(data),headers=headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.text)

    def login(self,username,pwd):
        url = "http://127.0.0.1:8000/login/"
        data = {
            "username": username,
            "pwd": pwd
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.post(url, data=json.dumps(data),headers=headers)
        cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        s = requests.Session()
        s.cookies = cookies
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.text)

    def logout(self):
        url = "http://127.0.0.1:8000/logout/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) App1eWebKit/537.36 (KHTML; like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.text)

if __name__ == '__main__':
    Client().cmdloop()





