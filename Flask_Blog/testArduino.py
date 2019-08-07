from getSerialPort import serial_ports
try:
    from pyfirmata import Arduino, util
except:
    import os
    os.system('pip install pyfirmata')
    from pyfirmata import Arduino, util


board = Arduino(serial_ports()[0])

iterator = util.Iterator(board)
iterator.start()
board.pass_time(1)

"""led = board.get_pin('d:12:o')
for i in range(5):
    led.write(1)
    board.pass_time(1)
    led.write(0)
    board.pass_time(1)"""

def getPin(pinType, pinNo, pinMode):
    return (pinType+':'+str(pinNo)+':'+pinMode)


def testWrite(digital_pins, analog_pins):
    board = Arduino(serial_ports()[0])
    iterator = util.Iterator(board)
    iterator.start()
    board.pass_time(1)
    for i in range(13,-1,-1):
        pin = board.get_pin(getPin('d',i,'o'))
        if(i in digital_pins):
            pin.write(1)
        else:
            pin.write(0)
    
    for pinNo in analog_pins:
        continue
    board.exit()

board.exit()