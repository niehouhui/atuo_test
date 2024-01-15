# xxx_cmd.csv 用例表格在飞书中更改并重新下载到当前文件夹并修改文件名，可用记事本查看csv文件的格式，必须是UTF-8 不能在其他应用上修改保存，格式会更改为ANSI或其他！！！
# 设备要建在fiber_doctor.com的阡陌服务器上，staging上的要改mqtt服务器地址

# 使用说明
以sn 序列号为名字建立文件夹，在文件夹中加入授权文件。lic文件， 然后添加进本文件的test_device文件夹中，然后直接运行main。py脚本即可，
测试完成后，在test_device文件夹中的每个设备文件夹中生成docx格式的报告和txt格式的测试日志。在test_device文件夹中的test_result。txt文件中报告每个设备测试结果。


## 需要改进的bug
小设备P型，在task——cmd处会卡回复，mqttfx上显示正常一问一答，但测试日志的回复会在上一个set——time的恢复正常时间cmd的回复set——time finished 处卡一个，之后的回复都是上一个命令的回复。
大设备V型无这问题。


## 需要做的功能
tcp连接的设备 4RU设备  命令的用例表格的创建，发什么命令，回什么命令
