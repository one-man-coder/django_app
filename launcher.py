import os
import webbrowser
project = input("enter project name : ")
command = "python {}/manage.py runserver".format(project)
os.system(command)
webbrowser.open("http://127.0.0.1:8000/")
