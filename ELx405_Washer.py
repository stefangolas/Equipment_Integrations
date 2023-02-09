# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:18:36 2022

@author: stefa
"""

class ELx405_Washer:
    
    """
    .dll integration for Biotek Elx405_Washer
    """
    
    def __init__(self, dll_path): #LHC_Runner.dll
        import clr
        clr.AddReference(dll_path)
        import clr # Must be called twice
        self.AutomationObj = clr.AutomationInterface.Interface() #Verify this and change if necessary
        
    def initialize(self, port):
        self.AutomationObj.LHC_SetCommunications(port)
        
    def run_protocol(self):
        self.AutomationObject.LHC_RunProtocol()    
        
    def load_protocol_from_file(self, path):
        self.AutomationObj.LHC_LoadProtocolFromFile(path)
    
    def load_protocol_from_flash(self, protocol):
        self.AutomationObj.LHC_LoadProtocolFromFlash(protocol)
    
    def pause_protocol(self):
        self.AutomationObject.LHC_PauseProtocol()
    
    def run_verify_manifold_test(self):
        status = self.AutomationObject.LHC_RunVerifyManifoldTest()
        return status
    
    def get_verify_manifold_status(self):
        status = self.AutomationObject.LHC_GetVerifyManifoldRunStatus
        return status