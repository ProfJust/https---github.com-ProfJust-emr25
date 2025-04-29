from rtde_control import RTDEControlInterface
from rtde_receive import RTDEReceiveInterface
from robotiq_gripper_control import RobotiqGripper
import time

UR3_IP = "127.0.0.1"

rtde_r = RTDEReceiveInterface(UR3_IP)
rtde_c = RTDEControlInterface(UR3_IP)
gripper = RobotiqGripper(rtde_c)

input("Roboter startet 1. Bewegung nach Eingabe beliebiger Taste")
resp = rtde_c.moveL( [ 1.0, 1.0, -0.5, 0.0, 0.0, 0.0], speed=0.5, acceleration=0.3)
print(f"📥 Antwort: {resp}")

input("Roboter startet 2. Bewegung nach Eingabe beliebiger Taste")
resp = rtde_c.moveL( [ 1.0, 1.0, -0.5, 0.0, 0.0, 1.57], speed=0.5, acceleration=0.3)
print(f"📥 Antwort: {resp}")

"""# Gripper Aktionen
gripper.activate()
gripper.set_force(50)
gripper.set_speed(100)

# Liste von kartesischen Zielposen (IK) bezogen auf das TCP-Koordinatensystem
# X, Y, Z, RZ, RY, RX (in RAD)
moveL_ziele = [
   [ 1.0, -1.0, 1.0, 0.0, 0.0, 0.0],   
   [ 1.0, -1.0, 1.0, 0.0, 1.57, 0.0],     
]

# Bewegungen ausführen

for i, ziel_pose in enumerate(moveL_ziele):
    input("Roboter startet Bewegung nach Eingabe beliebiger Taste")
    print(f"➡️  Sende moveL #{i+1}: {ziel_pose}")
    resp = rtde_c.moveL(ziel_pose, speed=0.5, acceleration=0.3)
    print(f"📥 Antwort: {resp}")
    actual_q = rtde_r.getActualQ() # in radian
    print("Aktueller Zustand - Gelenkpositionen in Grad ")
    for arg in actual_q:
        print(arg *180.0/3.1415927)
    time.sleep(1)

"""

"""# Gripper Aktionen
input("Gripper startet Bewegung nach Eingabe beliebiger Taste")
gripper.close()
time.sleep(1)
input("Gripper startet Bewegung nach Eingabe beliebiger Taste")
gripper.open()
time.sleep(1)
gripper.close()
time.sleep(1)"""

# Abschluss
rtde_c.disconnect()
rtde_r.disconnect()

"""  
# Gripper Aktionen
gripper.activate()
gripper.set_force(50)
gripper.set_speed(100)
gripper.close()

# Roboter bewegen
input("Roboter startet Bewegung nach Eingabe beliebiger Taste")
rtde_c.moveL([-0.300, -0.700 , 0.4,  0.0, 2.204, 0.1], 0.5, 0.3)
print("🤖 moveL...")
# rtde_c.moveL([-0.3, -0.7, 0.4, 0.0, 3.2, 0.1])
gripper.open()
#gripper.move_and_wait_for_pos(255, 255, 255)
actual_q = rtde_r.getActualQ() # in radian
print("Aktueller Zustand - Gelenkpositionen in Grad ")
for arg in actual_q:
    print(arg *180.0/3.1415927)

time.sleep(1)
# Roboter bewegen
input("Roboter startet Bewegung nach Eingabe beliebiger Taste")
print("🤖 moveJ..")
rtde_c.moveL([-0.600, -0.900 , 0.5,  0.0, 0.8, 0.1], 0.5, 0.3)
gripper.close()
time.sleep(1)
#gripper.move(10)  # mm

# Abschluss
rtde_c.disconnect()
rtde_r.disconnect()
"""