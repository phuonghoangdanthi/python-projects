import base64
import io
import requests
from PIL import Image
def get_byte_img(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img
api_key = 'c029d7886eb24eb8b4e51d764bea5046'
api_secret = 'db91784269c91fbaf0c8cd78cabf95cfce133280b8ea8f86aa624aa7e6d8109a'
img_path = "C:/Users/hungp/Documents/learnpython/pythonProject/image/2012_front-id-card.jpg"
encode_img = get_byte_img(Image.open(img_path))
response = requests.post(
    "https://demo.computervision.com.vn/api/v2/ocr/card?format_type=base64&get_thumb=false",
    auth=(api_key, api_secret),
    json={'img' : encode_img})
print(response.json())