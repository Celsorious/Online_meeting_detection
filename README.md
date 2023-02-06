# Online_meeting_detection
![image2](https://user-images.githubusercontent.com/95103811/217067436-ee1c9319-b0db-4db5-a71d-d523c57d06ed.jpeg)

With the rise of teleworking, surely it has happened to many of us that someone entered the room when we are meeting. To solve this problem I have developed a project that based on three variables determines if we are fulfilling ourselves or not. 

These are:

-Status of the webcam and microphone usage log.

-Program process status (Teams, Zoom...) 

On the grounds of this, it sends different information by serial protocol to an Arduino Nano which is responsible for turning on the RGB led status. Depending on its color (red or green) other people can know if we are busy or not.

To control all its functionalities I developed a graphical interface to make it easier to use.

![Sin título](https://user-images.githubusercontent.com/95103811/217067373-2e209f02-bce8-48a6-9e99-d7db2db8301b.png)

Finally, to make the system portable, apart from the 3D model design, I built a mini USB to USB adapter that allows you to place the device next to the laptop taking up as little space as possible.

![image4](https://user-images.githubusercontent.com/95103811/217067442-f14913fb-cbb6-4239-bce5-78e2bec0c499.jpeg)

# 3D model
To adjust the USB height to your laptop you need to modify the file /stl/height_usb_adjustment.STL
# Graphic Interface
To close correctly the USB serial interface you need to use the 'Exit application' button.



