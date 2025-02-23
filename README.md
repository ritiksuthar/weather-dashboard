# 🌤 Django Weather Dashboard

A web-based weather dashboard built with Django that provides real-time weather updates for any city. It fetches weather data from an external API and displays key metrics like temperature, humidity, wind speed, and a 5-day forecast.

## 🔹 Features
- 🌍 Search weather by city
- 📊 Real-time temperature, humidity, and wind speed updates
- 📅 5-day weather forecast
- 🎨 User-friendly and responsive interface
- ⚡ Caching for optimized performance

## 🛠 Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS
- **API:** OpenWeatherMap (or any preferred weather API)

## 🚀 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/ritiksuthar/weather-dashboard.git
cd weather-dashboard
```

### 2. Create a virtual environment and activate it:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:
Create a `.env` file and add your API key:
```env
WEATHER_API_KEY=your_openweathermap_api_key
```

### 5. Run the server:
```bash
python manage.py runserver
```

### 6. Open in browser:
Go to `http://127.0.0.1:8000/` to use the dashboard.

## 📷 Preview
![image](https://github.com/user-attachments/assets/1e45ed5a-3633-44f4-9e68-1c550397333e)


## 🤝 Contributing
- Fork the repository
- Create a new branch (`git checkout -b feature-name`)
- Commit your changes (`git commit -m 'Add new feature'`)
- Push to the branch (`git push origin feature-name`)
- Open a pull request

## 📜 License
This project is open-source and available under the **MIT License**.

---
Feel free to improve this project by contributing or suggesting new features! 🚀

