
from math import log
from time import time_ns
from traceback import print_tb
from component import *
import os
import json

if __name__ == "__main__":
    folder_path="./test_device"
    current_directory = os.listdir(folder_path)
    folders = [folder for folder in current_directory if os.path.isdir(os.path.join(folder_path, folder))]
    print("Folders in the current directory:")
    mqtt_init("fiber-doctor.com", 1883, "guest", "guest") #不能放到循环中，循环中反复连接会大概率连接失败，接收不到信息
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
        V_model_list = ["OFIRE-V3","OFIRE-V3-32","OFIRE-V3-64","OFIRE-V3A","OFIRE-V3A-32","OFIRE-V3A-64", "OFIRE-V4A"]
        P_model_list = ["OFIRE-P2-V3","OFIRE-P5-V3"]
        if device_model in P_model_list + V_model_list :
            mqtt_cmd_test(folder,device_id,device_model,sn)
            check_test_result(folder)
        elif device_model=="FUST-RAA" :
            pass
            # todo RAA设备的tcp命令测试   建立tcp client 发送命令 设备文件夹中要加IP。txt文件
            # tcp_cmd_test(ip)
            #check_test_result()






            ##mqtt_cmd_test部分 
            # 下面代码封装成函数
            # topic_send=f"/{device_id}/send"
            # topic_recv= f"/{device_id}/recv"
            # mqtt_subscribe(topic_send)
            # GetComponentList_cmd=read_specific_cell("./preprocess_cmd.csv", 1, 2)
            # mqtt_publish(topic_recv,GetComponentList_cmd)
            # time.sleep(1)
            # DeviceComponentList =get_DeviceComponentList() 
            # # print(f"{DeviceComponentList}")
            # json_CompontentList = json.loads(DeviceComponentList[4:])
            # if json_CompontentList["_type"] == "DeviceComponentList" :
            #    componentList  = json_CompontentList.get("componentList",[])
            #    for component in componentList : 
            #         if component["_type"] == "Otdr" :
            #             Otdr_slot = component["slot"]
            #         elif component["_type"] == "OpticSwitcher" :
            #             OpticSwitcher_slot = component["slot"]
            #         elif component["_type"] == "Rcu" :
            #             Rcu_slot = component["slot"]
            
            # StopReportOpticalPower_cmd=read_specific_cell("./preprocess_cmd.csv", 2, 2)
            # StopReportOpticalPower_cmd = set_slot(StopReportOpticalPower_cmd,Otdr_slot,OpticSwitcher_slot,Rcu_slot)
            # mqtt_publish(topic_recv,StopReportOpticalPower_cmd)
            # if device_model in P_model_list:
            #     csv_list = ["get_cmd","P_set_cmd","task_cmd"]
            # elif device_model in V_model_list :
            #     csv_list = ["get_cmd","V_set_cmd","task_cmd"]
            # for csv_file in csv_list :
            #     time.sleep(0.5)
            #     file_path = f"./{csv_file}.csv"
            #     row_number = get_row_number(file_path)
            #     # print(row_number)
            #     for row in range(1,row_number):
            #         msg_recv = read_specific_cell(file_path, row, 2)                
            #         msg_send_std = read_specific_cell(file_path, row, 3)
            #         msg_recv = set_slot(msg_recv,Otdr_slot,OpticSwitcher_slot,Rcu_slot)
            #         flag = get_flag()
            #         mqtt_publish(topic_recv,msg_recv)
            #         time.sleep(0.3)
            #         count = 0
            #         while  flag == get_flag() and count<3 :
            #             count = count + 1
            #             time.sleep(0.2)
            #         else:
            #             log_file_path = f"./test_device/{folder}/test_log.txt"  
            #             if count <3 :                            
            #                 msg_send = get_mqtt_msg()
            #                 json_send = json.loads(msg_send[4:])
            #                 json_send_std = json.loads(msg_send_std[4:])
            #                 if json_send["_type"]==json_send_std["_type"] :
            #                     print(f"{csv_file} 用例{row} ：测试成功\n")
            #                     try:
            #                         with open(log_file_path, 'a') as file:
            #                             file.write(f"{csv_file} 用例{row} ：测试成功\n")
            #                     except Exception as e:
            #                         print(f"An error occurred: {str(e)}")
            #                 else :
            #                     print(f"{csv_file} 用例{row} ：测试失败\n")
            #                     try:
            #                         with open(log_file_path, 'a') as file:
            #                             file.write(f"{csv_file} 用例{row} ：测试失败\n")
            #                             file.write(f"发送的命令 ：\n{msg_recv}\n")
            #                             file.write(f"接收到的回复 ：\n{msg_send}\n")
            #                     except Exception as e:
            #                         print(f"An error occurred: {str(e)}")

            #             else  :
            #                 print(f"ERROR: {csv_file} 用例{row} ：测试超时无回复\n")
            #                 try:
            #                     with open(log_file_path, 'a') as file:
            #                         file.write(f"ERROR: {csv_file} 用例{row} ：测试超时无回复\n")
            #                         file.write(f"发送的命令 ：\n{msg_recv}\n")
            #                         file.write(f"接收到的回复 ：\n{msg_send}\n")
            #                 except Exception as e:
            #                     print(f"An error occurred: {str(e)}")
            #         json_recv = json.loads(msg_recv[4:])
            #         if json_recv["_type"] == "SetTime" :
            #             msg_recv = get_nowtimestamp_cmd(msg_recv)
            #             mqtt_publish(topic_recv,msg_recv)
            #             time.sleep(3)                
            # print(f"{folder} test end\n")

            # result = check_for_ERROR(log_file_path)
            # result_file_path = f"./test_device/test_result.txt"
            # if result :
            #     result_f =  open(result_file_path, 'a') 
            #     result_f.write(f"ERROR：{folder}测试失败\n")
            # else :
            #     result_f =  open(result_file_path, 'a')
            #     result_f.write(f"{folder}测试成功\n")
            #     report_file_path = f"./test_device/{folder}/test_report.txt"  
            #     try:
            #         with open(report_file_path, 'w') as file:
            #             file.write(f"测试成功的测试报告\n")
            #     except Exception as e:
            #         print(f"An error occurred: {str(e)}")
        # else :
        #     # todo 建立tcp client 发送命令 设备文件夹中要加IP。txt文件
        #     pass