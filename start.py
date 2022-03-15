import webview
import serial
import db
import sys
import glob
import json
"""
An example of serverless app architecture
"""


class Api():

    def on_openport(self, title):
        print('Added item %s' % title)
        heading = webview.windows[0].get_elements('#heading')
        print('Heading:\n %s ' % heading[0]['innerHTML'])
        port = webview.windows[0].get_elements('#port')
        self.ser = ser(self.get_element("port","value"))
        self.ser.on_recv = self.on_sense
        self.learn_stat = "learn_begin"
        #print('port:\n %s ' % port[0]['text'])
        #self.set_element("port","value","123456")
        print(self.get_element("port","value"))

    def on_closeport(self, title):
        self.ser

    def on_learn(self,val):
        self.ser.write_thread(bytes([int(val)]))
        self.ser.on_recv = self.on_learn_sense
    
    def on_learn_sense(self,value):
        if value == 68:
            if self.learn_stat == "learn_begin":
                self.set_element("learn_status","textContent","Learn Started")
                self.learn_stat = "learn_started"
            else:
                self.set_element("learn_status","textContent","Learn Completed")
                self.ser.on_recv = self.on_sense
                self.learn_stat = "learn_begin"
        else:
            self.set_element("learn_status","textContent","Learn Invalid Try again")

                

    def on_write_LED(self,value):
        for i in range(0,len(value)):
            value[i] = int(value[i])
        value.append(0xFF)
        print(bytes(value))
        self.ser.write_thread(bytes(value))
 
    def on_led_update(self,value):
        print("LED is",int(value))
        self.ser.write_thread(bytes([int(value)]))
    
    def on_sense(self,value):
        print("value is ",value)
        self.set_element("sense_pin","value",int(value))

    def toggleFullscreen(self, param):
        webview.windows[0].toggle_fullscreen()
    
    def set_element(self,selector,attrib,value):
        code = 'document.getElementById("'+selector+'").'+attrib+' = "'+str(value)+'";'
        print(code)
        webview.windows[0].evaluate_js(code)

    def get_element(self,selector,attrib):
        code = 'var n = document.getElementById("'+selector+'").'+attrib+'; n;'
        return webview.windows[0].evaluate_js(code)
    
    def loadme(self,title):
        # Open a file: file
        file = open('current.txt',mode='r')
        # read all lines at once
        all_of_it = file.read()
        # close the file
        file.close()
        d = json.loads(all_of_it)
        cur = db.dbs()
        md = cur.get_masterdata(d["pno"])
        print("inside loadme")
        print(md)
        st=cur.get_testlogs_stats(d["pno"])
        print(st)
        self.set_element('partno','textContent',md['PartNo'])
        self.set_element('confail','textContent',st['continuityresult']['fail'])
        self.set_element('mainfail','textContent',st['masterresult']['fail'])
        self.set_element('mainpass','textContent',st['masterresult']['pass'])
        self.set_element('totaltest','textContent',str(int(st['masterresult']['pass'])+int(st['masterresult']['fail'])))
        try:
            self.set_element('rejpercent','textContent',str(round(int(st['masterresult']['fail'])/(int(st['masterresult']['pass'])+int(st['masterresult']['fail'])),1)*100)+'%')
        except:
            self.set_element('rejpercent','textContent','0%')
        webview.windows[0].evaluate_js("master_data="+json.dumps(md))
    
    def test_part(self,pno):
        print("inside test part")
        net = self.read_netlist("")
        if net == {}:
            print("harness not connected")
            webview.windows[0].evaluate_js("noharness();")
            self.s.close_ser()
            return
        else:
            print("back to test part")
            print(net)
            cur = db.dbs()
            m = cur.get_masterdata(pno)
            master = json.loads(m['LearnData'])
            print(master)
            print((set(master.keys())))
            print((set(net.keys())))
            print()
            fail = 0
            fail_list = []
            if len((set(master.keys()).symmetric_difference(set(net.keys())))) == 0:
                print("check 1 pass")
                for key in net.keys():
                    print("inside for")
                    print(net.get(key))
                    print(master.get(key))
                    if len(set(net.get(key)).symmetric_difference(set(master.get(key)))) == 0:
                        print("check {} pass".format(key,))
                    else:
                        print("check {} failed".format(key,))
                        print("check {} and {}".format(net[key],master[key]))
                        fail_list = net[key] + master[key]
                        fail +=1
                        break
            else:
                print("check 1 fail exit here")
                fail +=1 
            if fail !=0:
                print("test failed !!!")
                print(fail_list)
                cur.create_testlogs(pno,'fail','fail','fail','fail')
                self.s.write_thread(bytes("ind result=fail \n", 'utf-8'))
                webview.windows[0].evaluate_js("failed();")
                self.loadme("test")
            else:
                print("test passed !!!")
                cur.create_testlogs(pno,'pass','pass','pass','pass')
                self.s.write_thread(bytes("ind result=pass \n", 'utf-8'))
                webview.windows[0].evaluate_js("passed();")
                self.loadme("test")
        self.s.close_ser()

    def get_allpnos(self,title):
        print("inside get_allpnos")
        cur = db.dbs()
        pnos = cur.get_allpnos()
        print(pnos)
        return json.dumps(pnos)

    def write_curr(self,partno):
        print("inside write current part no")
        print(json.dumps({"pno":partno}))
        file = open('current.txt',mode='w+')
        # read all lines at once
        file.write(json.dumps({"pno":partno}))
        # close the file
        file.close()

    def save_masterdata(self,pno,names):
        cur = db.dbs()
        print("part no - ",pno)
        print("names - ",names)
        net = json.dumps(self.read_netlist(""))
        print("net is ",net)
        cur.create_masterdata(pno,net,names)

    def load_masterdata(self,pno): # for loading learnt data
        cur = db.dbs()
        md = cur.get_masterdata(pno)
        print(md)
        # pins = md["LearnData"].split('\n')
        # while("" in pins) :
        #     pins.remove("")
        # print(pins)
        # #convert to dict
        # a = {}
        # for i in pins:
        #     p = i.split('-')
        #     #pin = p[0].replace('pin ',"")
        #     a[p[0].strip()] = p[1].strip().split(',')
        #     #print(a)
        # print(a)
        #webview.windows[0].evaluate_js('var data ='+str(a)+';')
        webview.windows[0].evaluate_js('load_master('+json.dumps(md["LearnData"])+','+json.dumps(md["PINNames"])+');')

    def get_netlist(self,title):
        webview.windows[0].evaluate_js('netlist_load('+str(self.read_netlist(""))+');')

    def read_netlist(self,title): # for loading pin data
        print("inside get netlist")
        serport=self.serial_ports("")
        self.s = ser(serport[0])
        self.s.write_thread(bytes("continuity netlist=yes \n", 'utf-8'))
        read_data = self.s.ser.readlines()[3:]
        #print(read_data)
        new_data=[]
        for i in read_data:
            print(i.decode('utf-8').rstrip())
            if i.decode('utf-8').rstrip().find(',')!=-1:
                new_data.append(i.decode('utf-8').rstrip())
                print("selected ")
        print(new_data)
        pins = new_data
        #convert to dict
        a = {}
        for i in pins:
            p = i.split('-')
            #pin = p[0].replace('pin ',"")
            a[p[0].strip()] = p[1].strip().split(',')
            #print(a)
        print(a)
        return a

    def serial_ports(self,title):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

class ser():

    def __init__(self,serport):
        self.ser = serial.Serial(serport, 115200,timeout=1)  # open serial port
        print(self.ser.name)         # check which port was really used
        self.on_recv = None
        self.on_open = True
    
    def write_thread(self,byte):
        self.ser.write(byte)

    def close_ser(self):
        self.ser.close()

if __name__ == '__main__':
    api = Api()
    win = webview.create_window('Flywheels Advanced Testers', './main.html', js_api=api, fullscreen=True)
    webview.start(debug=True)

