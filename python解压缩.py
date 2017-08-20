# -*- coding: utf-8 -*-
import os
import zipfile
import shutil
from unrar import rarfile
import stat

print ('脚本运行环境是python3，且需要unrar模块的支持！安装过程参照txt文档！')
print('''
# 版本功能：
# 1、不需要手动replace
# 2、自动跳过需要密码的压缩包，和损坏的压缩包，并记录在txt文件
# 3、更正了上一版有漏解压的bug
# 4、屏幕上没有不相关信息
# 5、查找无exe和msi的压缩包，并记录在txt文件
''')
print('\n\n------解压开始，请按照提示输入文件路径------\n')
document = open("错误文件记录.txt", "w+")
document1=open("无msi和exe文件记录.txt", "w+")
# zip文件解压
path_name=input("输入待解压的zip文件名称：\nG:\工作\工作原始文件\图像捕捉1\图像捕捉所有zip文件夹\n")
path_name1=input("\n输入待解压rar文件夹名称：\n")
#path_name=r'F:\python自动解压脚本\待解压zip文件'
#path_name1=r'F:\python自动解压脚本\待解压rar文件'
os.chdir(path_name)
list = os.listdir(path_name)
for file in list:
    os.chdir(r'./'+file)
    file_name_list=os.listdir(os.getcwd())
    # 删除所有已经解压的文件，重新解压
    for name in file_name_list:
        if  name.endswith(".zip"):
            zip_name=name
            break

    namelist = []
    flag=1#为跳出两层压缩包所设
    try:
        zipFile = zipfile.ZipFile(zip_name)
    except:
        document.write(file+'\n')
        print(file,":解压错误，需要密码或者是压缩包损坏!")
        os.chdir(r'..')
        continue
    # 解决乱码的问题
    for file_inzip in zipFile.namelist():
        try:
            name = file_inzip.encode('cp437').decode('gbk')
            namelist.append(name)
        except:
            namelist.append(file_inzip)
        try:
            zipFile.extract(file_inzip)
        except:
            document.write(file+'\n')
            print(file,":解压错误，需要密码或者是压缩包损坏!")
            flag=0
            break

    if flag==0:
        os.chdir(r'..')
        continue
    # 进行文件的重命名
    for i in range(len(namelist)):
        j=len(namelist)-i-1
        if os.path.isdir(zipFile.namelist()[j]) or os.path.isfile(zipFile.namelist()[j]):
            try:
                os.renames(zipFile.namelist()[j], namelist[j])
            except:
                pass
    # 搜寻无exe和msi的文件夹
    fflag=0
    for find_exe_mis in namelist:
        if find_exe_mis.endswith(".exe") or find_exe_mis.endswith(".msi"):
            fflag=1
            break
    if fflag==0:
        document1.write(file + '\n')
    zipFile.close()
    print(file, "：解压成功！")
    os.chdir(r'..')
# rar解压
os.chdir(path_name1)
list = os.listdir(path_name1)
for file in list:
    os.chdir(r'./'+file)
    file_name_list=os.listdir(os.getcwd())
    # 删除所有已经解压的文件，重新解压
    for name in file_name_list:
        if  name.endswith(".rar"):
            rar_name = name
            break
    try:
        file_inrar = rarfile.RarFile(rar_name)  # 这里写入的是需要解压的文件，别忘了加路径
        file_inrar.extractall()  # 这里写入的是你想要解压到的文件夹
    except:
        print(file, ":解压错误,需要密码或者是压缩包损坏!")
        document.write(file+'\n')
        os.chdir(r'..')
        continue
    #搜寻无exe和msi的压缩包
    fflag = 0
    for find_exe_mis in file_inrar.namelist():
        if find_exe_mis.endswith(".exe") or find_exe_mis.endswith(".msi"):
            fflag = 1
            break
    if fflag == 0:
        document1.write(file + '\n')
    print(file, "：解压成功！")
    os.chdir(r'..')
document.close()
document1.close()
print('\n\n------解压完成，详情请查看两个txt文档------')
