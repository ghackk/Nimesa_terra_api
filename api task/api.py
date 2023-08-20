import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_temperature(data, target_datetime):
    for entry in data["list"]:
        if entry["dt_txt"] == target_datetime:
            return entry["main"]["temp"]
    return None

def get_wind_speed(data, target_datetime):
    for entry in data["list"]:
        if entry["dt_txt"] == target_datetime:
            return entry["wind"]["speed"]
    return None

def get_pressure(data, target_datetime):
    for entry in data["list"]:
        if entry["dt_txt"] == target_datetime:
            return entry["main"]["pressure"]
    return None

def main():
    response = requests.get(API_URL)
    weather_data = response.json()

    while True:
        print("\nMenu:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            target_datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, target_datetime)
            if temperature is not None:
                print(f"Temperature at {target_datetime}: {temperature} K")
            else:
                print("Data not available for the specified date and time.")
        elif choice == "2":
            target_datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, target_datetime)
            if wind_speed is not None:
                print(f"Wind Speed at {target_datetime}: {wind_speed} m/s")
            else:
                print("Data not available for the specified date and time.")
        elif choice == "3":
            target_datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, target_datetime)
            if pressure is not None:
                print(f"Pressure at {target_datetime}: {pressure} hPa")
            else:
                print("Data not available for the specified date and time.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
