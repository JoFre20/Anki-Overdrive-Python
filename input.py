
from inputs import get_gamepad
from overdrive import Overdrive
caradress = "EE:71:8D:6B:35:E4"
car = Overdrive(caradress)
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
                    print(carspeed)
