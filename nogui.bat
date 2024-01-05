@echo off

del /s /q "Z:\butto\output\output.gif"
del /s /q "Z:\butto\dirty\*"

:: Activate Python environment
call "C:\Users\ADMIN\anaconda3\Scripts\activate.bat" python3.11

:: Change directory to your project folder
cd /d "E:\#code\hawp"

:: Run .jpg to .json
call predic.bat "Z:\butto\input\image.jpg" 0.2

:: Run .json to .txt
cd /d "Z:\butto\dirty"
call haha image.json

:: Rhino .txt to .step
call "C:\Program Files\Rhino 7\System\Rhino.exe" /nosplash /runscript="-Grasshopper editor load document open d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order.gh _Enter _-Export Z:\butto\dirty\section.stp _Enter -_Exit _No _Enter" 


:: Ansa .step to .key
call "C:\Users\ADMIN\AppData\Local\Apps\BETA_CAE_Systems\ansa_v22.1.3\ansa64.bat" -nogui -translfp "d:\Users\ADMIN\Desktop\nogui\ansa\ExtrudeMeshSave.py" 
call "C:\Users\ADMIN\AppData\Local\Apps\BETA_CAE_Systems\ansa_v22.1.3\ansa64.bat" -nogui -translfp "d:\Users\ADMIN\Desktop\nogui\ansa\setValues.py" 


:: Ls-Run
call "D:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\lsprepost47\lsdynaintelvar.bat"  && mpiexec -localonly -np 32 "D:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\lsdyna_mpp_sp_impi.exe" i=Z:\butto\dirty\total.key memory=100m


:: Meta .gif
"C:\Users\ADMIN\AppData\Local\Apps\BETA_CAE_Systems\meta_post_v22.1.3\meta_post64.bat" -b -e -s "d:\Users\ADMIN\Desktop\nogui\meta\ModelGif.ses" 
