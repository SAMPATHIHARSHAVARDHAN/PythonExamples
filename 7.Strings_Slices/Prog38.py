#Note:before use of camelcase
# we must install pip install camelcase in terminal
import camelcase
c = camelcase.CamelCase()
txt = "hello srinviasarao kunchala how are you"
print(c.hump(txt)) #Title Case
print(txt.lower()) #lowecase
print(txt.upper()) #uppercase