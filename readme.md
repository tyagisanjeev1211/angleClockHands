# Angle between minute and hour hands of clock 

<img src="https://static.mathigon.org/cms/c411533cf1a47a6b49959d1843c8b6b1.png" width="250px" align="center">

Here user need to calculate the angle between hour and minute hands with below mentioned conditions: 

- Clock time will be in 24 hours format
- Minimum unit to check the angle is minute
- Output angle must be lowest 
- Output angle must be positive

### Approaching the problem: 

- Complete circle has $360^o$ for both hour and minute hands.
- So,
    - For minute hand angle will be changes $(360/60 = 6)^o$
    - For hour hand angle will be changes $(360/60 = 6)^o$
    - If Minute hand completed one circle $360^o$ then hours hand moves only $(360/12 )^o which is 30^o$ only
    - That mean, every minute hour hand moves $(30/60)^o which is 0.5^o$ 

### Let's start code for above points 

```
# For minute hand angle will be changes $(360/60 = 6)^o$
def get_minute_angel(minutes):
    ## minute angle
    return minutes * 6

def get_hour_angle(hours, minutes):
    ## hour angle added minute angle 
    return hours * 30 + ( minutes * 0.5 )

def angle_clock_hands(hours, minutes):

    ## clock is in 24 hours format
    hours = hours if hours < 12 else hours - 12

    ## angle must be positive 
    angle = abs( get_hour_angle(hours, minutes) - get_minute_angel(minutes) )

    ## angle must be lowest
    return min(360 - angle, angle)

# Tests
assert angle_clock_hands(3,0) == 90
assert angle_clock_hands(4,45) == 127.5
assert angle_clock_hands(4,40) == 100
assert angle_clock_hands(12,0) == 0
assert angle_clock_hands(16,0) == 120
```
