import requests

API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/attendance/"

data =
{
    'username':'1'
}
r = requests.post(url = API_ENDPOINT,data=data)
print(r)