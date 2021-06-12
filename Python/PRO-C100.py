"""class Car(object):
    def __init__(self,brand, name, color, seats, type):
        self.brand = brand
        self.name = name
        self.color = color
        self.seats = seats
        self.type = type
    
    def speed(self, distance, time):
        speed = distance/time
        print("Speed of the car is: " + str(speed) + "km/h")


car1 = Car("Buggati", "Chiron", "Black and Blue", 2, "Supercar")
print("Brand: "+ car1.brand)
print("Name: "+ car1.name)
print("Color: "+ car1.color)
print("Seats: "+ str(car1.seats))
print("Type: "+ car1.type)

km = int(input("Enter the distance covered (in km): "))
hr = int(input("Enter th time taken (in hr): "))
car1.speed(km, hr)"""

import time

class Computer(object):
    def __init__(self, processor, ram, rom, graphicCard, motherboard, psu, case, monitor, keyboard, mouse, webcamAndMic):
        self.processor = processor
        self.ram = ram
        self.rom = rom
        self.graphicCard = graphicCard
        self.motherboard = motherboard
        self.psu = psu
        self.case = case
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse
        self.webcamAndMic = webcamAndMic

    def systemConfig(self):
        print("Processor: "+ self.processor)
        print("RAM: "+ self.ram)
        print("ROM: "+ self.rom)
        print("Graphics Card: "+ self.graphicCard)
        print("Motherboard: " + self.motherboard)
        print("PSU: "+ self.psu)

    def hardware(self):
        print("Cabinet: " + self.case)
        print("Monitor: "+ self.monitor)
        print("Keyboard: "+ self.keyboard)
        print("Mouse: "+ self.mouse)
        print("Webcam: "+ self.webcamAndMic)

    def OS (self):
        choice = int(input("Enter the operating system you want in your computer [1: Windows] [2: Linux] [3: Mac OS]: "))
        if choice == 1:
            os = "Windows"
            print("You have selected Windows")
        elif choice == 2:
            os = "Linux"
            print("You have selected Linux")
        elif choice == 3:
            os = "Mac OS"
            print("You have selected Mac OS")
        else:
            print("please enter a valid operating system")

    def boot(self):
        print("Loading OS...")
        time.sleep(5)
        print("OS loaded successfully")

computer1 = Computer("AMD Ryzen 9 5950X", "128GB", "10TB SSD", "RTX 3090 8GB", "ASUS TUF Gaming X570-Plus", "XPG Core Reactor 650W", "Cougar Gaming Case", "49 inch Odyssey Super Ultra Wide QLED Gaming Monitor", "Corsair K100 RGB Optical", "Razer Deathadder V2", "Logitech C920")
computer1.systemConfig()
computer1.hardware()
computer1.OS()
computer1.boot()