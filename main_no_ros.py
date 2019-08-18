#!/bin/python3
#coding:utf-8
import random
import urllib
import time
import urllib,urllib2
import pycurl
import ConfigParser


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def open_lock():
    print("正在开锁，请稍等……")
    url = 'http://192.168.2.121/control?cmd=GPIO,15,1'
    data = urllib.urlopen(url)
    # data = data.decode('UTF-8')
    # print(data)
    # c = pycurl.Curl()
    # c.setopt(c.URL, url)
    # c.perform()
    # c.close()
    # time.sleep(0.1)
    url = 'http://192.168.2.121/control?cmd=GPIO,15,0'
    # c = pycurl.Curl()
    # c.setopt(c.URL, url)
    # c.perform()
    # c.close()
    # req = urllib2.Request(url=url)
    # res = urllib2.urlopen(req)
    data = urllib.urlopen(url)
    # data = data.decode('UTF-8')
    # print(data)

if __name__ == '__main__':

    print("欢迎进入密室逃脱！请按回车键(Enter)继续……")
    c = raw_input()
    cp = ConfigParser.SafeConfigParser()
    cp.read('escape.cfg')

    #print 'math:max',cp.get('math','max')

    math_max_int = int(cp.get('math', 'max'))
    required_score = int(cp.get('pass_condition', 'required_score'))
    correct_add_score = int(cp.get('math', 'correct_add_score'))
    wrong_sub_score = int(cp.get('math', 'wrong_sub_score'))
    score = 0
    a = 0
    b = 0
    operator = 0
    need_new_question = 1
    print("你们需要获得" + str(required_score) + "分才能进入下一关，答对一题加一分，答错一题减一分。")
    time.sleep(1)
    print("当前得分：" + str(score))
    while(score < required_score):
        if need_new_question :
            a = random.randint(0, math_max_int)
            b = random.randint(0, math_max_int)
            operator = random.randint(0, 1)
        while(a < b):
            a = random.randint(0, math_max_int)

        correct_answer = 0
        print("请输入以下算式的结果，然后按回车键Enter：")
        if operator == 0:
            print(str(a) + " + " + str(b) + " = ?")
            correct_answer = a + b
        else:
            print(str(a) + " - " + str(b) + " = ?")
            correct_answer = a - b

        c = raw_input()

        while not is_number(c):
            print("请输入数字")
            c = raw_input()

        c = int(c)

        print("你输入的是: " + str(c))
        time.sleep(1)
        if (c == correct_answer):
            print ("恭喜你，回答正确！加" + str(correct_add_score) + "分\n")
            score = score + 1
            need_new_question = 1
        else:

            print("很可惜，回答错误！减" + str(wrong_sub_score) + "分\n")
            need_new_question = 0
            if score > 0:
                score = score - 1

        time.sleep(3)
        print("当前得分：" + str(score))
        time.sleep(1)

    if(score >= required_score):
        open_lock()
