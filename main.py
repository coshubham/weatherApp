import requests       # network through we bring infomation
import json           # string convert in dictionary
import win32com.client as wincom

while True:
    city = input("Enter the name of city\n")


    url = f"https://api.weatherapi.com/v1/current.json?key=6adccab46911454d9a460133232907&q={city}"

    speak = wincom.Dispatch("SAPI.SpVoice")
    r = requests.get(url)
    if city == "y":
        text = "Bye Bye Friends"
        speak.Speak(text)
        break
    # print(r.text)
    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]

    speak.Speak(f"The current weather in {city} is {w} degrees")
    print(wdic["current"]["temp_c"])