import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    UNIT = "metric"
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNIT}"

    @classmethod
    def is_hot_in_pehuajo(cls):
        resp = False
        try:
            celcius = requests.get(cls.URL).json()['main']['temp']
            if celcius>28:
                resp = True
        except:
            resp = False
        return (resp)

print(GeoAPI.is_hot_in_pehuajo())