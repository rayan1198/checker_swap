import requests,uuid,random,re,ctypes,json,os,string,time,colorama,gc
from time import sleep
from threading import Thread,Lock
from termcolor import colored

dir_path = os.path.dirname(os.path.realpath(__file__))
colorama.init()

timestamp = str(int(time.time()))

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result






class Design:
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    s1 = '\x1b[36m1\x1b[31m'
    s2 = '\x1b[36m2\x1b[31m'
    one = f"\x1b[31m[{s1}]\x1b[31m"
    tow = f"\x1b[31m[{s2}]\x1b[31m"
    eq = '\x1b[36m≈\x1b[31m'
    eq1 = f"\x1b[31m[{eq}]\x1b[31m"
    equl = '\x1b[36m=\x1b[31m'
    equl1 = f"\x1b[31m[{equl}]\x1b[31m"
    du = '\x1b[36m≠\x1b[31m'
    du1 = f"\x1b[31m[{du}]\x1b[31m"
    plus = '\x1b[36m+\x1b[31m'
    plus2 = '\x1b[32m+\x1b[36m'
    mains = '\x1b[36m-\x1b[31m'
    SL = '\x1b[36m/\x1b[31m'
    INPUT = f"\x1b[31m[ {plus} ]\x1b[31m"
    INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
    INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"
    INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
    marka = '\x1b[32m✓\x1b[36m'
    INPUT3 = f"\x1b[36m[{marka}]\x1b[36m"
    blueq = '\x1b[36m\x1b[40m'
    reda = '\x1b[31m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    purble = '\x1b[35m\x1b[39m'
    SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
    Run = '\x1b[36m Started Running...\x1b[31m'
    under = '\x1b[35m_\x1b[39m'
    skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
    clearConsle = lambda: os.system('cls')
    
    clearTermnal = lambda: os.system('clear')
        

    qube = '['
    qube2 = ']'

    grey = 'gray'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    white = 'white'
    
    right = "Made By Psycho Rayan"
    
    banner = """
                        
                                
            ,-.          ,          .   .   
            |  \         |    o     |   |   
            |  | ,-: . . |    . ,-: |-. |-  
            |  / | | | | |    | | | | | |   
            `-'  `-` `-| `--' ' `-| ' ' `-' 
                    `-'        `-'     
"""
    


def Print(Frist_NewLine,ReadLine,mark,color,text,Last_Line):
    if Frist_NewLine:
        Frist_NewLine = "\n"
    else:
        Frist_NewLine = ""
    if ReadLine:
        ReadLine = "\r"
    else:
        ReadLine = ""
    if Last_Line:
        Last_Line = "\n"
    else:
        Last_Line = ""
    print(f"{Frist_NewLine}{ReadLine}{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)} {Last_Line}",end='')



def LoadFile(name,path):
    try:
        with open(path,"r") as myfile:
            file = myfile.read().splitlines()
    except:
        Print(False,False,"/",Design.yellow,f"{name} Path : ",False);pa = input()
        try:
            path2 = re.search(r"'(.*?)'",pa).group(1)
        except:
            path2 = re.search(r'"(.*?)"',pa).group(1)
        with open(path2,"r") as myfile:
            file = myfile.read().splitlines()
        #file = [i.strip() for i in open(path2,"r") if i]

    if len(file) <=0:
        Print(False,False,"!",Design.red,f"{name} Empty File",True)
        input()
        exit(0)
    else:
        Print(False,False,f"{len(file)}",Design.green,f"{name} Loaded Successfully ",True)
        return file
    
    
def CrateFile(name,path,text):
    try:
        with open(path,"a") as myfile:
            myfile.write(text)
    except:
        Print(False,False,"!",Design.yellow,f"{name} Error Crate File",False);
    
    if len(text) <=0:
        Print(False,False,"!",Design.red,f"{name} Empty File",True)
        input()
        exit(0)
    else:
        Print(False,False,f"+",Design.green,f"{name} Crated Successfully ",True)
        return myfile   
    
class swap:
    def __init__(self) :
        Design.clearConsle()
        print(Design.reda,Design.banner,Design.WHITE)
        self.UsersManager , self.ProxiesManager , self.Attempts , self.RS ,self.check,self.Error, self.Threads,self.check2 = 0,0,0,0,0,0,0,0
        self.run = True
        self.Locks = Lock()
        self.usernames = LoadFile("Usernames" , "list.txt")
        self.Proxies = LoadFile("Proxies","proxies.txt")
        self.sessions = LoadFile("sessions","sessions.txt")
        self.lenth_username = len(self.usernames)
        self.lenth_proxy = len(self.Proxies)
        try:
            self.sesstings = open("sesstings.txt","r").read()
            Print(False,False,f"+",Design.green,f"sesstings Loaded Successfully ",True)          
        except:
            Print(False,False,"!",Design.red,f"{Design.reda}Error loded Press Enter To Create 'sesstings.txt'",True);input()
            open("sesstings.txt","a").write('{"sesstings" : {\n\t"name": "#DayLight",\n\t"bio": "Maybe Rayan",\n\t"MSG": "Sucessfully Claimed",\n\t"Webhook": "Here",\n\t"url_imge": ""\n}}')
        self.json_sesstings = json.loads(self.sesstings)
        self.bio = self.json_sesstings["sesstings"]["bio"]
        self.Msg = self.json_sesstings["sesstings"]["MSG"]
        self.name = self.json_sesstings["sesstings"]["name"]
        self.Web_hook = self.json_sesstings["sesstings"]["Webhook"]
        self.url_imge = self.json_sesstings["sesstings"]["url_imge"]
        self.check_url = "https://i.instagram.com/api/v1/accounts/create_business_validated/"
        self.check_url2 = 'https://i.instagram.com/api/v1/accounts/create_business/'
        Print(False,False,"?",Design.yellow,f"Do You Want Swap With Proxy  [Y/n] : ",False); self.askp = input()
        Print(False,False,"?",Design.yellow,"Threads : ",False) ; self.Threads = int(input())
        Thread(target=self.switch_create_validated).start()
        Thread(target=self.switch_create).start()
        Thread(target=self.rs).start()
        Thread(target=self.th).start()
        
        
    def th(self):
        try:
            self.Threads_li = []
            for i in range(self.Threads):
                t = Thread(target=self.just_loop)
                t.daemon = True
                t.start()
                self.Threads_li.append(t)
            for t in self.Threads_li:
                t.join()
        except:pass
    def just_loop(self):
        while self.run:
            try:
                self.ProxiesManager +=1
                if self.ProxiesManager >= self.lenth_proxy:
                    self.ProxiesManager =0
                
                self.check_username(self.Proxies[self.ProxiesManager])
                self.check_username2(self.Proxies[self.ProxiesManager])
            except:pass
        sleep(3)
    def remove_session(self, Sessions):
        
        if Sessions not in self.sessions:
            return 
        self.sessions.remove(Sessions)
        if len(self.sessions) == 0:
            self.run = False

            print("\n".join(self.sessions), file=open(dir_path + "/sessions.txt", "w"))
    def remove_user(self,user):
        
        if user not in self.usernames:
            return 
        self.usernames.remove(user)
        
        if len(self.usernames) == 0:
            self.run = False
            print("\n".join(self.usernames), file=open(dir_path + "/list.txt", "w"))
            
    def switch_create_validated(self):
        while self.run:
            if self.check >= self.lenth_proxy:
                self.check =0
                if (self.check_url == "https://i.instagram.com/api/v1/accounts/create_business_validated/"):
                    
                    self.check_url = "https://i.instagram.com/api/v1/accounts/create_validated"
                    
                elif (self.check_url == "https://i.instagram.com/api/v1/accounts/create_validated"):
                    
                    self.check_url = "https://i.instagram.com/api/v1/accounts/create_business_validated/"
                
                
            sleep(3.5)
    def switch_create(self):
        while self.run:
            if self.check2 >= self.lenth_proxy:
                self.check2 = 0
                if (self.check_url2 ==  'https://i.instagram.com/api/v1/accounts/create_business/'):
                    
                    self.check_url2 = 'https://i.instagram.com/api/v1/accounts/create/'
                    
                elif (self.check_url2 == "https://i.instagram.com/api/v1/accounts/create/"):
                    
                    self.check_url2 = "https://i.instagram.com/api/v1/accounts/create_business/"
                    
                     
            sleep(3.5)
    
    def check_username(self,proxy):
            self.UsersManager +=1
            if self.UsersManager > self.lenth_username:
                self.UsersManager =0
            username = self.usernames[self.UsersManager]
            try:
                Response = requests.post(self.check_url,headers={"Cookie": f"ds_user_id={RandomString(15)} ; ds_user_id={RandomString(15)}" , "User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)","ContentType":"application/x-www-form-urlencoded; charset=UTF-8"},data={"username":username},proxies={"https": proxy,"http": proxy})
                if not Response:
                    pass
                if Response.text.__contains__('"account_created": false, "errors": {"phone_number": ["This field is required."], "device_id": ["This field is required."], "__all__": ["You need an email or confirmed phone number."]}, "existing_user": false, "status": "ok", "error_type": "required, required, no_contact_point_found"'):
                    #Print(False,True,"$",Design.red,f"@{username} Try to Hunt it . ",False)
                    return self.sett(random.choice(self.sessions),username,proxy)#self.sett(random.choice(self.sessions),username,proxy)
                elif Response.text.__contains__("taken") or Response.text.__contains__("held"):
                    self.Attempts +=1
                else:
                    self.Error +=1
                self.check +=1

            except Exception: pass
            Response.close()
            sleep(5)
    def check_username2(self,proxy):

            self.UsersManager +=1
            if self.UsersManager > self.lenth_username:
                self.UsersManager =0
                
                username = self.usernames[self.UsersManager]
                try:
                    Response = requests.post(self.check_url2,headers={"Cookie": f"ds_user_id={RandomString(15)} ; ds_user_id={RandomString(15)}" , "User-Agent": "Instagram 133.0.0.32.120 Android (25/7.1.2; 240dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)","ContentType":"application/x-www-form-urlencoded; charset=UTF-8"},data={"email":RandomString(15)+"@gmail.com","enc_password":f"#PWD_INSTAGRAM:0:0:{RandomString(15)}","first_name":"","device_id":str(uuid.uuid4()),"phone_id":str(uuid.uuid4()),"username":username},proxies={"https": proxy,"http": proxy})
                    if not Response:
                        pass
                    if Response.text.__contains__("That code isn't valid. You can request a new one."):
                       # Print(False,True,"$",Design.red,f"@{username} Try to Hunt it . ",False)
                        self.sett(random.choice(self.sessions),username,proxy)
                    elif Response.text.__contains__("isn't"):
                        self.Attempts +=1
                    else:
                        self.Error +=1
                
                    self.check2 +=1
                        
                        #Response.close()
                except Exception:pass
                Response.close()
            sleep(5)
            
    def sent_Discord(self,user):
        url = "" #webhook url, from here: https://i.imgur.com/f9XnAew.png

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {}
        #leave this out if you dont want an embed
        #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
        data["embeds"] = [
            {
                "title" : f"Details...",
                "description" : f"\n*** Sucssfully Catched => [ [@{user}](https://instagram.com/{user}) ]***\n**(``Devloped By Mexaw & RoRo``)**",
                "color": 2895667,
                "thumbnail" : {
                    "url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"},
        
                "footer" : {
                "text": f'Attempts : {self.Attempts} | R/s : {self.RS}',
                #"icon_url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"
                    
                },
                "author" :{
                    "name" : "DayLight checker"
                }
                
            }
        ]
        result = requests.post(url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            pass
        result.close()
    def sent_Discord2(self,user):
        url = "" #webhook url, from here: https://i.imgur.com/f9XnAew.png

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {}
        #leave this out if you dont want an embed
        #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
        data["embeds"] = [
            {
                "title" : f"Details...",
                "description" : f"\n*** Sucssfully Catched => [ [@{user}](https://instagram.com/{user}) ]***\n**(``Devloped By Mexaw & RoRo``)**",
                "color": 2895667,
                "thumbnail" : {
                    "url": f"{self.url_imge}"},
        
                "footer" : {
                "text": f'Attempts : {self.Attempts} | R/s : {self.RS}',
                #"icon_url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"
                    
                },
                "author" :{
                    "name" : f"{self.name}"
                }
                
            }
        ]
        result = requests.post(self.Web_hook, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            pass
        result.close()
    def done(self,user,session):
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + session})
        requests.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + session})
        Print(True,False,"$",Design.red,f"{Design.GREEN}@{user}{Design.WHITE} {self.Msg}",True)
        CrateFile(f"{user}",f"{user}.txt",f"username : {user}\nsession : {session}")
        self.sent_Discord(user)
        try:
            self.sent_Discord2(user)
        except:pass
        
        self.remove_session(''.join(session))
        self.remove_user(''.join(user))
        return False

        
        
        

    def sett(self,session,user,proxy):
        #email = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm123456789")for i in range(5)) + "@gmail.com"
            #response = send_Request(endpoint="https://i.instagram.com/api/v1/accounts/set_username/",data={"username":user},sessionid=session,timeout=5,proxies=None)
            try:
                if self.askp.lower() == "y":
                    response = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"Cookie": f"sessionid={session}" , "User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)","ContentType":"application/x-www-form-urlencoded; charset=UTF-8"},data={"username": user},proxies={"https":proxy,"http":proxy})
                else:
                    response = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"Cookie": f"sessionid={session}" , "User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 720x1280; google; G011A; G011A; intel; en_US; 289692181)","ContentType":"application/x-www-form-urlencoded; charset=UTF-8"},data={"username": user})
                    #print(response.text)
                if response.text.__contains__(user):
                        with self.Locks:
                            self.done(user,session)
                        ctypes.windll.user32.MessageBoxW(0, f"{self.Msg} : @{user}  ", f"{self.name}", 0x1000)
                if response.text.__contains__("isn't"):
                    with self.Locks:
                        Print(False,True,"!",Design.red,f"{Design.reda}@{user}{Design.blueq} I tryed To Hunt but Filed ",False)

                response.close()
            except:pass
                
                

        
    def rs(self):
        while self.run:
            befor = self.Attempts
            sleep(1)
            self.RS = self.Attempts - befor
            ctypes.windll.kernel32.SetConsoleTitleW(str(f"Attempt : {self.Attempts} / Error : {self.Error} / R/s : {self.RS}  "))
            #os.system(f"title Attempt : {self.Attempts} / Error : {self.Error} / R/s : {self.RS}  ")
            #Print(False,True,"/",Design.green,f"Attempt : {self.Attempts} / Error : {self.Error} / R/s : {self.RS}",False)
            gc.collect()

swap()
