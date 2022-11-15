duration = int(input('duration = '))

days = duration // 86400
hour = duration % 86400 // 3600
minutes = duration % 86400 % 3600 // 60
sec = duration % 86400 % 3600 % 60

if duration < 60:
    print(duration, 'сек')

elif duration < 3600 and sec == 0:
    print(minutes, 'мин')
elif duration < 60 * 60:
    print(duration // 60, 'мин', duration % 60, 'сек')

elif duration < 86400 and minutes == 0 and sec == 0:
    print(hour, 'час')
elif duration < 86400 and minutes != 0 and sec == 0:
    print(hour, 'час', minutes, 'мин')
elif duration < 86400 and minutes == 0 and sec != 0:
    print(hour, 'час', sec, 'сек')
elif duration < 86400 and minutes != 0 and sec != 0:
    print(hour, 'час', minutes, 'мин', sec, 'сек')
    
elif hour == 0 and minutes == 0 and sec == 0:
    print(days, 'дн')
elif hour != 0 and minutes == 0 and sec == 0:
    print(days, 'дн', hour, 'час')
elif hour != 0 and minutes != 0 and sec == 0:
    print(days, 'дн', hour, 'час', minutes, 'мин')
elif hour != 0 and minutes != 0 and sec != 0:
    print(days, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')
elif hour == 0 and minutes != 0 and sec == 0:
    print(days, 'дн', minutes, 'мин')
elif hour == 0 and minutes != 0 and sec != 0:
    print(days, 'дн', minutes, 'мин', sec, 'сек')
elif hour == 0 and minutes == 0 and sec != 0:
    print(days, 'дн', sec, 'сек')
elif hour != 0 and minutes == 0 and sec != 0:
    print(days, 'дн', hour, 'час', sec, 'сек')
else:
    print(days, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')

