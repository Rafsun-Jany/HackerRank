def timeConversion(s):
    new_time = s.split(':')
    new_hour = int(new_time[0])
    new_min = new_time[1]
    new_sec = new_time[2]
    if 1 <= new_hour <= 12 and s[8:] != 'AM':
        if new_hour == 12 and int(new_min) > 0:
            return s[:8]

        new_hour = new_hour + 12
        if new_hour%24 == 0:
            new_time = '{0}:{1}:{2}'.format('00',new_min,new_sec)[:8]
            return new_time

        else:
            new_time = '{0}:{1}:{2}'.format(new_hour,new_min,new_sec)[:8]
            return new_time
    else:
        if new_hour == 12 and s[8:] == 'AM':
            new_time = '{0}:{1}:{2}'.format('00',new_min,new_sec)[:8]
            return new_time
        else:
            return s[:8]


if __name__ == '__main__':

    s = input()
    result = timeConversion(s)
    print(result)
