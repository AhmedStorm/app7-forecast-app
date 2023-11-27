import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"


def get_data(place, forecasted_days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = forecasted_days * 8
    filtered_data = data["list"]
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", forecasted_days=2, kind="Temperature"))
    print(get_data("Tokyo", forecasted_days=3, kind="Sky"))
