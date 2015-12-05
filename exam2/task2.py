import requests
import re

with open("links.txt", "r") as l:
    with open("email_addresses.txt", "w")as adrs:
        list_e_mails = list()
        for link in l:
            response = requests.get(link)
            mails = response.text
            e_mail = re.findall('\w+@\w+\.\w+', mails)
            if e_mail != []:
                for i in e_mail:
                    if i not in list_e_mails:
                        list_e_mails.append(i)
        for i in list_e_mails:
            adrs.write(str(i) + "\n")
