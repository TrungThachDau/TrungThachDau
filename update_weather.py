import requests

# Thông tin API
API_KEY = "daf507f48231467bd52c81ef9d56d9e1"  # Thay bằng API key của bạn
LAT = 10.8231  # Vĩ độ của Sài Gòn
LON = 106.6297  # Kinh độ của Sài Gòn
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# Gửi yêu cầu HTTP tới API
response = requests.get(URL)

# Kiểm tra mã trạng thái
if response.status_code == 200:
    data = response.json()

    # Lấy các thông tin cần thiết từ dữ liệu trả về
    weather_description = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Cập nhật nội dung README.md
    with open('README.md', 'r') as file:
        content = file.readlines()

    # Tìm và cập nhật phần thời tiết trong README
    for idx, line in enumerate(content):
        if line.startswith("<!-- WEATHER -->"):
            content[idx + 1] = f"- 📍 Saigon, Vietnam: {weather_description} - {temperature}°C \n"
            break

    # Lưu lại nội dung đã cập nhật
    with open('README.md', 'w') as file:
        file.writelines(content)
else:
    print("Không thể lấy dữ liệu thời tiết.")
