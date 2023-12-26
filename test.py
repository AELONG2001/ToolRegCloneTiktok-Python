import requests
from io import BytesIO
import base64
import time

key = '837c315533f8364a1e90b21de86ea148'
url1 = 'https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/14f6e22582754d0a8378529e62b31630~tplv-b4yrtqhy5a-2.jpeg'
url2 = 'https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/6cb5c78e040f4166ad9106c625a9dc22~tplv-b4yrtqhy5a-2.jpeg'

ur1_bytes = url1.encode('utf-8')
ur2_bytes = url2.encode('utf-8')

ee1 = base64.b64encode((ur1_bytes))
ee2 = base64.b64encode((ur2_bytes))

payload = {'textinstructions': 'koleso', 'click': 'geetest', 'key': key, 'method': 'base64', 'body0': ee1, 'body1': ee2}
res = requests.post("http://api.cap.guru/in.php", data=payload)

time.sleep(10)

rt = res.text.split('|')
url = 'http://api.cap.guru/res.php?key='+key+'&id='+rt[1]

response = requests.get(url).text
print(response.split("|")[1].split('y=')[1])