#!/bin/python2
#coding:utf-8
import random
import rospy
from std_msgs.msg import String
import urllib
import time
import urllib,urllib2
import pycurl

def open_lock():
    url = 'http://192.168.2.207/control?cmd=GPIO,15,1'
    data = urllib.urlopen(url)
    # data = data.decode('UTF-8')
    # print(data)
    # c = pycurl.Curl()
    # c.setopt(c.URL, url)
    # c.perform()
    # c.close()
    # time.sleep(0.1)
    url = 'http://192.168.2.207/control?cmd=GPIO,15,0'
    # c = pycurl.Curl()
    # c.setopt(c.URL, url)
    # c.perform()
    # c.close()
    # req = urllib2.Request(url=url)
    # res = urllib2.urlopen(req)
    data = urllib.urlopen(url)
    # data = data.decode('UTF-8')
    # print(data)

def talker(pub, a):

    rate = rospy.Rate(10) # 10hz
    hello_str = str(a)
    pub.publish(hello_str)
    rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # rate.sleep()
    # pub.publish(hello_str)
    # while not rospy.is_shutdown():
    #     hello_str = "hello world %s" % rospy.get_time()
    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()


if __name__ == '__main__':

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    print("欢迎进入密室逃脱！")

    a = random.randint(0, 99)
    b = random.randint(0, 99)
    while(a < b):
        a = random.randint(0, 99)
    operator = random.randint(0,1)
    correct_answer = 0
    print("请输入以下算式的结果：")
    if operator == 0:
        print(str(a) + " + " + str(b) + " = ?")
        correct_answer = a + b
    else:
        print(str(a) + " - " + str(b) + " = ?")
        correct_answer = a - b


    c = input()
    c = int(c)

    print("你输入的是: " + str(c))

    is_correct = 0
    if (c == correct_answer):
        print("恭喜你，回答正确！")
        is_correct = 1
        open_lock()

    else:
        print("很可惜，回答错误！")
        is_correct = 0

    try:
        talker(pub, is_correct)
    except rospy.ROSInterruptException:
        pass

