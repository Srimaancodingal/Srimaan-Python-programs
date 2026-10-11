weather = (1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1)

sunny = 0
rainy = 0

for i in weather:
    if weather[i] == 0:
        rainy = rainy + 1
    else:
        sunny+= 1
if sunny > rainy:
    print ("The weather is sunny outside ")
else :
    print ("The weather is rainy outside")