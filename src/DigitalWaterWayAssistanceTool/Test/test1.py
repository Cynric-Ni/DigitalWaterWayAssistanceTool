import requests

def get_data_by_config():
    url = "http://172.18.100.216/api/blade-auth/ext/api/api/oauth/token"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
        'Connection': 'keep-alive',
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    payload = {
        'tenantId': '999999',
        'clientId': '65ABFC56CA9C7FAFDF7A2E599F6C392B',
        'clientSecret': '942846F01B9657F257D1843FD303706A',
        'grantType': 'api'
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    access_token = result['data']['access_token']
    print(access_token)

    url = 'http://172.18.100.216/api/datacenter/dataapiCfg/dc/getDataByConfigApi'
    params = {
        'cfgName': '数字航道TO武汉局主中心航道保护工作信息'
    }
    headers["Blade-Auth"] = access_token
    response = requests.post(url, headers=headers, json=params)
    print(response.json())
    return response.json()

get_data_by_config()