# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:50:10 2022

@author: stefa
"""

class SpectraMax:
    """
    .dll integration for SpectraMax reader
    """
    
    def __init__(self, dll_path):
        import clr
        clr.AddReference(dll_path)
        import clr # Must be called twice
        self.AutomationObj = clr.AutomationInterface.Interface() #Verify this and change if necessary
        
    def initialize(self, ip):
        self.AutomationObj.Initialize(ip)
        
    def read(self):
        self.AutomationObject.StartRead()    
        
    def start_shake(self):
        self.AutomationObj.SetShake(True)
    
    def stop_shake(self):
        self.AutomationObj.SetShake(False)
    
    def close_drawer(self):
        self.AutomationObject.CloseDrawer()
    
    def open_drawer(self):
        self.AutomationObject.OpenDrawer()
    
