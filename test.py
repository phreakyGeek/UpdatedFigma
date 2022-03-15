
# import serial
# import threading
# import time
# import sys
# # def strtopin():
# #     cur = db.dbs()
# #     md = cur.get_masterdata("987654321")
# #     print(md)
# #     pins = md["LearnData"].split('\n')
# #     while("" in pins) :
# #         pins.remove("")
# #     print(pins)
# #     #convert to dict
# #     a = {}
# #     for i in pins:
# #         p = i.split('-')
# #         #pin = p[0].replace('pin ',"")
# #         a[p[0].strip()] = p[1].strip().split(',')
# #         #print(a)
# #     print(a)
# #     # s1=set(a['pin 51'])
# #     # s2=set(a['pin 52'])
# #     # print(s1^s2)


# # #strtopin()

# # import sys
# # import glob
# # import serial


# # def serial_ports():
# #     """ Lists serial port names

# #         :raises EnvironmentError:
# #             On unsupported or unknown platforms
# #         :returns:
# #             A list of the serial ports available on the system
# #     """
# #     if sys.platform.startswith('win'):
# #         ports = ['COM%s' % (i + 1) for i in range(256)]
# #     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
# #         # this excludes your current terminal "/dev/tty"
# #         ports = glob.glob('/dev/tty[A-Za-z]*')
# #     elif sys.platform.startswith('darwin'):
# #         ports = glob.glob('/dev/tty.*')
# #     else:
# #         raise EnvironmentError('Unsupported platform')

# #     result = []
# #     for port in ports:
# #         try:
# #             s = serial.Serial(port)
# #             s.close()
# #             result.append(port)
# #         except (OSError, serial.SerialException):
# #             pass
# #     return result


# import glob
# def get_netlist(title):
#     print("inside get netlist")
#     serport=serial_ports("")
#     s = ser(serport[0])
#     s.write_thread(bytes("continuity netlist=yes \n", 'utf-8'))
#     read_data = s.ser.readlines()[3:]
#     #print(read_data)
#     new_data=[]
#     for i in read_data:
#         print(i.decode('utf-8').rstrip())
#         if i.decode('utf-8').rstrip().find(',')!=-1:
#             new_data.append(i.decode('utf-8').rstrip())
#             print("selected ")
#     print(new_data)
#     pins = new_data
#     #convert to dict
#     a = {}
#     for i in pins:
#         p = i.split('-')
#         #pin = p[0].replace('pin ',"")
#         a[p[0].strip()] = p[1].strip().split(',')
#         #print(a)
#     print(a)

# def serial_ports(title):
#     """ Lists serial port names

#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/tty[A-Za-z]*')
#     elif sys.platform.startswith('darwin'):
#         ports = glob.glob('/dev/tty.*')
#     else:
#         raise EnvironmentError('Unsupported platform')

#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except (OSError, serial.SerialException):
#             pass
#     return result

    

# class ser():

#     def __init__(self,serport):
#         self.ser = serial.Serial(serport, 115200,timeout=1)  # open serial port
#         print(self.ser.name)         # check which port was really used
#         self.on_recv = None
#         self.on_open = True
    
#     def write_thread(self,byte):
#         self.ser.write(byte)

#     def close_ser(self):
#         self.ser.close()


# if __name__ == '__main__':
#     print(get_netlist(""))

a = [1,2,3,4,]
b = [1,2,3,4,]

print(len(set(a).symmetric_difference(set(b))))