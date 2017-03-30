def calcSpeed(mouseInput):
    analogInput = int(mouseInput * 255 / 1000)

    # polynomial constants
    const_2 = -0.0092
    const_1 = 4.272
    const_0 = -212.8

    # second order polynomial representing the speed (kph)
    return str(int(const_2 * pow(analogInput, 2) + const_1 * analogInput + const_0))

def calcDist(mouseInput):
    analogInput = float(mouseInput) / 1920.0 * 80 + 120

    # polynomial constants
    const_2 = -0.0226
    const_1 = 8.881
    const_0 = -622.86

    # second order polynomial representing the speed (kph)
    return str(int(const_2 * pow(analogInput, 2) + const_1 * analogInput + const_0))

def calcActualSpeed(mouseInput):
    analogInput = int(mouseInput * 255 / 1000)


    

# test 
# for i in range(0,19):
#     print getMinDist(str(i*100))
