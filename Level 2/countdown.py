import time

countdown = input("Geben sie den gewollten Countdown ein: ")
for x in range(int(countdown)+1):
    time.sleep(0.5)
    print(int(countdown) - x)