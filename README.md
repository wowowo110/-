### 版本特性：
* 不需要手动replace   
* 自动跳过需要密码的压缩包，和损坏的压缩包，并记录在txt文件   
* 更正了上一版有漏解压的bug   
* 屏幕上没有不相关信息   
* 查找无exe和msi的压缩包，并记录在txt文件（在脚本所在位置）  
### 注意事项
本次脚本运行环境为python3且需要unrar模块的支持！！！   
另外，除了在python中安装unrar，Windows下安装也需要安装unrar，具体方法如下:    
1. 先到RARLab官方下载库文件，http://www.rarlab.com/rar/UnRARDLL.exe ，然后安装；   
2. 安装最好选择默认路径，一般在 C:\Program Files (x86)\UnrarDLL\ 目录下；   
3. 然后重要的一步，就是添加环境变量，此电脑（我的电脑）右键，属性，找到 高级系统设置，高级 选项卡下点击 环境变量，在系统变量（注意不是用户变量）中新建，变量名输入 UNRAR_LIB_PATH ，必须一模一样，变量值要特别注意！如果你是64位系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，如果是32    位系统就输入 C:\Program Files (x86)\UnrarDLL\UnRAR.dll ，这个从unrar安装目录的内容也能看出来它是区分64和32位的;
4. 确定保存环境变量后，重启你的PyCharm，代码不变，再运行就不会出错了。这个时候依赖库已经添加到系统环境中。  
#####  `由于我们运行的软件当中有注册机等，windows可能会阻止解压，需要把工作文件夹添加进杀毒软件白名单`
