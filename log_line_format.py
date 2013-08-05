#-*-coding:utf-8-*-
#python—2.7.3写的  win下和centos下测试都能通过
#如果centos的 python版本只有2.4.3的话要载入time模块把时间格式转换的函数换一下，下面有介绍
#by：Z-Ping
#mail:251683535@qq.com
import re
#import time   #python版本只有2.4.3 去掉import前面的注释
import datetime

class WebLogFormat:
    def __init__(self, filename):
        self.WebFile = filename
        self.LogFormat = re.compile(r'(?P<origin>\d+\.\d+\.\d+\.\d+) '+ r'(?P<identd>-|\w+) (?P<auth>-|\w+) '
                     +r'\[(?P<date>[^\[\]:]+):(?P<time>\d+:\d+:\d+) (?P<tz>[\-\+]?\d\d\d\d)\] '
                     +r'"(-|((?P<method>\w+) (?P<path>[\S]+) (?P<protocol>[^"]+))|[^"]+)" (?P<status>\d+) (?P<bytes>-|\d+)'
                     +r'( (?P<referrer>-|"[^"]*")( (?P<client>-|"[^"]*")( (?P<cookie>-|"[^"]*"))?)?)?\s*\Z')
