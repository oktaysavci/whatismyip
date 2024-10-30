import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except Exception as e:
        return f"Hata oluştu: {e}"

print("IP Adresiniz:", get_public_ip())
