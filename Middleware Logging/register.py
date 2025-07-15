import requests

url = "http://20.244.56.144/evaluation-service/register"

data = {
    "email": "ashishpadiyar92@gmail.com",
    "name": "Ashish Padiyar",
    "mobileNo": "8958758377",
    "githubUsername": "ashish220111331",
    "rollNo": "2218510",
    "accessCode": "QAhDUr"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except:
    print("Response Text:", response.text)
