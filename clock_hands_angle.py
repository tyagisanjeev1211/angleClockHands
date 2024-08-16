def get_minute_angel(minutes):
    return minutes * 6

def get_hour_angle(hours, minutes):

    return hours * 30 + ( minutes * 0.5 )

def angle_clock_hands(hours, minutes):

    ## clock is in 24 hours format
    hours = hours if hours < 12 else hours - 12



    angle = abs( get_hour_angle(hours, minutes) - get_minute_angel(minutes) )
    return min(360 - angle, angle)
