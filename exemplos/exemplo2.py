import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1} #filtro por postId
response = requests.get(url, params=params)
comments = response.json()
print(f'"{len(comments)} comments found"')
#print(response.json())
