import requests
import json

def get_access_token(client_id, client_secret, refresh_token):
    url = "https://api.dropboxapi.com/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to obtain access token: {response.content}")

def download_file(access_token, remote_file_path, local_file_path):
    url = "https://content.dropboxapi.com/2/files/download"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Dropbox-API-Arg": json.dumps({"path": remote_file_path})
    }

    response = requests.post(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(local_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)
    else:
        raise Exception(f"Failed to download file: {response.content}")

def main(client_id, client_secret, refresh_token, remote_file_path, local_file_path):
    access_token = get_access_token(client_id, client_secret, refresh_token)
    download_file(access_token, remote_file_path, local_file_path)

if __name__ == "__main__":
    client_id = ""
    client_secret = ""
    refresh_token = ""
    remote_file_path = ""
    local_file_path = ""
    
    main(client_id, client_secret, refresh_token, remote_file_path, local_file_path)

