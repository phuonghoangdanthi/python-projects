import requests

api_key = 'c029d7886eb24eb8b4e51d764bea5046'
api_secret = 'db91784269c91fbaf0c8cd78cabf95cfce133280b8ea8f86aa624aa7e6d8109a'
front_path = 'C:/Users\hungp\Documents/learnpython/pythonProject/image/image_2022-12-05_17-49-36.png'
back_path = 'C:/Users\hungp\Documents/learnpython/pythonProject/image/image_2022-12-08_17-23-36.png'

response = requests.post(
  "https://demo.computervision.com.vn/api/v3/ekyc/cards?format_type=file&get_thumb=false",
  auth=(api_key, api_secret),
  files={'img1': open(front_path, 'rb'), 'img2': open(back_path, 'rb')})

print(response.json())
