# phaserecon
python GUI application（PyQt） for Phase reconstruction

### PyQt 打包成exe执行文件
> pyinstaller -Fw E:\Code\phaserecon\phaserecon.py --distpath=E:\Code\exe -i E:\Code\phaserecon\icon\MyDIP.ico --upx-dir=F:\Software\upx-3.95-win64\upx-3.95-win64
> pyinstaller -Fw 待打包py文件路径  ----distpath=程序指定生成的文件夹路径  -i  图标ico地址  --upx-dir=程序upx.exe的存放路径  

> pyinstaller -D E:\Code\phaserecon\phaserecon.py --distpath=E:\Code\exe -i E:\Code\phaserecon\icon\MyDIP.ico  
> 使用Enigma Virtual Box打包
