for _ in range(int(input())):
    d,m = input().split()
    if m == 'Jan':
        print('Aquarius') if int(d) >= 21 else print('Capricorn')
    elif m == 'Feb':
        print('Pisces') if int(d) >= 20 else print('Aquarius')
    elif m == 'Mar':
        print('Aries') if int(d) >= 21 else print('Pisces')
    elif m == 'Apr':
        print('Taurus') if int(d) >= 21 else print('Aries')
    elif m == 'May':
        print('Gemini') if int(d) >= 21 else print('Taurus')
    elif m == 'Jun':
        print('Cancer') if int(d) >= 22 else print('Gemini')
    elif m == 'Jul':
        print('Leo') if int(d) >= 23 else print('Cancer')
    elif m == 'Aug':
        print('Virgo') if int(d) >= 23 else print('Leo')
    elif m == 'Sep':
        print('Libra') if int(d) >= 22 else print('Virgo')
    elif m == 'Oct':
        print('Scorpio') if int(d) >= 23 else print('Libra')
    elif m == 'Nov':
        print('Sagittarius') if int(d) >= 23 else print('Scorpio')
    elif m == 'Dec':
        print('Capricorn') if int(d) >= 22 else print('Sagittarius')
    
         
    
