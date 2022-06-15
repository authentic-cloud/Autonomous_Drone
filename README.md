# Drone
Tello drone repo
Created for Face Recognition with DJI- Tello
Working file without delay = Test.py
Tello takes off and ascends to about 1.5m (human face level)
1- Rotates slowly in yaw (scans the surroundings)
2- If the face is detected, drone tries to:
3- Keep the target in the middle of the screen (by controlling yaw and altitude,
position control optional)
4- Maintain distance to target 

Working file with classifier working with precision is Test.py
Reference file = facetrack.py
Special Thanks to MurtazasWorkshopRoboticsandAI -His youtube videos help me to tune the contol system precisely.
Link to youtube video--
https://www.youtube.com/watch?v=LmEcyQnfpDA&t=2189s
**WARNING**--- 
Facetrack.py do not work properly and precisely  so i created my own algorithm which is test.py.
Test.py works little bit aggresively because i made it that way so it works without any delay .
