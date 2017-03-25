def calcCarSpeed(analogInput):
    # correct for changing the analog input after we'd done the speed tests
    analogInput = analogInput - 70 

    # polynomial constants
    const_2 = -0.0093
    const_1 = 3.0062
    const_0 = 40.485

    # second order polynomial representing the speed (kph)
    return const_2 * pow(analogInput, 2) + const_1 * analogInput + 40.485

def calcMinDist(car_speed, edge_status, jitter, latency):
    # function TBD
    print "nothing" 

# test 
for i in range(120,200):
    print calcCarSpeed(i)
