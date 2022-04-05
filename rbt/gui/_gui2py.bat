@echo OFF
set PATH=%PATH%;C:\Users\marco.pluchino\AppData\Roaming\Python\Python38\Scripts;C:\Program Files (x86)\Melexis\Python
ECHO\ 
ECHO\
ECHO %PATH%
ECHO\
ECHO convert qrc in .py
pyrcc5.exe -o resources.py icons\resource.qrc
ECHO DONE
Pause
ECHO\
ECHO convert .ui in py
python -m PyQt5.uic.pyuic -x "ui_gui.ui" -o "ui_gui.py"
ECHO DONE
Pause
REM C:\Program Files (x86)\Melexis\Python -m PyQt5.uic.pyuic -x "C:\Users\marco.pluchino\Desktop\LavoroMarco\SVN\STEPPER_SMART_ACTUATOR\branches\LRS\TEST_674_A\verification\pydlrt\gui\gui_simple.ui" -o "C:\Users\marco.pluchino\Desktop\LavoroMarco\SVN\STEPPER_SMART_ACTUATOR\branches\LRS\TEST_674_A\verification\pydlrt\gui\gui_simple.py"