# auth.py
import requests

def get_access_token():
    url = "http://20.244.56.144/evaluation-service/auth"

    data = {
        'email': 'ashishpadiyar92@gmail.com',
        'name': 'ashish padiyar', 
        'rollNo': '2218510', 
        'accessCode': 'QAhDUr', 
        'clientID': 'd085ec92-b309-41da-914f-187c2caef94d', 
        'clientSecret': 'QhacHjwytSgUFMSd'
    }

    response = requests.post(url, json=data)

    if response.status_code == 201:
        return response.json().get('access_token')
    else:
        print("Token fetch failed!")
        print("Status Code:", response.status_code)
        try:
            print("Response:", response.json())
        except:
            print("Response Text:", response.text)
        raise Exception("Could not get access token")
