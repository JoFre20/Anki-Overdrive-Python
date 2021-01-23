from overdrive import Overdrive

caradress = "EE:71:8D:6B:35:E4"
car = Overdrive(caradress)
if car.addr == caradress:
    print("Online")
    car.sendCommand("set-engine-lights 255 0 0 STEADY 0")