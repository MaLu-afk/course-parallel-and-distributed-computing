## ***1. Operaciones limitadas por E/S y por CPU***

```python
import requests

response = requests.get('https://www.example.com/')
items = response.headers.items()
headers = [f'{key}: {header}' for key, header in items]
formatted_headers = '\n'.join(headers) 

with open('unit_1/week_1/headers.txt', 'w') as file:
 file.write(formatted_headers)
```

