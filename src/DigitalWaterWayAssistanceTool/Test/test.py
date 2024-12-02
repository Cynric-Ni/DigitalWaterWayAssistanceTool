import requests


def get_auth_token(app_id, app_secret):
    url = "http://172.18.100.216/api/blade-auth/ext/api/api/oauth/token"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        'Connection': 'keep-alive',
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    payload = {
        "tenantId": "999999",
        "clientId": f"${app_id}$",
        "clientSecret": f"${app_secret}$",
        "grantType": "client_credentials"  # Assuming 'grantType' is needed and it's 'client_credentials'
        #"grantType":"api"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        token_data = response.json()
        print(token_data.get('access_token'))
        return token_data.get('access_token')
    except requests.RequestException as e:
        print(f"Failed to obtain token: {e}")
        return None


def get_data_by_config(api_token, config_id):
    url = "http://172.18.100.216/api/datacenter/dataapiCfg/dc/getDataByConfigApi"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    params = {
        "configId": config_id
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None

#get_auth_token('3A3885B032A98A5415ABF4D9D286DB5F','62F45543C8BA2281582FDDAE0FC6D007')
get_auth_token('65ABFC56CA9C7FAFDF7A2E599F6C392B','942846F01B9657F257D1843FD303706A')
