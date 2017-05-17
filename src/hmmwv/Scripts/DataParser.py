#!/usr/bin/env python
import csv
import roslib
import rospy
from std_msgs.msg import Float64
publ = rospy.Publisher('/hmmwv/Driving/Throttle', Float64, queue_size=10)
pubr = rospy.Publisher('/hmmwv/Driving/Steering', Float64, queue_size=10)
pubb = rospy.Publisher('/Desired/Speed', Float64, queue_size=10)

Throttle=0
Steer=0
def read_cell(x, y):
    with open('/home/ariel/ariel-ws/ariel/DataWavyRoad.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1
print (float(read_cell(4, 8))+3) 
def listener():
    i=1
    rospy.init_node('DataDriver', anonymous=True)
    rate = rospy.Rate(33.33333333) # 33.33333333Hz
    while not rospy.is_shutdown():
        Throttle=float(read_cell(1, i))
        Steer=float(read_cell(2, i))
        publ.publish(Float64(Throttle))
        pubr.publish(Float64(Steer))
        pubb.publish(Float64(0))
        i+=1
        rate.sleep()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
