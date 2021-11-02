import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {   "aluminium": 1.65,
 	"ammonia":9.08,
    "arsenic":0.04,
    "barium":2.85,
    "cadmium":0.007,
    "chloramine":0.35,
    "chromium":0.83,
    "copper":0.17,
    "flouride":	0.05,
    "bacteria":0.20,
    "lead":	0.054,
    "nitrates":16.08,
    "nitrites":1.13,
    "mercury":	0.007,
    "perchlorate":37.75,
    "radium":	6.78,
    "selenium":0.08,
    "silver":0.34,
    "uranium":0.02	
 }


response = requests.post(url, json=customer).json()
print(response)

if response['is_safe'] == 1:
    print('water is safe to drink')
else:
    print('water is not safe to drink')



 