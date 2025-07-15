import requests
from auth import get_access_token

API_URL = "http://20.244.56.144/evaluation-service/logs"
ACCESS_TOKEN = get_access_token()

VALID_STACKS = {"frontend", "backend"}
VALID_LEVELS = {"debug", "info", "warn", "error", "fatal"}
VALID_PACKAGES = {"api", "component", "hook", "page", "state", "style"}

def log(stack, level, package, message):
    global ACCESS_TOKEN

    # ✅ Validation checks
    if stack not in VALID_STACKS:
        print(f"[!] Invalid stack: '{stack}'. Must be one of {VALID_STACKS}")
        return
    if level not in VALID_LEVELS:
        print(f"[!] Invalid level: '{level}'. Must be one of {VALID_LEVELS}")
        return
    if package not in VALID_PACKAGES:
        print(f"[!] Invalid package: '{package}'. Must be one of {VALID_PACKAGES}")
        return

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            print("[✓] Log sent successfully")
        elif response.status_code == 401:
            print("[!] Token expired — refreshing...")
            ACCESS_TOKEN = get_access_token()
            headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
            retry_response = requests.post(API_URL, json=payload, headers=headers)
            print(f"[Retry] Status: {retry_response.status_code}")
            print("Response:", retry_response.text)
        else:
            print(f"[!] Log failed: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("[X] Request failed:", str(e))
