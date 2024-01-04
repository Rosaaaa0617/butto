@echo off

cd /d "Z:\butto\dirty\"

call "D:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\lsprepost47\lsdynaintelvar.bat" && mpiexec -localonly -np 32 "D:\Program Files\ANSYS Inc\v221\ansys\bin\winx64\lsdyna_mpp_sp_impi.exe" i=Z:\butto\dirty\cantileverControl.key memory=100m

"C:\Users\ADMIN\AppData\Local\Apps\BETA_CAE_Systems\meta_post_v22.1.3\meta_post64.bat" -b -e -s "d:\Users\ADMIN\Desktop\nogui\meta\ModelGif.ses" 

