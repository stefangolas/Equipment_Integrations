import serial
import time

class PyShaker:

    def __init__(self, comport):
        
        self.interface=serial.Serial(comport, 9600, timeout=1)
        
    def _send_command(self, cmd_string):
        cmd_string = cmd_string + " \r"
        command = bytes(cmd_string, encoding='utf-8')
        self.interface.write(command)
        return self.interface.readline()
        
    def start(self, rpm=100, ramp_time=10):
        er = self._send_command("V"+str(rpm))
        er = self._send_command("A" + str(ramp_time))
        er = self._send_command("G")
        time.sleep(ramp_time)
    
    def stop(self):
        er = self._send_command("S")
    
    def get_speed(self):
        er = self._send_command("?W")


