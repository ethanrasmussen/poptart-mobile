import gpiozero as gz
from time import sleep


left = gz.OutputDevice(27)
right = gz.OutputDevice(17)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("g-run s-stop f-forward e-exit")
print("\n")

while (1):

    x = input()

    if x == 'g':
        print("run")
        left.on()
        right.on()
        print("forward")
        x = 'z'

    elif x == 's':
        print("stop")
        left.off()
        right.off()
        x = 'z'

    elif x == 'f':
        print("forward")
        left.on()
        right.on()
        x = 'z'

    elif x == 'l':
        print("left")
        left.on()
        right.off()
        x = 'z'

    elif x == 'r':
        print("left")
        left.off()
        right.on()
        x = 'z'

    elif x == 'e':
        left.off()
        right.off()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")