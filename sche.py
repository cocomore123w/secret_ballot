from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

import time
##

flag = False
objArray = []
###########
##
##

##

##
##
##
def scheduleTask():
    ##
    global objArray
    print(pollObjResult(objArray))
    objArray = []
    ##
    global flag
    flag = False

#############
##
##
##sched return job_id
def scheduleCreat():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    get_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 10))
    sched = BackgroundScheduler()
    # sched.add_job(some_decorated_task,'interval',seconds=3)
    sched.add_job(scheduleTask, 'date', run_date=get_date)
    return sched
##############

##############
##
##input list
##return string
def pollObjResult(pollObj):
    ##############
    ##統計投票項目
    #global pollObjArray
    pollObjArray = []
    for i in range(len(pollObj)):
        if (pollObj[i] in pollObjArray) == False:
            pollObjArray.append(pollObj[i])
    #return pollObjArray
    print(pollObjArray)
    result = ""
    ###########
    ##歸票
    for i in range(len(pollObjArray)):
        result += str(pollObjArray[i]) + "出現了"
        result += str(pollObj.count(pollObjArray[i])) + "次\n"
        result += "##########\n"

    return result
##########
##
##input #vote [vote topic] (第一次輸入發起投票)
##input #vote [vote item] (投票)
##
'''''''''
########### 無記名投票測試
while(1):
    a = input("輸入指令")
    print(flag)
    if a.split(" ")[0] == "#vote" and flag == False:

        print("投票主題 "+ a.split(" ",2)[1])
        flag = True
        sched = scheduleCreat()
        sched.start()
        #print("finish")
    elif a.split(" ")[0] == "#vote" and flag == True:

        obj = a.split(" ",2)[1]
        objArray.append(obj)
        #print("")
    else:
        print("x")
'''

'''''''''
######歸票功能測試
array = ["A","B","A","C","C","C"]
(print(pollObjResult(array)))
'''


