# logical opertors = evaluate multiple condition (or, and, not)

# OR operator
temp = -25
is_raining = False
is_sunny = True

# if temp > 35 or temp < 0 or is_raining :
#     print("Event is cancelled")
# else: 
#     print("Event is Today")  

# AND operator 
if temp >= 25 and is_sunny :
 print("its Hot outside 🥵")
 print("its sunny 🌞")
elif temp <= 0 and is_sunny :
 print("its cold outside 🥶")
 print("its sunny 🌞")
elif 28 > temp > 0 and is_sunny:
 print("Its Warm outside 🌤")
 print("its sunny 🌞")
# NOT operator
elif temp >= 25 and not is_sunny :
 print("its Hot outside 🥵")
 print("its Cloudy ☁")
elif temp <= 0 and not is_sunny :
 print("its cold outside 🥶")
 print("its Cloudy ☁")
elif 28 > temp > 0 and not is_sunny:
 print("Its Warm outside 🌤")
 print("its Cloudy ☁")


