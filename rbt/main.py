import os,sys
        
class main():
    prj_folder = os.path.abspath("")
    sys.path.append(prj_folder)
    from rbt.py import utilities,excel
    from rbt.gui import gui
    # READ SWC
    SWC_file = prj_folder+'\SWC.xlsx'
    print("breakpoint")
    swc = excel.Swc(enable=False, SWC_file=SWC_file, verbose=False)
    swc.read()
    # OPEN GUI
    gui.Gui(show=True, dict=swc, user='developer', verbose=False)

def test1():
    main()
def test2():
    print("TODO")


if __name__ == '__main__':
    test1()
    

    