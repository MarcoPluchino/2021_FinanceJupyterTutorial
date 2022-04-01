import time
import pandas as pd
class Swc():
    '''
    Import SWC file
    '''
    def __init__(self,enable = False, SWC_file = None,verbose=False):
        print(f"Swc(enable={enable},SWC_file={SWC_file},verbose={verbose})\n ")
        self.SWC_file = SWC_file
        # self.swc = None
        if enable:
            self.read()
    def read(self):
        '''
        readSwc
        '''
        time.sleep(1)
        self.swc={}
        # sheet2df
        for sheet in pd.ExcelFile(self.SWC_file,engine='openpyxl').sheet_names:  # Read all sheets
            self.swc[sheet] = pd.read_excel(self.SWC_file, sheet_name=sheet,skiprows=4,header=0)#.to_dict(orient='index')
        pd.ExcelFile(self.SWC_file).close()
        return self.swc
     
    def get(self,sheet = 'other',column = 'NAME',find = 'pyrcc5.exe',desired = 'VALUE',ISO = 'Default'):
        self.value = 'NA'
        if ISO == 'Default' and desired == 'VALUE':
            column = 'NAME'
        self.value = self.swc[sheet][self.swc[sheet][column] == find][desired].tolist()[0]
        return self.value
    def __str__(self) -> str:
        print(self.value)
        return self.value
    
def test1():
    import os
    print(os.path.abspath("SWC.xlsx"))
    swc = Swc(enable=False, SWC_file=os.path.abspath("SWC.xlsx"), verbose=False)
    swc.read()
    swc.get()
    swc.__str__()
    # swc.get_value()

if __name__ == '__main__':
    test1()

