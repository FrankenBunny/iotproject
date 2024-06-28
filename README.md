Julia Johansson jj224iw

# ProZone: An introductionairy IoT device for gamers
The ProZone is an IoT device developed by gamers, for gamers. The device can easily be built by using the information and steps detailed in this document.  The process consists out of obtaining the required materials, setting up the development environment, implementing the software, designing the user interface, and finally combining all the steps to create the IoT device known as ProZone. Using the information and steps detailed in this docuement the process is estimated to take 8 hours.

## Objective
*ProZone was designed to be reliable in terms of its purpose, cost-efficient in terms of required materials, and beginner-friendly in terms of the neccessary prior knowledge within the area of IoT.*

To game or not to game is a question old as time. Before jumping into another competitive match one might wonder how, with new equipment, the struggle remains. Maybe it's not the equipment's fault after all: maybe it's the gamer's. Alas, ProZone intends to tackle another, previously unexplored factor: the environment. A factor usually overlooked and forgotten, the environment plays a vital role in a gamer's performance and may differ from one gamer to another. The ProZone sets out to track each gamer's optimal environment by utilzing sensors to capture temperatures, humidity levels, and light levels. The data is then fortified by insights from the gamers themselves. To ensure that gamers can continue replacing faulty gear, hindering their ability, the ProZone can be constructed by any gamer willing to take on the task. The device can be constructed using readily available, cost-effective materials found online in a starter pack. The design is straightforward and accessible, requiring no prior IoT knowledge whilst having the entire construction process detailed in this document.

<br>

A common saying states:

*It is not the destination, it is the journey that matters.*

And it remains true in the context of ProZone. As the result of constructing your own device will not only give you the ability to track your optimal environment, potentially improving your gaming experience exponentially, but it introduces each undertaker of the task to the great world of IoT. The journey requires the task-bearer to learn about multiple components, how the combination of different components can be used in a single purpose, how to implement the software required to both capture and send information to their custom dashboard.

## Material
The hardware required to construct a ProZone device can be found in Linné University's "Start kit", which can be ordered from Elektrokit for 399 SEK. Due to the limited number of cables for each color, color coding was not followed in the picture seen below. Altough, the table below will list the required cables if one was to follow the color code of: red-power supply, black-grounding, and blue-communication. The cost for each separate item is listed in the table below, the currency is SEK.

| Type | Item | Utility | Count |Cost|
|---|---|---|---|---|
|Microcontroller|Raspberry Pi Pico WH|Controls the functions within the device.|1|109|
|Prototyping Board|Breadboard 840 connections|Build and test circuits without soldering.|1|69|
|Cable|USB Cable A-male to micro B 1.8m|Connects device to computer.|1|39|
|Lab Cable|Male/Male 30cm Black|Connecting components on the breadboard.|3|1.225|
|Lab Cable|Male/Male 30cm Red|Connecting components on the breadboard.|3|1.225|
|Lab Cable|Male/Female 30cm Black|Connecting components on the breadboard to the microcontroller.|1|1.225|
|Lab Cable|Male/Female 30cm Blue|Connecting components on the breadboard to the microcontroller.|2|1.225|
|Lab Cable|Male/Female 30cm Red|Connecting components on the breadboard to the microcontroller.|1|1.225|
|Resistor|Carbon Film Resistor 0.25W 4.7kohm|Restricts the flow of electric current by 4.7 kohm.|1|1|
|Resistor|Carbon Film Resistor 0.25W 330ohm|Restricts the flow of electric current by 330 ohm.|1|1|
|Sensor|Photoresistor CdS 4-7 kohm|Restricts the flow of electric current based on light levels.|1|8|
|Sensor|Digital Temperature and Humidity Sensor DHT11|Measures air temperature and humidity.|1|39|
|Switch|Tilt Switch|Detect tilting movements.|1|15|

