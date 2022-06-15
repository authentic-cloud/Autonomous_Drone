# Drone
Tello drone repo<br />
Created for Face Recognition with DJI- Tello<br />
Working file without delay = Test.py<br />
Tello takes off and ascends to about 1.5m (human face level)<br />
1- Rotates slowly in yaw (scans the surroundings)<br />
2- If the face is detected, drone tries to:<br />
3- Keep the target in the middle of the screen (by controlling yaw and altitude,
position control optional)<br />
4- Maintain distance to target <br />

Working file with classifier working with precision is Test.py<br />
Reference file = facetrack.py<br />
Special Thanks to MurtazasWorkshopRoboticsandAI -His youtube videos help me to tune the contol system precisely.<br />
Link to youtube video--<br />
https://www.youtube.com/watch?v=LmEcyQnfpDA&t=2189s<br />
**WARNING**--- <br />
Facetrack.py do not work properly and precisely  so i created my own algorithm which is test.py.<br />
Test.py works little bit aggresively because i made it that way so it works without any delay .<br />
