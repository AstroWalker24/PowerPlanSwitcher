## ماشااللہ


import subprocess 
import datetime
import sys
import time

# define the power plans 
power_plans = {
    'balanced':'381b4222-f694-41f0-9685-ff5bb260df2e',
    'high_performance':'8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c',
    'power_saver':'a1841308-3541-4fab-bc81-f71556f20b4a'
}


def switch_powerplans(power_plan):
    if power_plan in power_plans:
        # retreive the GUID of the power plan
        power_plan_guid = power_plans[power_plan]
        # setting the power plan using the powercfg command 
        try:
            subprocess.run(['powercfg','-setactive',power_plan_guid],check=True)
            return 1
        except subprocess.CalledProcessError as e :
            print("Error occured while switching the power plan",e)
            return -1
        
    
    else :
        print("Invalid Power Plan")
        return -1




# switching the power plan based on the time of the day 
def main():
    # running the infinite loop and checks for every 1 hour 
    while(True):
        # fetching the current time
        now_date,now_time = str(datetime.datetime.now()).split()

        if now_time[0:2]>'00' and now_time[0:2]<'08':
            # use the power saver plan
            status_code = switch_powerplans('power_saver')
            if status_code == -1:
                sys.exit()
            
        elif now_time[0:2]>'08' and now_time[0:2]<'18':
            # use the balanced plan
            switch_powerplans('balanced')
            if status_code == -1:
                sys.exit()

        elif now_time[0:2]>'18' and now_time[0:2]<'00':
            # use the high performance plan
            switch_powerplans('high_performance')
            if status_code == -1:
                sys.exit()
            
        # sleep for 1 hour 
        time.sleep(3600)

     
    

if __name__=="__main__":
    main()


