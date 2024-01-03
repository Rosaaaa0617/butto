@echo off
:: Activate Python environment
call "C:\Users\ADMIN\anaconda3\Scripts\activate.bat" python3.11

:: Change directory to your project folder
cd /d "E:\#code\hawp"

:: Run .jpg to .json
call predic.bat duh.jpg 0.2

:: Run .json to .txt
call haha duh.json

:: Copy the txt file to the Rhino folder
copy *.txt "d:\Users\ADMIN\Desktop\nogui\rhino"

:: Rhino .txt to .step
cd /d "d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order"
"C:\Program Files\Rhino 7\System\Rhino.exe" /nosplash /runscript="-Grasshopper editor load document open d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order.gh _Enter _-Export d:\Users\ADMIN\Desktop\nogui\ansa\section.step _Enter -_Exit _No _Enter" 

:: Ansa .step to .key
cd /d "d:\Users\ADMIN\Desktop\nogui\ansa"
"C:\Users\ADMIN\AppData\Local\Apps\BETA_CAE_Systems\ansa_v22.1.3\ansa64.bat" -nogui -translfp "d:\Users\ADMIN\Desktop\nogui\ansa\extrude-mesh-plot.py"
