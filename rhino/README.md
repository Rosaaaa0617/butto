# Grasshopper connect lines by order

## connect-by-order.gh
Need two files, one includes the coordinates(nodes.txt), the other includes how the point connects(elements.txt). Manually selecting paths.

.gh file can direct bake.

Manually delete unneeded points or lines in the export file.

## nogui.bat
@echo off
cd d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order
"C:\Program Files\Rhino 7\System\Rhino.exe" /nosplash /runscript="-Grasshopper editor load document open d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order\cmd-true.gh _Enter _-Export d:\Users\ADMIN\Desktop\nogui\rhino\connect-by-order\section.step _Enter" 

# Rhino.3dm
## Rhino模块不支持python3.12.0
1. 在anaconda下安装了python3.11版本
conda create --name python3.11 python=3.11

2. 激活环境
conda activate python3.11

3. 安装rhino模块
pip install rhino3dm
pip install compute-rhino3d

4. 在vscode选择解释器
ctrl+shift+p，选择conda的python3.11解释器

## Running and Debugging Compute Locally
https://developer.rhino3d.com/guides/compute/development/

# Rhino scripts folder
C:\Users\ADMIN\AppData\Roaming\McNeel\Rhinoceros\7.0\scripts


