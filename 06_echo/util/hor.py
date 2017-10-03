sign = ""

ZODIAC = {"Aries":[(3, 21), (4, 19)], "Taurus":[(4, 20), (5, 20)], "Gemini":[(5, 21), (6, 20)], "Cancer":[(6, 21), (7, 22)], "Leo":[(7, 23), (8, 22)],"Virgo":[(8, 23), (9, 22)],"Libra":[(9, 23), (10, 22)],"Scorpio":[(10, 23), (11, 21)],"Sagittarius":[(11, 22), (12, 21)],"Capricorn":[(12, 22), (1, 19)],"Aquarius":[(1, 20), (2, 18)],"Pisces":[(2, 19), (3, 20)]}

def get_horoscope(month, day):
    for key in ZODIAC:
        if ZODIAC[key][0][0] == month:
            #if the lower date is less than the current birth-day
            if ZODIAC[key][0][1] <= day:
                sign = key
                return sign
        elif ZODIAC[key][1][0] == month:
            #if the upper date is greater than the current birth-day
            if ZODIAC[key][1][1] >= day:
                sign = key
                return sign

print get_horoscope(12, 21)


            
                
