#!/usr/bin/env python3

import argparse
from datetime import datetime
from dateutil import tz

NUMERALS = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

def instance(n):
    if n < 1 or n > 99:
        raise ValueError('Only indices from 1-99 are currently supported')
    if n <= 11:
        val = NUMERALS[n - 1]
    elif n < 20:
        val = '十' + NUMERALS[n - 11]
    else:
        val = NUMERALS[n // 10 - 1] + '十' + NUMERALS[n % 10 - 1]
    return val


def timezones(sched):
    time_info = 'HONGKONG {}\n\n'.format(
        sched.astimezone(tz.gettz('Asia/Hong_Kong')).strftime('%I:%M %p'))
    timezones = ['America/Los_Angeles', 'Europe/London', 'Europe/Berlin',
        'America/Vancouver', 'America/Toronto', 'America/Toronto']
    locations = ['Los Angeles', 'London', 'Munich', 'Vancouver', 'Toronto', 'Ottawa']
    for i in range(len(locations)):
        time_info += '{} {}\n'.format(locations[i],
            sched.astimezone(tz.gettz(timezones[i])).strftime('%I:%M %p'))
    return time_info


def message(n, t, z):
    sched = datetime.strptime(args.t, '%Y-%m-%d %I:%M %p').replace(
        tzinfo=tz.gettz('America/Los_Angeles'))
    return """通知：第{}次 Zoom 視像會議, 
{}
{}
如已裝了Zoom 可按下列網址加入會議:

https://ucla.zoom.us/j/{}

或輸入會議号碼 :
{}

歡迎各姐弟妹全體親友等隨意参加，合府統請，一齊面談。

到時見。謝謝。""".format(
    instance(args.n),
    '本星期{}，{}月{}日。本地時間:\n'.format(instance(sched.weekday() + 1),
        instance(sched.month), sched.day),
    timezones(sched),
    args.z.replace(' ', ''),
    args.z)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Meeting Invitation Generator')
    parser.add_argument('n', type=int, help='Meeting #')
    parser.add_argument('t', help='Meeting time, YYYY-MM-DD HH:MM [AP]M')
    parser.add_argument('z', help='Zoom Meeting ID')
    try:
        args = parser.parse_args()
        print(message(args.n, args.t, args.z))
    except:
        print('Use -h for help. Example usage: ./meeting.py 6 "2020-10-17 09:00 AM" "123 4567 890"')
