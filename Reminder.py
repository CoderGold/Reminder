from plyer import notification
import time
events={}
times={}
def notifications(message):
        notification.notify(
        title="!!REMINDER!!",
        message=message,
        app_icon="C:\\Users\\rajde\\downloads\\Graphicloads-100-Flat-Clock.ico",
        timeout=7,
        )
def listsave(event,time,i):
    events[i]=event
    times[i]=time

if __name__=='__main__':
    i=0
    l=0
    print("Enter Your Schedule: \n")
    while True:
        now=time.ctime()
        n=now[11]+now[12]+now[14]+now[15]
        N=int(n)
        event=input("Event Name: ")
        Time=input("When?(24 Hour Format: 1300): ")
        t=int(Time)
        if t<960 and t>=0:
            if int(Time[1]+Time[2])>=60:
                print("Invalid Time..Try Again\n")
                continue
            elif t<1000:
                print("Invalid Time...Try Again\n")
                continue
            else:
                l+=1
                listsave(event,t,i)
                print("Saved\n")
                i+=1
                inp=input("Enter More?(y/n): ")
                x=inp.lower()
                if x=='y':
                    continue
                elif x=='n':
                    break
                else:
                    print("Invalid Input...Assuming NO\n")
                    break
        elif t>=2400:
            print("Invalid Time..Try Again\n")
            continue
        elif t<N:
            print("Invalid Time...Try Again\n")
            continue
        else:
            if int(Time[2]+Time[3])>=60:
                print("Invalid Time..Try Again\n")
                continue
            else:
                l+=1
                listsave(event,t,i)
                print("Saved\n")
                i+=1
                inp=input("Enter More?(y/n): ")
                x=inp.lower()
                if x=='y':
                    continue
                elif x=='n':
                    break
                else:
                    print("Invalid Input...Assuming NO\n")
                    break

#lists are created
    print("You Will Be Notified\n")
    j=0
    while j<l:
        now=time.ctime()
        n=now[11]+now[12]+now[14]+now[15]
        N=int(n)
        hour=times[j]-N
        h=str(hour)
        if len(h)==1:
            sec=int(h[0])*60
        elif len(h)==2:
            sec=int(h[0]+h[1])*60
        elif len(h)==3:
            sec=(int(h[0])*3600)+(int(h[1]+h[2])*60)
        else:
            sec=(int(h[0]+h[1])*3600)+(int(h[2]+h[3])*60)
        time.sleep(sec)
        notifications("EVENT: "+events[j]+"TIME: "+str(times[j]))
        j+=1
