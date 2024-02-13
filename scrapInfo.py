from requests import get
import re


class EmailScrap():
    def __init__(self, filename) -> None:
        self = filename
        # display message
        print("Email scraping started")
        print("Scrapping.....")

    def find(self):
        Emailoutput = open('Email.csv', 'w')
        Mobileoutput = open('MobileNo.csv', 'w')
        # open file to read urls
        with open(filename, 'r') as linkFile:
            urls = linkFile.read()
            for url in urls.split():
                # Get http get response from web
                response = get(url).text.split()
                for word in response:
                    # match special condition for email and phone number
                    if re.match(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t-Z^-~]*])", word):
                        Emailoutput.write(str(word) + '\n')
                    elif re.match(r"^(?:\+?)?[79]\d{9}$", word):
                        Mobileoutput.write(str(word) + '\n')

        print(" Done Email scraping!  ")

    def displaydata():  # display scrapped data
        print("Display Scrapped data ?")
        temp = input('Y for YES , if no then Enter any other key ')
        if temp == 'y' or temp == 'Y':
            with open('Email.csv', 'r') as file:
                read = file.read().split()
                for email in read:
                    print(email)

            with open('MobileNo.csv', 'r') as file:
                read = file.read().split()
                for number in read:
                    print(number)
        input('Enter any key to exit ')


filename = input('Enter urls file name Or path : ')
getInfo = EmailScrap(filename).find()
getInfo = EmailScrap.displaydata()
