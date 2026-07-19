import time # For some Wait time to slow down execution so we can interact and read info

# Creating Parent Class
class SmartDevice:
    # Defining The Public and Private Attributes
    def __init__(self, name, device_id, power_status):
        self.name = name
        self.__device_id = device_id
        self.__power_status = power_status
    # Definig The Turn ON, Turn OFF and Display INFO Methods
    def turn_on(self):
        self.__power_status = True
        print(f"{self.name} is now turned ON.")

    def turn_off(self):
        self.__power_status = False
        print(f"{self.name} is now turned OFF.")

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.__device_id}, Power ON: {self.__power_status}")
    # Using The @property To Allow Access To the Private Attribute "__device_id"
    @property
    def device_id(self):
        return self.__device_id
    # Defining a Setter to help change the device id if necessary
    @device_id.setter
    def device_id(self, id):
        if len(id) == 0:
            print("Invalid Device ID: Cannot be empty")
        else:
            self.__device_id = id
    # Using The @property method To Allow Access To the Private Attribute "__power_status" 
    @property
    def power_status(self):
        return self.__power_status
    
# Definig Child Classes
class TemperatureSensor(SmartDevice):
    # Adding extra attributes to TemperatureSensor class
    def __init__(self, name, device_id, power_status, temperature):
        super().__init__(name, device_id, power_status)
        self.temperature = temperature
    # Adding extra functionality to TemperatureSensor class
    def read_temperature(self):
        print(f"Current {self.name} temperature is: {self.temperature}°C")


class SecurityCamera(SmartDevice):
    # Adding extra attributes to TemperatureSensor class
    def __init__(self, name, device_id, power_status, recording_status):
        super().__init__(name, device_id, power_status)
        self.recording_status = recording_status
    # Adding extra functionalities to TemperatureSensor class
    def start_recording(self):
        self.recording_status = True
        print(f"{self.name} has started recording.")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.name} has stopped recording.")


class SmartLight(SmartDevice):
    # Adding extra attributes to TemperatureSensor class
    def __init__(self, name, device_id, power_status, brightness):
        super().__init__(name, device_id, power_status)
        self.brightness = brightness
    # Adding extra functionality to TemperatureSensor class
    def increase_brightness(self, amount):
        new_brightness = self.brightness + amount
        if new_brightness > 100:
            self.brightness = 100
            print(f"{self.name} is at maximum brightness (100%).")
        else:
            self.brightness = new_brightness
            print(f"{self.name} brightness increased to {self.brightness}%.")

    def decrease_brightness(self, amount):
        new_brightness = self.brightness - amount
        if new_brightness < 0:
            self.brightness = 0
            print(f"{self.name} is at minimum brightness (0%).")
        else:
            self.brightness = new_brightness
            print(f"{self.name} brightness decreased to {self.brightness}%.")

    @property
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, value):
        if value < 0 or value > 100:
            print("Invalid Value: Brightness must be between 0 and 100")
        else:
            self.__brightness = value


# Object Creation 
temp_sensor = TemperatureSensor("Living Room Sensor", "TS1", False, 26)
camera = SecurityCamera("Front Gate Camera", "SC1", False, False)
light = SmartLight("Porch Light", "SL1", False, 0)

# The Menu-Driven Interface 
while True:
    # Wait Time
    time.sleep(0.5)
    print("""
          Essel's Smart Device Management System
    1. Display All Device Information
    2. Turn Device On
    3. Turn Device Off
    4. Read Temperature (Living Room Sensor)
    5. Adjust Brightness (Porch Light)
    6. Start/Stop Recording (Front Gate Camera)
    7. Exit
""")
    choice = input("Enter your choice (1-7): ")
    print("")
    # Choosing the device to interact with
    if choice == '1':
        print("Loading Device Status ")
        temp_sensor.display_info()
        camera.display_info()
        light.display_info()
    # Determinig the device to turn ON
    elif choice == '2':
        print("Which device do you want to turn ON?")
        print("1. Living Room Sensor")
        print("2. Front Gate Camera")
        print("3. Porch Light")
        dev_choice = input("Select Device (1-3): ")
        # Mechanism Behind Turning ON the Device
        if dev_choice == '1':
            temp_sensor.turn_on()
        elif dev_choice == '2':
            camera.turn_on()
        elif dev_choice == '3':
            light.turn_on()
        else:
            print("Invalid Selection.")
    # Determinig the device to turn OFF
    elif choice == '3':
        print("Which device do you want to turn OFF?")
        print("1. Living Room Sensor")
        print("2. Front Gate Camera")
        print("3. Porch Light")
        dev_choice = input("Select Device (1-3): ")
        # Mechanism Behind Turning ON the Device
        if dev_choice == '1':
            temp_sensor.turn_off()
        elif dev_choice == '2':
            camera.turn_off()
        elif dev_choice == '3':
            light.turn_off()
        else:
            print("Invalid Selection.")
    # Reading Temperature
    elif choice == '4':
        temp_sensor.read_temperature()
    # Adjusting the brightness of device
    elif choice == '5':
        action = input("Porch Light: Type '1' to increase or '2' to decrease brightness: ")
        
        if action == '1':
            try:
                amount = int(input("Enter the amount to increase by: "))
                light.increase_brightness(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif action == '2':
            try:
                amount = int(input("Enter the amount to decrease by: "))
                light.decrease_brightness(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        else:
            print("Invalid action.")
    # Defining the functionality of the camera to either start or stop recording
    elif choice == '6':
        action = input("Front Gate Camera: Type '1' to start recording or '2' to stop recording: ")
        if action == '1':
            camera.start_recording()
        elif action == '2':
            camera.stop_recording()
        else:
            print("Invalid Action.")

    elif choice == '7':
        print("Exiting the program...")
        break

    else:
        print("Invalid option. Please select 1 through 7.")
# Wait Time
time.sleep(0.5)
