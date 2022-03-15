import serial
import select
import threading


def read_thread():
    try:
        while True:
            read_data = ser.read()
            print(read_data.hex())
    except KeyboardInterrupt:
        raise
    except:
        pass


ser = serial.Serial('COM8', 9600)  # open serial port
print(ser.name)         # check which port was really used
threading.Thread(target=read_thread,name="read").start()
#ser.write(b'0x01')     # write a string
#ser.close()             # close port



