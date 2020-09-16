import time
from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts"   # enter your path ( C drive -> windows -> system32 -> drives -> etc -> hosts )
redirect = "127.0.0.1"

website_list = ['www.instagram.com', 'instagram.com', 'www.facebook.com',  
                'facebook.com', 'www.pinterest.com', 'pinterest.com']        # enter websites which you want to block during working time

starting_time = dt(dt.now().year, dt.now().month, dt.now().day, 12)         # enter starting time  
ending_time = dt(dt.now().year, dt.now().month, dt.now().day, 20)           # enter ending time
current_time = dt.now()                                                     # current time    

while True:
    if starting_time < current_time < ending_time:
        with open(host_path, 'r+') as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

        print("All Websites are Blocked !!!!")
        break

    else:

        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):

                    file.write(line)

            file.truncate()

        print("All Websites are Unblocked!!!!")
        break
