# cool api example
import requests

def bypass(url):
  payload = {
    "url": url,
  }

  r = requests.post("https://api.bypass.vip/", data=payload)
  return r.json()


if __name__ == '__main__':
  print('Link: ')
  result = bypass(input())  # include url to bypass
  resultvar = repr(result)
with open('output4awesomeprogram.txt','w',encoding = 'utf-8') as f:
   f.write(resultvar)
   print('Check txt for your bypass!')
