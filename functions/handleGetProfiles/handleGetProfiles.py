import requests


def handleGetProfileIdsFromGoLogin():
    try:
        api_token_gologin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGNjZDc0MDlhYmQxMjM4NjUzYjdjYTQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGNjZDc2ZGJlNWU1ZTJkMGQ4NjA1NjAifQ.v-x_VxW3tmxbH6Dch1gja57jn5uWLdBQ3NbwmrB2NZY"
        userDataDirs = []

        url = "https://api.gologin.com/browser/v2"
        headers = {
            "Authorization": f"Bearer {api_token_gologin}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        for profile in data["profiles"]:
            userDataDirs.append(
                f"C:/Users/HD/AppData/Local/Temp/GoLogin/profiles/{profile['id']}/Default"
            )

        return userDataDirs

    except requests.exceptions.RequestException as e:
        print(e)
