import time
from inputs import get_gamepad
from overdrive import Overdrive
caradress = "EE:71:8D:6B:35:E4"
car = Overdrive(caradress)
numl = 0
numr = 0
if car.addr == caradress:
    print("car connected")
    while 1:
        events = get_gamepad()
        for event in events:
            if not event.ev_type == "Sync":
                if event.code == "ABS_RZ":
                    carspeed = event.state
                    if carspeed > 800:
                        carspeed = 800

                    car.changeSpeed(carspeed, 1000)
                else:
                    if event.code == "BTN_TR":
                        print("Can RIGHT")
                        numr = numr+1
                        print(numr)
                        if numr == 2:
                            car.changeLaneRight(carspeed, 800)
                            print("RIGHT")
                            numr = 0
                    else:
                        if event.code == "BTN_TL":
                            print("Can LEFT")
                            numl= numl+1
                            print(numl)
                            if numl == 2:
                                car.changeLaneLeft(carspeed, 800)
                                print("LEFT")
                                numl = 0