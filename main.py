import machine
from machine import ADC, Pin

import time
from time import sleep

import dht

import network
import urequests as requests


# Setting up Ubidot variables
TOKEN = "BBUS-HqB4xp0MLF7M3oBXWrcQzAxechzHGl"
GAMERHELPER = "PicoWBoard"
TILT_VARIABLE = "Tilt"
LIGHT_VARIABLE = "Light"
HUMIDITY_VARIABLE = "Humidity"
TEMPERATURE_VARIABLE = "Temperature"
TILT_TEMPERATURE = "TiltTemperature"
TILT_HUMIDITY = "TiltHumidity"
TILT_LIGHT = "TiltLight"
WIFI_SSID = "Valpen"
WIFI_PASS = "ChupaCabra4i4i"
DELAY = 1

# Set up WiFi Connection
def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip


# Build json for requests
def build_Json(variables):
    try:
        data = {variable: {"value": value} for variable, value in variables.items()}
        return data
    except:
        return None
    


# Sending data to Ubidots Restful Webserice
def sendData(device, variables):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_Json(variables)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass


# Define Pins
ldr = ADC(Pin(27))
led = Pin("LED", Pin.OUT)
tempSensor = dht.DHT11(machine.Pin(26))     # DHT11 Constructor 
tiltPin = Pin(22, Pin.IN)


# Define variables
currentTemperature = 0
currentHumidity = 0
currentLight = 0


# Connect to WiFi
connect()


# MAIN EXECUTION
while True:
    if tiltPin.value() == 1:
        print("Switch on")
        
        lightRead = ldr.read_u16()
        light = 100 - round(lightRead / 65535 * 100, 2)
        print("Light is {}%".format(light))
        try:
            tempSensor.measure()
            temperature = tempSensor.temperature()
            humidity = tempSensor.humidity()
            print("Temperature is {} degrees Celsius".format(temperature))
            print("Humidity is {}%".format(humidity))
        except Exception as error:
            print("Exception occurred", error)
        
        # Set values
        currentTemperature = temperature
        currentHumidity = humidity
        currentLight = light

        # Send values
        variables = {
            "Temperature": currentTemperature,
            "Humidity": currentHumidity,
            "Light": currentLight,
            "Tilt": tiltPin.value()
        }

        returnValue = sendData(GAMERHELPER, variables)

    else:
        print("Switch off")
        
        lightRead = ldr.read_u16()
        light = 100 - round(lightRead / 65535 * 100, 2)
        print("Light is {}%".format(light))
        try:
            tempSensor.measure()
            temperature = tempSensor.temperature()
            humidity = tempSensor.humidity()
            print("Temperature is {} degrees Celsius".format(temperature))
            print("Humidity is {}%".format(humidity))
        except Exception as error:
            print("Exception occurred", error)
        
        # Set values
        currentTemperature = temperature
        currentHumidity = humidity
        currentLight = light


        # Send values
        variables = {
            "TiltTemperature": currentTemperature,
            "TiltHumidity": currentHumidity,
            "TiltLight": currentLight,
            "Tilt": tiltPin.value()
        }
        
        returnValue = sendData(GAMERHELPER, variables)

    time.sleep(5)