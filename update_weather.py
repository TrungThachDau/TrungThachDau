import requests

# Thông tin API và thành phố
API_KEY = "your_openweather_api_key"  # Thay bằng API key của bạn
CITY = "Ho Chi Minh City"  # Thành phố
URL = f"http://api.openweathermap.org/data/2.5/weather?q=Saigon&appid=daf507f48231467bd52c81ef9d56d9e1&units=metric"

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        return f"### Thời tiết tại Sài Gòn: {weather}, {temp}°C"
    else:
        return "### Không thể lấy thông tin thời tiết."

def update_readme():
    weather_info = get_weather()
    
    with open("README.md", "r") as file:
        content = file.readlines()
    
    with open("README.md", "w") as file:
        for line in content:
            if line.startswith("### Thời tiết tại"):
                file.write(weather_info + "\n")
            else:
                file.write(line)

if __name__ == "__main__":
    update_readme()
