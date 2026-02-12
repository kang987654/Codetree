n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

forecasts = [Forecast(dt, dy, w) for dt, dy, w in zip(date, day, weather)]
for forecast in sorted(forecasts, key=lambda forecast: forecast.date):
    if forecast.weather == 'Rain':
        print(forecast.date, forecast.day, forecast.weather)
        break
