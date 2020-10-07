# phaserecon
python GUI application（PyQt） for Phase reconstruction

### PyQt 打包成exe执行文件
- 打包方式1
> pyinstaller -Fw E:\Code\phaserecon\phaserecon.py --distpath=E:\Code\exe -i E:\Code\phaserecon\icon\MyDIP.ico 
> pyinstaller -Fw 待打包py文件路径  ----distpath=程序指定生成的文件夹路径  -i  图标ico地址  
  
- 打包方式2（推荐）  
> pyinstaller -Dw E:\Code\phaserecon\phaserecon.py --distpath=E:\Code\exe -i E:\Code\phaserecon\icon\MyDIP.ico  
> 使用Enigma Virtual Box 封包
