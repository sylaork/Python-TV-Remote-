#KUMANDA PROJESİ

import random
import time

class TvRemote():
    def __init__(self, tv_state="Off", tv_voice=0, channel_list=["Fox"], channel="Fox"):
        self.tv_state=tv_state
        self.tv_voice=tv_voice
        self.channel_list=channel_list 
        self.channel=channel
        
    def tv_open(self):
        if (self.tv_state=="On"):
            print("TV is on.")
        else:
            print("TV is turning on...")  
            self.tv_state="On"  
            
    def tv_close(self):
        if(self.tv_state=="Off"):
            print("TV is off.")
        else:
            print("TV is turning off...")
            self.tv_state="Off"
            
    def voice_control(self):
        while True:
            answer=input("To increase the voice: '>' \n To turn down the voice: '<' \n Exit: \n :")  
            if(answer=='<'):
                if(answer!=0):
                    self.tv_voice-=1
                    print("Ses: ", self.tv_voice)
                
            elif(answer=='>'):
                 if(answer!=50):
                    self.tv_voice+=1
                    print("Ses: ", self.tv_voice)
            else:
                 print("voice has been updated...")
                 break
                
    def add_channel(self, channel_name):
        print("Adding the channel...")
        time.sleep(3)
        
        self.channel_list.append(channel_name)
        print("Channel has been added...")
        
    def random_channel(self):
        random= random.randint(0, len(self.channel_list)-1)
        self.channel=self.channel_list[random]
        print("Random channel is updading...")
        time.sleep(3)
        print("current channel: ", self.channel)
    
    def __len__(self):
        return len(self.channel_list)   
    
    def __str__(self):
        return "TV State: {}\n Voice: {}\n Channel List:{}\n Current Channel: {}".format(self.tv_state, self.tv_voice, self.channel_list, self.channel) 



remote= TvRemote()                       
print("""
    ******TV APP******
    1-Turn ON 
    2-Turn Off
    3-Voice Control
    4- Add Channel
    5-The Number Of Channels
    6-Random Channel Selection
    7-Information
   To Exit type 'S' !!
       """)                     
while True: 
    
    choice=input("Enter your choice:")
    
    if(choice=='S'):
        print("exit...")
        time.sleep(2)
        print("thank you!...")
        break
    
    elif(choice=="1"):
            remote.tv_open()
            
    elif(choice=="2"):
        remote.tv_close()
        
    elif(choice=="3"):
        remote.voice_control()
        
    elif(choice=="4"):
        channel_name=input("Separate the channel names with ',' :")
        channel_list=channel_name.split(",")
        for eklenecekler in channel_list:
           remote.add_channel(eklenecekler)
        
    elif(choice=="5"):
        print("number of channels: ", len(remote))
        
    elif(choice=="6"):
        remote.random_channel()
        
    elif(choice=="7"):
       print(remote) 
    
    else:
        print("Incorrect input... Try again.")
