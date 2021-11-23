import requests
import sys
url = "https://api.exchangeratesapi.io/latest?base="
#url = "https://finans.truncgil.com/today.json"
birinci_doviz = input("birinci doviz:")
ikinci_doviz = input("ikinci doviz:")
miktar = float(input("miktar"))
response = requests.get(url + birinci_doviz)
veri = response.json()

try:
    print(float(veri["rates"][ikinci_doviz])*miktar)
except KeyError:
    sys.stderr.write("Dogru degeri girin")
    sys.stderr.flush()
"""
#orn2
"""
import requests
import sys

url = "http://data.fixer.io/api/latest?access_key=f52e0f6a00e6506b3e8d338ca6f322ba"

birinci_doviz = input("birinci doviz:")
ikinci_dovz = input("ikinci doviz:")
miktar = int(input("miktar"))

response = requests.get(url)
veri = response.json()

first_value = veri["rates"][birinci_doviz]
secondry_value = veri["rates"][ikinci_dovz]

try:
    print((secondry_value / first_value) * miktar)
except KeyError:
    sys.stderr.write("Dogru degeri girin")
    sys.stderr.flush()