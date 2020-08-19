import requests

url = 'http://webservice.forclass.net/ForClassService.asmx/Userlogin?'
data = 'account=rd0006&password=jQ7qCVbbvtJGHu2qEwsNFA==%20&xStr={"timestamp":"1563792715"}&typeIdx=1'
response = requests.get(url + data)
print(response.text)

# session = getsession(response.text)
# print(session)
# str1 = "".join(session)
# bytes_session = str1.encode("utf-8")
# str_session = str(base64.b64encode(bytes_session),'utf-8')
# print('Bearer '+str_session)