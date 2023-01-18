import mmh3
import requests
import base64


response = requests.get('https://developer.harmonyos.com/assets/image/favicon.ico')   ##输入域名
favicon = base64.b64encode(response.content)
print(favicon) ##校验
hash = mmh3.hash(favicon)
print ('icon_hash='+str(hash)) ##前缀为fofa语法