![20240627_170431](https://hackmd.io/_uploads/H1upJ-sUR.jpg)

## Computer setup
The following information is applicable on Windows users. To start implementing the software required by ProZone, [Visual Code]("https://code.visualstudio.com/") was utilized. Once installed, the extension [Pymakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) which is an extension created to facilitate the development of PyCom devices. 

### Initial firmware setup for microcontroller
The next step consisted out of flashing the microcontroller with its firmware. The steps are listed in order below and can be used to update the firmware following new releases. Make sure you back up of any code before updating the firmware.
1. Download the latest version of required firmware from [this website](https://micropython.org/download/RPI_PICO_W/), found under the *Release* header. The downloaded file should be a **uf2** file.
2. Remove the sponge beneath the Raspberry Pi Pico and carefully but firmly connect the micro-USB end to the microcontroller. It is not unusual for there to be a small gap.
3. Press and hold down `BOOTSEL` on the Raspberry Pi Pico until step 5.
4. Connect the USB type A end to your computer.
5. You can now release the `BOOTSEL` button. A new drive named *RPI-RP2* will appear, open it in *File Explorer*.
6. Copy and paste the previously downloaded **uf2** file into the *RPI-RP2* drive.
7. Once the file has been transferred, the drive will dissapear from the *File Explorer* and you may then unconnect the device from your computer.

### Setting up the project and development environment
1. Open Visual Code.
2. Open the Pymakr tab found in the shortcut menu.
3. Create a new project and select which folder it should be stored in.
4. Set the name of the project.
5. Use the *empty* template.
6. Confirm you trust the authors of the given files.
7. Add your device, *Serial USB device(COMx)/unkown*, where x determines which USB port is used.
8. Select *Connect device* when hovering over the device name located under the project name.
9. Select *Create terminal* to create a terminal in which you can view output from the device.
10. Select *Start development mode*
11. Open the *Explorer* tab.
12. Copy the code presented in Section [The Code](#the-code), either by replacing the files or by copying the content within each given file and replace the local file content.
13. Save and the device should directly start printing output.


## Connecting the hardware
![circuit](https://hackmd.io/_uploads/B1nG3ljU0.png)
The circuit diagram above shows how the different components have been connected. The breadboard is excluded from the circuit diagram, instead the grounding and power supply has been connected by the wires.

### Raspberry Pi Pico
1. Connect the female end of the only male/female black lab cable, to the GND pin located on the Raspberry Pi Pico. Connect the male end on the same black cable to the ground rail on the breadboard.
2. Connect the female end of the only male/female red lab cable, to the 3V3-OUT pin on the Raspberry Pi Pico. Connect the male end on the same red cable to the power rail on the breadboard.
3. Connect each of the blue male/female lab cables, to one out of the GP27, GP26, and GP22 pins respectively.

### DHT11
1. Connect the male end of a male/male black lab cable to the ground rail on the breadboard.
2. Connect the other male end to the GND pin on the DHT11 sensor.
3. Connect the male end of a male/male red lab cable to the power rail on the breadboard.
4. Connect the other end to the VDD pin on the DHT11 sensor.
5. Connect the male end of the blue cable connected to the GP22 pin to the remaining pin on the DHT11 sensor.

### Photoresistor (DOUBLECHECK, move the output behind the resistor)
1. Connect the male end of a male/male black lab cable to the ground rail on the breadboard.
2. Connect the other male end to one end of the 4.7kohm resistor.
4. Connect the male end of a male/male red lab cable to the ground rail on the breadboard.
5. Connect the other male end to the other end of the 4.7kohm resistor.
6. Connect the male end of the blue cable connected to the GP27 pin to the output pin on the photoresistor.

### Tilt switch
1. Connect the male end of a male/male black lab cable to the ground rail on the breadboard.
2. Connect the other male end to the GND pin on the tilt switch. 
3. Connect the male end of a male/male red lab cable to one end of the 330 ohm resistor.
4. Connect the other end of the resistor to the power pin on the tilt switch.
5. Connect the male end of the blue cable connected to the GP26 pin to the output pin on the tilt switch.


*How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?*


- [x] Circuit diagram (can be hand drawn)


## Platform
Ubidots is the selected platform for data management and visualization, and it was chosen to allow the task-bearer the opportunity to learn how to use REST API's and coding. It is a cloud-based platform specially designed for IoT applications. Ubidots was selected due to its user friendly UI and vast range of components used for visualization even in the free version. In Ubidots a user with a free memembership can have up to three devices and one dashboard. Each device may capture multiple variables, which the developer designates. The dashboard can then through the use of components display the data within these variables. If the ProZone was to be expanded, depending on the need the premium version could be utilized to offer a greater variety of data analysis through the expanded librabry of components available in the dashboard.

### Setup the platform
In this section the setup of the Ubidots platform is detailed. The setup is required prior to the implementation of the software in order to accurately transmit the data to its corresponding variable. The table below displays the variables, their purpose, and their Ubidots dashboard component.
|Name|Purpose|Component|
|---|---|---|
|Tilt|Captures the status of the tilt switch.|Indicator|
|Temperature|Captures the air temperature.|Thermometer|
|Humidity|Captures the air humidity.|Gauge|
|Light|Captures the light levels.|Gauge|
|TiltTemperature|Captures the air temperature when the device has been tilted.|Column in Values table|
|TiltHumidity|Captures the air humidity when the device has been tilted.|Column in Values table|
|TiltLight|Captures the light levels when the device has been tilted.|Column in Values table|

1. Create a blank device named ProZone.
2. Create the variables seen in the table.
3. Create a new dashboard named *ProZone Dashboard*.
4. Create the individual components listed in the table.
5. Create the columns for each tilt variable in the Values table.
    1. Set the aggregation method for the variable to Average.
    2. Set the span to this month.
    3. Set the sample period to 1 month(s).

## Presenting the data
*Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?*

- [ ] *Provide visual examples on how the dashboard looks. Pictures needed.*
- [ ] How often is data saved in the database.
- [ ] *Explain your choice of database.
- [ ] *Automation/triggers of the data.
- [ ] Finalizing the design
- [ ] Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!


## The code
The software required by ProZone consists out of three files, `keys.py`, `boot.py`, and `main.py`. The following sections describe the purpose and implementation for each file.

### `keys.py`
This file contains the login credentials for the WiFi the ProZone should connect to, with both the name of the network and its' password stored as separate variables.

### `boot.py`
The boot file contains the processes neccessary prior to the execution of the main process located in the main file. In this file the network connection is setup since it is required for the main execution to function. The execution requires the importation of the keys file, the network library, and sleep from the time library. Once the neccessary imports are made there exists two functions except from the main execution. The `http_get()` function requires the libraries socket and time to be locally imported.

1. Try to establish a connection to the existing network using the `connect()` function.
2. If connection failed:
    1. Reset machine.
3. Try to perform the HTTP GET request using the `http_get(url)` function.
 

#### `connect()`
The function is used to establish a connection to a WiFi network. The resets the network interface to ensure that a fresh connection is established following a boot or reset. If a connection cannot be established, the developer is resetted.
1. Reset the network interface.
2. Set the network interface to station mode, to ensure it connects to an existing network rather than tries to create one itself.
3. Connect to the network with the credentials stored in the keys file.
4. Wait for connection to be established.
5. If connection is established:
    1. Stop waiting
    2. Notify of successful connection.
6. If connection is not established and time limit has succeeded:
    1. Notify of failed connection.
7. End


#### `http_get(url)`
This function makes sure that it can successfully perform a HTTP GET request. This is neccessary to later send the data using the API from Ubidots.
1. Parse the URL and store the values as their respective variables in the HTTP request.
2. Get the IP address of the host server.
3. Initialize the socket.
4. Connect to the host address.
5. Wait for response.
6. Receive and print the response.
8. Close the socket connection.

### `Main.py`
This file contains the main execution for ProZone. This includes the handling of sensors as well as communicating with the Ubidots API to send the captured data. The process requires the libraries machine, specifically ADC and Pin, time, specifically sleep, dht, as well as network and requests.




How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

How often is the data sent?
Which wireless protocols did you use (WiFi, LoRa, etc …)?
Which transport protocols were used (MQTT, webhook, etc …)
*Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.




## Show final results of the project
- [ ] Pictures
- [ ] *Video presentation
