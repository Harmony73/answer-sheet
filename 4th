w = input ("please enter your weight (kg):")
h = input ("please enter your height (m):")
x = float (w)/(float(h)*float(h))
print ("the BMI is:",x)
if x < 18.5:
    print ("over light")
elif 18.5 <= x <23.9:
    print ("normal")
elif 23.9 <= x < 27.9:
    print ("over weight")
else:
    print ("obesity")
input ("press enter to exit")
#防止程序自动终止
