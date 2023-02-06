""" 
    MEETING PROGRAM DETECTION
    Author: Celso Martínez Rivas
    Info: Include everything in one file to make easier the compilation to .exe. Used autopytoexe 
    Functions: Detect meeting based on the status of the register of webcam, microphone and if is the process on tasklist
               Send data to usb serial device to switch on a RGB LED.
    Interface: To close the process of detection completely you need to press the 'exit application' button.
"""

###### PYTHON PACKAGES ######
import tkinter as tk
from tkinter import messagebox

import winreg
import subprocess
import serial, time
import serial.tools.list_ports

###### WEBCAM MICROPHONE CONFIGURATION ######

MAIN_KEY = winreg.HKEY_CURRENT_USER
VARIABLE = "LastUsedTimeStop"

def create_device_path(device):
    DEVICE_PATH = f"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\{device}\\NonPackaged"
    return DEVICE_PATH

def configure_key(DEVICE_PATH):
    return winreg.OpenKey(MAIN_KEY, DEVICE_PATH)

def obtain_number_subkeys(register_key):
    number_subkeys, _, _ = winreg.QueryInfoKey(register_key)

    return number_subkeys

def obtain_activity_device(register_key, number_subkeys, variable, DEVICE_PATH):
    stopped_time_check = []
    for subkey_index in range(number_subkeys):
        name_subkey = winreg.EnumKey(register_key, subkey_index)
        full_path = f"{DEVICE_PATH}\\{name_subkey}"
        subkey = winreg.OpenKey(MAIN_KEY, full_path)

        stopped_time_stamp, _ = winreg.QueryValueEx(subkey, variable)
        stopped_time_check.append(stopped_time_stamp)
    
    return stopped_time_check

def check_activity_device(stopped_time_check, device):
    device_is_on = False
    if 0 in stopped_time_check:
        device_is_on = True

    return device_is_on
    
# MICROPHONE REGISTER #
DEVICE_PATH = create_device_path(device = "microphone")
register_key = configure_key(DEVICE_PATH = DEVICE_PATH)
VARIABLE = "LastUsedTimeStop"
DEVICE = "MICROPHONE"

# WEBCAM REGISTER #
DEVICE_PATH_1 = create_device_path(device = "webcam")
register_key_1 = configure_key(DEVICE_PATH = DEVICE_PATH_1)
DEVICE_1 = "WEBCAM"


###### PROGRAM CONFIGURATION ######
PROCESS_NAME = "Teams.exe"
def check_program(process_name):
    process_is_running = False
    process_list = str(subprocess.check_output('tasklist', shell=True))
    if process_name in process_list:
        process_is_running = True
    return process_is_running

###### SEND DATA FROM SERIAL ######
device_is_connected = False
def get_device_port():
    global device_is_connected
    device_port = ""
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        device_port = port
    if device_port != "":
        device_is_connected = True
    else:
        print("Device not connected.")

    return device_port 

def configure_serial_port(device_port):
    baudrate = 9600
    configuration_time = 2
    esp_serial = serial.Serial(port = device_port, baudrate = baudrate)
    time.sleep(configuration_time)
   
    return esp_serial

###### SCREEN CONFIGURATION ######

root = tk.Tk()
HEIGHT = 5
WIDTH = 200
canvas1 = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas1.pack()

###### BUTTON FUNCTIONS ######

# VARIABLE FOR EXECUTE ONE TIME THE PROCESS #
count_connection = 0

def connect_device():
    global esp_device
    global count_connection
    TIME_CHECK_USB = 1
    if count_connection == 0:
        msg_box = tk.messagebox.askquestion('Device connection', 'Connect your device', icon='warning')

        if msg_box == 'yes':
            while not device_is_connected:
                device_port = get_device_port()
                time.sleep(TIME_CHECK_USB)
            esp_device = configure_serial_port(device_port = device_port) 
            tk.messagebox.showinfo('Device connection', 'Device connected') 
            count_connection += 1              
        else:
            tk.messagebox.showinfo('Return', 'Return to the main screen')
    else:
        tk.messagebox.showinfo('Device connection', 'The device is still connected')

TIME_EXECUTION = 100
def main_execution():
   global count_mainloop
   if device_is_connected:
        # STATUS PROCESS #
        status_program = check_program(process_name = PROCESS_NAME)

        # STATUS WEBCAM #
        number_subkeys = obtain_number_subkeys(register_key = register_key)
        stopped_time_check = obtain_activity_device(register_key = register_key, number_subkeys = number_subkeys, variable = VARIABLE, DEVICE_PATH = DEVICE_PATH)
        status_webcam = check_activity_device(stopped_time_check = stopped_time_check, device = DEVICE)

        # STATUS MICROPHONE #
        number_subkeys_1 = obtain_number_subkeys(register_key = register_key_1)
        stopped_time_check_1 = obtain_activity_device(register_key = register_key_1, number_subkeys = number_subkeys_1, variable = VARIABLE, DEVICE_PATH = DEVICE_PATH_1)
        status_microphone = check_activity_device(stopped_time_check = stopped_time_check_1, device = DEVICE_1)


        if (status_webcam or status_microphone) and status_program:
            esp_device.write(b'2') # SEND 2 = RED LED

        elif not status_webcam and not status_microphone:
            esp_device.write(b'0') # SEND 0 = LED GREEN

        count_mainloop += 1
        root.after(TIME_EXECUTION, main_execution) # REFRESH GRAPHICAL INTERFACE

# VARIABLE FOR EXECUTE ONE TIME THE PROCESS #
count_mainloop = 0 

def mainloop():
    if count_mainloop == 0:
        msg_box = tk.messagebox.askquestion('TEAMS meeting detection', 'Start detection', icon='warning')
        
        if msg_box == 'yes':
            main_execution()         
        else:
            tk.messagebox.showinfo('Return', 'Return to the application screen')
    else:
        tk.messagebox.showinfo('TEAMS meeting detection', 'The main process is still running')

def exit_application():
    msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
    
    if msg_box == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Return', 'Return to the main screen')

###### BUTTON CONFIGURATION ######
button2 = tk.Button(root, text='Device connection', command=connect_device, bg='grey', fg='white')
button1 = tk.Button(root, text='Mainloop', command=mainloop, bg='grey', fg='white')
button3 = tk.Button(root, text='Exit program', command=exit_application, bg='grey', fg='white')

button1.pack(side = 'left')
button2.pack(side = 'left')
button3.pack(side = 'left')


root.mainloop()