from requests import request

class APICall():
  
    def __init__(self, url):
        self.url = url
        self.ipdetail = request("GET", url).json()

    def ipInfo(self):
        return self.ipdetail


ipaddr = APICall("https://api.ipify.org/?format=json").ipInfo()
print('Your ip address is : ', ipaddr)

ipdetail = APICall(f'https://ipinfo.io/{ipaddr["ip"]}/geo').ipInfo()
print('Other Details\n')

for i, k in ipdetail.items():
    print(i, " : ", k)
