import requests, json, sys, urllib.request

api_key = '42ae5bc7019f475d94e548841ac2c7bb'

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = sys.argv[1]

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

weather = ''

if x["cod"] != "404": 
    y = x["main"]
    if y["temp"] - 273.15 > 17:
        weather = 'Summer'
    else:
        weather = 'Winter'

    google_api_key = 'AIzaSyASFFmyJkj3_80AqjuMm52H9gf9OJpk710'

    google_cx = '000700725034361579724:fdsgnzu8lts'

    google_base_url = 'https://www.googleapis.com/customsearch/v1?'

    google_complete_url = google_base_url+'q='+weather+'+outfit+men'+'&num=10&searchType=image'+'&key='+google_api_key+'&cx='+google_cx

    google_response = requests.get(google_complete_url)

    results = google_response.json()

    image_set = results["items"]

    num = 1

    for image in image_set:
        full_path = 'Outfits/'+str(num)+'.jpg'
        urllib.request.urlretrieve(image["link"], full_path)
        num += 1    
else: 
    print(" City Not Found ")












