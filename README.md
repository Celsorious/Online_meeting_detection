# Online_meeting_detection
![image2](https://user-images.githubusercontent.com/95103811/217067436-ee1c9319-b0db-4db5-a71d-d523c57d06ed.jpeg)

With the rise of teleworking, surely it has happened to many of us that someone entered into the room when we are meeting.To solve this problem I have developed a project that based on three variables determines whether we are meeting or not. These are:

-Status of the webcam and microphone usage log.

-Status of the program process (Teams, Zoom...)

Based on this, it sends by serial protocol different information to an Arduino Nano by which the color of the RGB LED is selected. To control all its funcionalities  I develop a graphical interface for making it more user friendly.

Explained the software part, to make the system as portable as possible, apart from the 3D model, I built a mini USB to USB adapter that allows you to place the device next to the laptop occupying the minimum possible space.

![image4](https://user-images.githubusercontent.com/95103811/217067442-f14913fb-cbb6-4239-bce5-78e2bec0c499.jpeg)

# 3D model
To adjust the USB height to your laptop you need to modify the file /stl/height_usb_adjustment.STL
# Graphic Interface
To close correctly the USB serial interface you need to use the 'Exit application' button.

![Sin título](https://user-images.githubusercontent.com/95103811/217067373-2e209f02-bce8-48a6-9e99-d7db2db8301b.png)

