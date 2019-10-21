# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:31:08 2019

@author: ygm
"""

import requests
import json
import time
def getInfo(username="***",password="***"):
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    with requests.Session() as s:
        captcha_headers = {'User-Agent': ua}
        payload = {"username": username, "password": password}
        login = s.post('https://app***/uc/wap/login/check', data=payload, allow_redirects=True)
        #print(login.text)
        mark=int(0)
        classTable = [[" " for i in range(6)]for i in range(17*7*7)]
        classNum=0
        initWeek=35
        year=2019
        for week in range(17):
            schedule_payload = {"year": "2019-2020", "term": 1, "week": week, "type": 1}
            schedule = s.post('https://app***/timetable/wap/default/get-datatmp', data=schedule_payload)
            dict = json.loads(schedule.text)
            dict = json.loads(schedule.text)['d']['classes']
            n=len(dict)
            nowWeek=week+initWeek
            for i in range(0,n):
                classTable[classNum][0]=dict[i]['course_name']
                classTable[classNum][1]=dict[i]['location']
                time1='2019-'+str(nowWeek)+'-'+str(dict[i]['weekday'])
                time2=time.strptime(time1, '%Y-%U-%w')
                time3=time.strftime("%Y%m%d",time2)
                classTable[classNum][2]=time3
                classTable[classNum][3]=dict[i]['teacher']
                clock=dict[i]['course_time']
                clock=clock.split('~')
                clockStart=clock[0].split(':')
                clockEnd=clock[1].split(':')
                clock1=clockStart[0]+clockStart[1]+'00'
                clock2=clockEnd[0]+clockEnd[1]+'00'
                classTable[classNum][4]=clock1
                classTable[classNum][5]=clock2
                classNum+=1
        for i in range(classNum):
           print(classTable[i])

def editICSfoot():
    t_n = b_new_file.write("END:VCALENDAR\n")
    b_new_file.close()
    pass

def editICSbody():

    pass

def editICShead():
    newfile = "i" + "1707020110" + ".ics"  # 学号换成传入的参数：学号
    b_new_file = open(newfile, 'w')
    t_n = b_new_file.write("BEGIN:VCALENDAR\n" +
                           "METHOD:PUBLISH\n" +
                           "VERSION:2.0\n" +
                           "COMMENT:本软件服务由中国石油大学（华东）网络信息协会提供，代码编写人员：李恒源，杨国铭，田继林，本代码半开源，使用本软件造成的法律后果由使用者承担。需要代码请联系李恒源：870575989@qq.com\n"
                           "X-WR-CALNAME:课程\n" +
                           "PRODID:-//Apple Inc.//Mac OS X 10.14.6//EN\n" +
                           "X-APPLE-CALENDAR-COLOR:#1D9BF6\n" +
                           "X-WR-TIMEZONE:Asia/Shanghai\n" +
                           "CALSCALE:GREGORIAN\n" +
                           "BEGIN:VTIMEZONE\n" +
                           "TZID:Asia/Shanghai\n" +
                           "BEGIN:STANDARD\n" +
                           "TZOFFSETFROM:+0900\n" +
                           "RRULE:FREQ=YEARLY;UNTIL=19910914T170000Z;BYMONTH=9;BYDAY=3SU\n" +
                           "DTSTART:19890917T020000\n" +
                           "TZNAME:GMT+8\n" +
                           "TZOFFSETTO:+0800\n" +
                           "END:STANDARD\n" +
                           "BEGIN:DAYLIGHT\n" +
                           "TZOFFSETFROM:+0800\n" +
                           "DTSTART:19910414T020000\n" +
                           "TZNAME:GMT+8\n" +
                           "TZOFFSETTO:+0900\n" +
                           "RDATE:19910414T020000\n" +
                           "END:DAYLIGHT\n" +
                           "END:VTIMEZONE\n")  # ics固定格式
    pass

if __name__ == '__main__':
    #editICShead()
    getInfo()
    #editICSfoot()
