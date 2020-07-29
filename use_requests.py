import requests
requests.get('https://detik.com')

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'success {response}')
    print(f'Content {response.text}')
except Exception as e:
    print('There is an error' , e)
print('Program ended')
