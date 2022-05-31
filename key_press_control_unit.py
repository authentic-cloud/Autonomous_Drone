from djitellopy import tello
import time
import keyPress_detect as kp

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
def getKeyboardInput():
    left_right, fwd_bwd , up_down , yaw_vel = 0, 0, 0, 0
    speed = 20

    if kp.getKey("TAB"): yaw_vel = me.takeoff()
    if kp.getKey("SPACE"): yaw_vel = me.land()

    if kp.getKey("LEFT"):left_right = -speed
    elif kp.getKey("RIGHT"):left_right = speed

    if kp.getKey("w"):up_down= speed
    elif kp.getKey("s"):up_down = -speed

    if kp.getKey("UP"):fwd_bwd = speed
    elif kp.getKey("DOWN"):fwd_bwd = -speed

    if kp.getKey("a"):yaw_vel = speed
    elif kp.getKey("d"):yaw_vel = -speed

    return [left_right, fwd_bwd , up_down , yaw_vel]

me.takeoff()
while True:
    vals=getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(1)

