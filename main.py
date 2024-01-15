
from math import log
from time import time_ns
from traceback import print_tb
from component import *
import os
import json

V_model_list = ["OFIRE-V3","OFIRE-V3-32","OFIRE-V3-64","OFIRE-V3A","OFIRE-V3A-32","OFIRE-V3A-64", "OFIRE-V4A"]
P_model_list = ["OFIRE-P2-V3","OFIRE-P5-V3"]

if __name__ == "__main__":
    folder_path="./test_device"
    current_directory = os.listdir(folder_path)
    folders = [folder for folder in current_directory if os.path.isdir(os.path.join(folder_path, folder))]
    print("Folders in the current directory:")
    mqtt_init("fiber-doctor.com", 1883, "guest", "guest") 
    result_file_path = f"./test_device/test_result.txt"
    try:
        with open(result_file_path, 'w') as file:
            file.write(f"test_log print:\n")
    except Exception as e:
            print(f"An error occurred: {str(e)}")
            
    for folder in folders:
        print(f"文件夹 {folder} test start")
        folder_path=f"./test_device/{folder}"
        log_file_path = f"./test_device/{folder}/test_log.txt"  
        for file in [folder_path,log_file_path] :
            try:
                with open(file, 'w') as file:
                    file.write(f"test_log print:\n")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        device_id,device_model,sn =  get_info_from_lic(folder_path)
        print(f"{device_id}\n{device_model}\n{sn}")
        if device_model in P_model_list + V_model_list :
            mqtt_cmd_test(folder,device_id,device_model,sn)
            check_test_result(folder)
        elif device_model=="FUST-RAA" :
            pass
            # todo RAA设备的tcp命令测试   建立tcp client 发送命令 设备文件夹中要加IP。txt文件
            # tcp_cmd_test(ip)
            #check_test_result()
