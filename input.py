import time
from inputs import get_gamepad
from overdrive import Overdrive
caradress = "EE:71:8D:6B:35:E4"
car = Overdrive(caradress)
numa = 0
numl = 0
numr = 0
mcs = 800
nums = 0
if car.addr == caradress:
    print("car connected")
    while 1:
        events = get_gamepad()
        for event in events:
            if not event.ev_type == "Sync":
                if event.code == "ABS_RZ":
                        carspeed = event.state
                        if carspeed > mcs:
                            carspeed = mcs
                        car.changeSpeed(carspeed, 1000)
                        print(carspeed)
                else:
                    if event.code == "BTN_TR":
                        numr = numr+1
                        if numr == 2:
                            car.changeLaneRight(500, 800)
                            print("RIGHT")
                            numr = 0
                    else:
                        if event.code == "BTN_TL":
                            numl= numl+1
                            if numl == 2:
                                car.changeLaneLeft(500, 800)
                                print("LEFT")
                                numl = 0
                        else:
                            if event.code == "BTN_SOUTH":
                                numa = numa+1
                                print(numa)
                                if numa == 2:
                                    mcs = 1000
                                    car.changeSpeed(carspeed,1000)
                                    time.sleep(1)
                                    mcs = 800
                                    car.changeSpeed(carspeed, 1000)
                                    numa = 0
                            else:
                                if event.code == "BTN_SELECT":
                                    nums = nums+1
                                    if nums == 2:
                                       car.changeSpeed(600,1000)
                                    else:
                                        if nums == 4:
                                            car.changeSpeed(0,1000)
                                            nums = 0

