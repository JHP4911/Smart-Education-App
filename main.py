from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
import numpy as np
import sqlite3
from PIL import Image
from kivy.core.audio import SoundLoader
import os
from twilio.rest import Client
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
import res
from datetime import date
from pygame import mixer
import pyttsx3
import time
studdd=-1
start_time=0
end_time=0
log=0
class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def si(self):
            sa.screen_manager.current = 'second'
    def li(self):
        global log
        global studdd
        global start_time
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('Training/trainningData.yml')
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        id = -1
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        while True:
            ret, img =cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if (confidence < 75):
                    id =id
                else:
                    id ="UNKNOWN"
            cv2.imshow('camera',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        cam.release()
        cv2.destroyAllWindows()
        comd=sqlite3.connect("Users.db")
        print("Opened database successfully")
        cmd="SELECT ID ,Type from Details"
        cursor=comd.execute(cmd)
        isrecord=0
        print(id)
        for row in cursor:
            print(row)
            print(row)
            if str(id) in row and 't'in row:
                isrecord=1
                studdd = 1
                sa.screen_manager.current = 'fourth'

            elif str(id) in row and 'S' in row:
                isrecord=1
                studdd =0
                start_time = time.time()
                log=id
                sa.screen_manager.current = 'twelve'

        if isrecord==0:
            sa.screen_manager.current = 'third'

        
    
class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def changescreen2(self):
        sa.screen_manager.current = 'first'
    def check(self):
        comd=sqlite3.connect("Users.db")
        print("Opened database successfully")
        cmd="SELECT Email,Password,Type from Details"
        cursor=comd.execute(cmd)
        isrecord=0
        
        for row in cursor:
            print(row)
            if self.emaill.text in row and self.pwdl.text in row:
                isrecord=1
                if 'T' in row:
                    sa.screen_manager.current = 'fourth'
                else:
                    sa.screen_manager.current = 'twelve'
        if isrecord==0:
            print("INVALID")

class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def change(self):
        sa.screen_manager.current = 'third'
    def changeattandance(self):
        sa.screen_manager.current = 'fifth'
    def assi(self):
        sa.screen_manager.current = 'sixth'
    def moni(self):
        sa.screen_manager.current = 'seven'
    def changel(self):
        sa.screen_manager.current = 'Learn'
class Attandance(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def back(self):
        sa.screen_manager.current = 'fourth'
    def ma(self):
        sa.screen_manager.current = 'nine'
    def view(self):
        sa.screen_manager.current = 'eleven'


class Assignment(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def back(self):
        sa.screen_manager.current = 'fourth'
    def sm(self):
        sa.screen_manager.current = 'eight'
    def a(self):
        os.system('DATA-STRUCTURES-RCS-305.pdf')
class stud(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
    def back(self):
        global end_time
        global start_time
        global log
        sa.screen_manager.current = 'third'
        end_time = time.time()
        #t= (end_time-start_time)//60
        t=5
        t=int(t)
        print(t)
        comd = sqlite3.connect("Users.db")
        print("Opened database successfully ",log)
        cmd = "SELECT ID, Time from Timer"
        cursor = comd.execute(cmd)
        isrecord = 0
        for row in cursor:
            print(row)
            if log in row:
                isrecord = 1
                cmd="update Time set Time = Time" + "{}".format(t)
                comd.execute(cmd)
        if isrecord==0:
            cmd="INSERT INTO Timer VALUES (?,?)"
            res=(log,t)
            comd.execute(cmd,res)
        comd.commit()
        comd.close()

    def changel(self):
        sa.screen_manager.current = 'Learn'
    def changemt(self):
        sa.screen_manager.current='mathtest'

class Markattandance(BoxLayout):
    today = date.today()
    l = [today,'A','A','A','A']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def changes(self):
        connection = sqlite3.connect("Users.db")
        crsr = connection.cursor()
        crsr.execute("INSERT INTO Attandance VALUES (?,?,?,?,?)",self.l)
        connection.commit()
        connection.close()
        sa.screen_manager.current = 'fifth'
    def captures(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainningData.yml')

        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        #iniciate id counter
        id = 0
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480) 
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        while True:
            ret, img =cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if (confidence < 75):
                    id =id
                else:
                    id ="UNKNOWN"        
            cv2.imshow('camera',img) 
            k = cv2.waitKey(30) & 0xff
            if k == 27: 
                break
        cam.release()
        cv2.destroyAllWindows()
        self.sp2.text=str(id)
        if id=="UNKNOWN":
            pass
        else:
            self.l[id]='P'
        
class viewatt(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_users()

    def get_users(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Attandance")
        rows = cursor.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)
    def ex(self):
        sa.screen_manager.current = 'fifth'
        
class SelectableRecycleGridLayout2(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton2(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, viewatt, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton2, self).refresh_view_attrs(viewatt, index, data)


    def apply_selection(self, viewatt, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def update_changes(self, txt):
        self.text = txt

        
class Monitor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def open(self):
        sa.screen_manager.current = 'ten'
    def sho(self):
        sa.screen_manager.current = 'coll'
    def back(self):
        sa.screen_manager.current = 'fourth'

        


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)


    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def update_changes(self, txt):
        self.text = txt


class RV(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Marks ORDER BY ID ASC")
        rows = cursor.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)
    def ex(self):
        sa.screen_manager.current = 'seven'

    
class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def changescreen(self):
        sa.screen_manager.current = 'first'
    def register(self):
        if self.name.text=="":
            self.spz.text ="NAME CANNOT BE BLANK"
        elif '@' not in self.email.text:
            self.spz.text ="INVALID EMAIL-ID"
        elif len(self.pwd.text)<8:
            self.spz.text ="PASSWORD SHOULD BE OF ATLEAST 8 CHARACTERS"
        elif self.school.text=="":
            self.spz.text ="SCHOOL NAME CANNOT BE BLANK"  
        elif not(self.idd.text.isnumeric()) :
            self.spz.text ="INVALID ID-NUMBER"
        else:
            a=str(self.name.text)
            b=str(self.email.text)
            c=str(self.idd.text)
            d=str(self.pwd.text)
            e=str(self.school.text)
            f='t'
            comd=sqlite3.connect("Users.db")
            print("Opened database successfully")
            cmd="INSERT INTO Details(Name,ID,Email,Password,School,Type) VALUES(?,?,?,?,?,?)"
            record=(a,c,b,d,e,f)
            comd.execute(cmd,record)
            comd.commit()
            comd.close()            
            faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            cam=cv2.VideoCapture(0)
            id=self.idd.text
            sampleno=0
            while(True):
                ret, img = cam.read()
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                for(x,y,w,h) in faces:
                    sampleno+=1
                    cv2.imwrite('Dataset/user.'+str(id)+'.'+str(sampleno)+'.jpg',gray[y:y+h,x:x+w])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.imshow("face",img)
                cv2.waitKey(1)
                if sampleno>20:
                    break
            cam.release() 
            cv2.destroyAllWindows()
            
            recognizer=cv2.face.LBPHFaceRecognizer_create();
            path="Dataset"
            
            def getImagesWithID(path):
                imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
                faces=[]
                IDs=[]
                for imagePath in imagePaths:
                    faceImg=Image.open(imagePath).convert('L')
                    faceNp=np.array(faceImg,'uint8')
                    a=imagePath.split('user')
                    idd=int(a[1].split('.')[1])
                    faces.append(faceNp)
                    IDs.append(idd)
                    cv2.imshow("training",faceNp)
                    cv2.waitKey(10)
                return np.array(IDs), faces
            
            Ids, faces = getImagesWithID(path)
            recognizer.train(faces, Ids)
            recognizer.save('Training/trainningData.yml')
            cam.release() 
            cv2.destroyAllWindows()  
            
            sa.screen_manager.current = 'fourth'

class Learn(BoxLayout):
    global studdd
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def changescreene(self):
        sound = SoundLoader.load('enghome.wav')
        if sound:
            sound.play()
        sa.screen_manager.current = 'English'

    def changescreenm(self):
        sa.screen_manager.current ='thirtythree'
    def changescreenb(self):
        global studdd
        if studdd ==1:
            studdd=-1
            sa.screen_manager.current = 'fourth'
        else:
            studdd =-1
            sa.screen_manager.current = 'twelve'
class English(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def changescreenf(self):
        sa.screen_manager.current = 'option'
    def echap1(self):
        sa.screen_manager.current = 'e1ch100'
    def echap2(self):
        sa.screen_manager.current = 'e1ch200'

class e1ch100(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap1intro.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch101'

class e1ch101(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap101.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch102'

class e1ch102(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap102.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch103'

class e1ch103(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap103.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch104'

class e1ch104(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap104.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch105'

class e1ch105(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap105.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch106'

class e1ch106(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap106.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch107'

class e1ch107(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('end.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'Learn'

class e1ch200(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap2intro.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch201'

class e1ch201(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap201.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch202'

class e1ch202(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap202.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch203'

class e1ch203(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap203.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch204'

class e1ch204(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap204.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch205'

class e1ch205(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap205.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch206'

class e1ch206(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap206.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch207'

class e1ch207(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('echap207.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'e1ch208'

class e1ch208(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def play_sound(self):
        sound = SoundLoader.load('end.wav')
        if sound:
            sound.play()
    def changescreen(self):
        sa.screen_manager.current = 'Learn'

class storemarks(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def changescreen(self):
        sa.screen_manager.current = 'sixth'
    def register(self):
        a=str(self.idd.text)
        b=str(self.e1.text)
        c=str(self.h1.text)
        d=str(self.m1.text)
        if(len(self.idd.text)!=8):
            self.info.text="Enter the correct ID-Number "
        elif(a=='' or b=='' or c=='' or d=='' or int(self.e1.text)>50 or int(self.h1.text)>50 or int(self.m1.text)>50):
            self.info.text="Enter the correct Marks"
        else:
            comd=sqlite3.connect("Users.db")
            print("Opened database successfully")
            cmd="SELECT * FROM Marks WHERE ID+"+str(self.idd.text)
            cmd="INSERT INTO Marks(ID,English1,Hindi1,Maths1) VALUES(?,?,?,?)"
            record=(a,b,c,d)
            comd.execute(cmd,record)
            comd.commit()
            comd.close()
            self.info.text="Sucessfully stored marks of:- " + str(self.idd.text)
            self.idd.text=''
            self.e1.text=''
            self.h1.text=''
            self.m1.text=''

class maths(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        sa.screen_manager.current = "thirtyfour"

    def change1(self):
        sa.screen_manager.current = "thirtyfive"

    def change2(Fourth):
        sa.screen_manager.current = "thirtysix"

    def change3(self):
        sa.screen_manager.current = "thirtyseven"

    def change4(self):
        sa.screen_manager.current = "Shape"
    def changeb(self):
        sa.screen_manager.current ='Learn'


class SecondWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk1(self):
        print("btn1")
        print(self.height)
        print(self.width)
        mixer.init()
        mixer.music.load("hindi.mp3")
        mixer.music.play()

    def change(self):
        sa.screen_manager.current = "thirtythree"



class ThirdWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk2(self):
        print("btn2")

        mixer.init()
        mixer.music.load("count.mp3")
        mixer.music.play()

    def change(self):
        sa.screen_manager.current = "thirtythree"

class FourthWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk3(self):
        print("btn3")
        # hindi = """
        #         अब हम गणित का अध्ययन करने जा रहे हैं।
        #  प्रथम
        #  गणित में दो नंबर कैसे जोड़े
        # उदाहरण के लिए हमारे पास दो नंबर 5 और 4 हैं। इन नंबरों को जोड़ने के लिए सबसे पहले हम इनमें से
        # एक संख्या लेते हैं और फिर इस संख्या के बाद दी गई  संख्या की गिनती करते हैं।
        # उपरोक्त उदाहरण के लिए हमने 4 लिया
        #  और इसके बाद
        # पांच बार गिना जाता है
        # 5
        #  6
        # 7
        # 8
        # 9
        # उत्तर है
        #  5 और 4 का जोड़ 9 है
        #  अब  जोड़ने का प्रयास करें """
        # obj = gTTS(text=hindi, slow=False, lang='hi')
        # obj.save("addition.mp3")
        mixer.init()
        mixer.music.load("addition.mp3")
        mixer.music.play()

    def change(self):
        sa.screen_manager.current = "thirtythree"


class FifthWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk4(self):
        print("btn4")
        mixer.init()
        mixer.music.load("subtract.mp3")
        mixer.music.play()
    # def btn_clk(self):
    #     print("btn")
    #     txt="stop"
    #     obj = gTTS(text=txt, slow=False, lang='en')
    #     obj.save("stop.mp3")
    #     mixer.init()
    #     mixer.music.load("stop.mp3")
    #     mixer.music.play()

    def change(self):
        sa.screen_manager.current = "thirtythree"


class ShapeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):
        engine = pyttsx3.init()
        hindi = "circle"
        engine.say(hindi)
        engine.runAndWait()

    def change(self):
        sa.screen_manager.current = "Circle"

    def change1(self):
        sa.screen_manager.current = "thirtythree"


class CircleWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):
#         txt="""
# एक सर्कल एक समतल में सभी बिंदुओं से मिलकर एक आकृति है जो किसी दिए गए बिंदु से एक दूरी है,
#  केंद्र; समान रूप से यह एक बिंदु से पता लगाया जाता है जो एक विमान में चलता है ताकि किसी दिए गए बिंदु से इसकी दूरी स्थिर हो। सर्कल और केंद्र के किसी भी बिंदु के बीच की दूरी को त्रिज्या कहा जाता है"""
#         obj = gTTS(text=txt, slow=False, lang='hi')
#         obj.save("circle.mp3")
        mixer.init()
        mixer.music.load("circle.mp3")
        mixer.music.play()
    def btn_shp(self):
        engine = pyttsx3.init()
        hindi = "rectangle"
        engine.say(hindi)
        engine.runAndWait()

    def change(self):
        sa.screen_manager.current = "Rectangle"



class RectangleWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):

        mixer.init()
        mixer.music.load("rectangle.mp3")
        mixer.music.play()

    def btn_shp(self):
        engine = pyttsx3.init()
        hindi = "square"
        engine.say(hindi)
        engine.runAndWait()

    def change(self):
        sa.screen_manager.current = "Square"


class SquareWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):

        mixer.init()
        mixer.music.load("square.mp3")
        mixer.music.play()
    def btn_shp(self):
        engine = pyttsx3.init()
        hindi = "triangle"
        engine.say(hindi)
        engine.runAndWait()

    def change(self):
        sa.screen_manager.current = "Triangle"

class Collective(BoxLayout):
    def bar(self):
        res.fn()
    def back(self):
        sa.screen_manager.current = 'fourth'
    def line(self):
        res.fn2()


class TriangleWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):
#         txt="""
# एक त्रिभुज एक आकृति, या दो आयामी अंतरिक्ष का एक हिस्सा है।
# इसके तीन सीधे पक्ष और तीन कोने हैं। त्र
# िभुज के तीन कोण हमेशा 180 ° (180 डिग्री) तक जुड़ते हैं।
# यह बहुभुज है जिसमें पक्षों की कम से कम संभव संख्या होती है।"""
#         obj = gTTS(text=txt, slow=False, lang='hi')
#         obj.save("triangle.mp3")
        mixer.init()
        mixer.music.load("triangle.mp3")
        mixer.music.play()
    def change(self):
        sa.screen_manager.current = "thirtythree"

mark=0
class mtq1Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def btn_clk(self):
    #     txt="यह स्पीकर है"
    #     obj = gTTS(text=txt, slow=False, lang='hi')
    #     obj.save("speaker.mp3")
    #     mixer.init()
    #     mixer.music.load("speaker.mp3")
    #     mixer.music.play()

    # def check(self, data):
    #     a=1
    #     if(a==self.data):
    #         mark=mark+1
    #     print("sum")
    #     print(mark)
    #     print("sum")

    # def change1(self):
    #     mark=mark+1
    #     print(mark)

    def change(self):
        global mark
        mark=0
        mark = mark + 1
        # print("sum")
        print(mark)
        # print("sum")
        sa.screen_manager.current = "mtq2"
        # txt = "3-2 का अंतर ज्ञात कीजिये?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq2.mp3")
        mixer.init()
        mixer.music.load("mtq2.mp3")
        mixer.music.play()

    def change1(self):
        global mark
        print(mark)
        sa.screen_manager.current = "mtq2"
        # txt = "3-2 का अंतर ज्ञात कीजिये?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq2.mp3")
        mixer.init()
        mixer.music.load("mtq2.mp3")
        mixer.music.play()




class mtq2Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def btn_clk(self):
    #     # txt="यह कीबोर्ड है"
    #     # obj = gTTS(text=txt, slow=False, lang='hi')
    #     # obj.save("keyboard.mp3")
    #     mixer.init()
    #     mixer.music.load("keyboard.mp3")
    #     mixer.music.play()

    def change(self):
        # print("3")
        global mark

        mark=mark+1
        print(mark)
        sa.screen_manager.current = "mtq3"
        # txt="2-3 का अंतर ज्ञात कीजिये?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq3.mp3")
        mixer.init()
        mixer.music.load("mtq3.mp3")
        mixer.music.play()

    def change1(self):
        # print("3")
        global mark
        print(mark)
        sa.screen_manager.current = "mtq3"
        # txt="2-3 का अंतर ज्ञात कीजिये?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq3.mp3")
        mixer.init()
        mixer.music.load("mtq3.mp3")
        mixer.music.play()

class mtq3Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def btn_clk(self):
    #     # txt="यह माउस है"
    #     # obj = gTTS(text=txt, slow=False, lang='hi')
    #     # obj.save("mouse.mp3")
    #     mixer.init()
    #     mixer.music.load("mouse.mp3")
    #     mixer.music.play()

    def change(self):
        # print("4")
        global mark
        mark = mark + 1
        # print("sum")
        print(mark)
        # print("sum")
        sa.screen_manager.current = "mtq4"
        # txt="10 के बाद क्या आया?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq4.mp3")
        mixer.init()
        mixer.music.load("mtq4.mp3")
        mixer.music.play()

    def change1(self):
        # print("4")
        global mark
        print(mark)
        sa.screen_manager.current = "mtq4"
        # txt="10 के बाद क्या आया?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq4.mp3")
        mixer.init()
        mixer.music.load("mtq4.mp3")
        mixer.music.play()

class mtq4Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def btn_clk(self):
    #     # txt="यह सीपीयू है"
    #     # obj = gTTS(text=txt, slow=False, lang='hi')
    #     # obj.save("cpu.mp3")
    #     mixer.init()
    #     mixer.music.load("cpu.mp3")
    #     mixer.music.play()
    def change(self):
        # print("5")
        global mark
        mark = mark + 1
        # print("sum")
        print(mark)
        # print("sum")
        sa.screen_manager.current = "mtq5"
        # txt = "10 से पहले क्या आया?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq5.mp3")
        mixer.init()
        mixer.music.load("mtq5.mp3")
        mixer.music.play()


    def change1(self):
        # print("5")
        global mark
        print(mark)
        sa.screen_manager.current = "mtq5"
        # txt = "10 से पहले क्या आया?"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq5.mp3")
        mixer.init()
        mixer.music.load("mtq5.mp3")
        mixer.music.play()

class mtq5Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        # print("6")
        global mark
        mark = mark + 1
        # print("sum")
        print(mark)
        # print("sum")
        sa.screen_manager.current = "finish"

    def change1(self):
        global mark
        print(mark)
        # print("6")
        sa.screen_manager.current = "finish"


class finishWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        sa.screen_manager.current = "twelve"

# class mtq5Window(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#     def change(self):
#         sa.screen_manager.current = "third"

class mathtest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        # print("1")
        global mark
        mark=0
        sa.screen_manager.current = "mtq1"
        # txt="3 + 2 का योग ज्ञात कीजिए"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mtq1.mp3")
        mixer.init()
        mixer.music.load("mtq1.mp3")
        mixer.music.play()
    def changeb(self):
        sa.screen_manager.current='twelve'
    def changeyi(self):
        sa.screen_manager.current='twelve'

class SigninApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.first = MainWindow()
        screen = Screen(name="first")
        screen.add_widget(self.first)
        self.screen_manager.add_widget(screen)

        self.second = SigninWindow()
        screen = Screen(name='second')
        screen.add_widget(self.second)
        self.screen_manager.add_widget(screen)

        self.third = Login()
        screen = Screen(name='third')
        screen.add_widget(self.third)
        self.screen_manager.add_widget(screen)
        
        self.fourth = MainMenu()
        screen = Screen(name='fourth')
        screen.add_widget(self.fourth)
        self.screen_manager.add_widget(screen)
        
        self.fifth = Attandance()
        screen = Screen(name='fifth')
        screen.add_widget(self.fifth)
        self.screen_manager.add_widget(screen)
     
        self.sixth = Assignment()
        screen = Screen(name='sixth')
        screen.add_widget(self.sixth)
        self.screen_manager.add_widget(screen)
    
        self.seven = Monitor()
        screen = Screen(name='seven')
        screen.add_widget(self.seven)
        self.screen_manager.add_widget(screen)
        
        self.eight = storemarks()
        screen = Screen(name='eight')
        screen.add_widget(self.eight)
        self.screen_manager.add_widget(screen)
        
        self.nine = Markattandance()
        screen = Screen(name='nine')
        screen.add_widget(self.nine)
        self.screen_manager.add_widget(screen)

        self.ten = RV()
        screen = Screen(name='ten')
        screen.add_widget(self.ten)
        self.screen_manager.add_widget(screen)

        self.eleven = viewatt()
        screen = Screen(name='eleven')
        screen.add_widget(self.eleven)
        self.screen_manager.add_widget(screen)        
        
        self.twelve = stud()
        screen = Screen(name='twelve')
        screen.add_widget(self.twelve)
        self.screen_manager.add_widget(screen)        


        self.thirteen = Learn()
        screen = Screen(name="Learn")
        screen.add_widget(self.thirteen)
        self.screen_manager.add_widget(screen)

        self.fourteen = English()
        screen = Screen(name='English')
        screen.add_widget(self.fourteen)
        self.screen_manager.add_widget(screen)

        self.fifteen = e1ch100()
        screen = Screen(name = 'e1ch100')
        screen.add_widget(self.fifteen)
        self.screen_manager.add_widget(screen)

        self.sixteen = e1ch101()
        screen = Screen(name = 'e1ch101')
        screen.add_widget(self.sixteen)
        self.screen_manager.add_widget(screen)

        self.seventeen = e1ch102()
        screen = Screen(name = 'e1ch102')
        screen.add_widget(self.seventeen)
        self.screen_manager.add_widget(screen)

        self.eighteen = e1ch103()
        screen = Screen(name = 'e1ch103')
        screen.add_widget(self.eighteen)
        self.screen_manager.add_widget(screen)

        self.nineteen = e1ch104()
        screen = Screen(name = 'e1ch104')
        screen.add_widget(self.nineteen)
        self.screen_manager.add_widget(screen)

        self.twenty = e1ch105()
        screen = Screen(name = 'e1ch105')
        screen.add_widget(self.twenty)
        self.screen_manager.add_widget(screen)

        self.twentyone = e1ch106()
        screen = Screen(name = 'e1ch106')
        screen.add_widget(self.twentyone)
        self.screen_manager.add_widget(screen)

        self.twenty2 = e1ch107()
        screen = Screen(name = 'e1ch107')
        screen.add_widget(self.twenty2)
        self.screen_manager.add_widget(screen)

        self.twentytwo = e1ch200()
        screen = Screen(name = 'e1ch200')
        screen.add_widget(self.twentytwo)
        self.screen_manager.add_widget(screen)

        self.twentythree = e1ch201()
        screen = Screen(name = 'e1ch201')
        screen.add_widget(self.twentythree)
        self.screen_manager.add_widget(screen)

        self.twentyfour = e1ch202()
        screen = Screen(name = 'e1ch202')
        screen.add_widget(self.twentyfour)
        self.screen_manager.add_widget(screen)

        self.twentyfive = e1ch203()
        screen = Screen(name = 'e1ch203')
        screen.add_widget(self.twentyfive)
        self.screen_manager.add_widget(screen)

        self.twentysix = e1ch204()
        screen = Screen(name = 'e1ch204')
        screen.add_widget(self.twentysix)
        self.screen_manager.add_widget(screen)

        self.twentyseven = e1ch205()
        screen = Screen(name = 'e1ch205')
        screen.add_widget(self.twentyseven)
        self.screen_manager.add_widget(screen)

        self.twentyeight = e1ch206()
        screen = Screen(name = 'e1ch206')
        screen.add_widget(self.twentyeight)
        self.screen_manager.add_widget(screen)

        self.twentynine = e1ch207()
        screen = Screen(name = 'e1ch207')
        screen.add_widget(self.twentynine)
        self.screen_manager.add_widget(screen)

        self.thirty = e1ch208()
        screen = Screen(name = 'e1ch208')
        screen.add_widget(self.thirty)
        self.screen_manager.add_widget(screen)

        self.thirtyone = e1ch107()
        screen = Screen(name = 'e1ch107')
        screen.add_widget(self.thirtyone)

        self.thirtythree = maths()
        screen = Screen(name='thirtythree')
        screen.add_widget(self.thirtythree)
        self.screen_manager.add_widget(screen)

        self.thirtyfour = SecondWindow()
        screen = Screen(name='thirtyfour')
        screen.add_widget(self.thirtyfour)
        self.screen_manager.add_widget(screen)

        self.thirtyfive = ThirdWindow()
        screen = Screen(name='thirtyfive')
        screen.add_widget(self.thirtyfive)
        self.screen_manager.add_widget(screen)

        self.thirtysix = FourthWindow()
        screen = Screen(name='thirtysix')
        screen.add_widget(self.thirtysix)
        self.screen_manager.add_widget(screen)

        self.thirtyseven = FifthWindow()
        screen = Screen(name='thirtyseven')
        screen.add_widget(self.thirtyseven)
        self.screen_manager.add_widget(screen)

        self.Shape = ShapeWindow()
        screen = Screen(name='Shape')
        screen.add_widget(self.Shape)
        self.screen_manager.add_widget(screen)

        self.Circle = CircleWindow()
        screen = Screen(name='Circle')
        screen.add_widget(self.Circle)
        self.screen_manager.add_widget(screen)


        self.Rectangle = RectangleWindow()
        screen = Screen(name='Rectangle')
        screen.add_widget(self.Rectangle)
        self.screen_manager.add_widget(screen)

        self.Triangle = TriangleWindow()
        screen = Screen(name='Triangle')
        screen.add_widget(self.Triangle)
        self.screen_manager.add_widget(screen)

        self.Square = SquareWindow()
        screen = Screen(name='Square')
        screen.add_widget(self.Square)
        self.screen_manager.add_widget(screen)

        self.coll = Collective()
        screen = Screen(name='coll')
        screen.add_widget(self.coll)
        self.screen_manager.add_widget(screen)

        self.mathtest=mathtest()
        screen=Screen(name='mathtest')
        screen.add_widget(self.mathtest)
        self.screen_manager.add_widget(screen)

        self.mtq1 = mtq1Window()
        screen = Screen(name='mtq1')
        screen.add_widget(self.mtq1)
        self.screen_manager.add_widget(screen)

        self.mtq2 = mtq2Window()
        screen = Screen(name='mtq2')
        screen.add_widget(self.mtq2)
        self.screen_manager.add_widget(screen)

        self.mtq3 = mtq3Window()
        screen = Screen(name='mtq3')
        screen.add_widget(self.mtq3)
        self.screen_manager.add_widget(screen)

        self.mtq4 = mtq4Window()
        screen = Screen(name='mtq4')
        screen.add_widget(self.mtq4)
        self.screen_manager.add_widget(screen)

        self.mtq5 = mtq5Window()
        screen = Screen(name='mtq5')
        screen.add_widget(self.mtq5)
        self.screen_manager.add_widget(screen)

        self.finish = finishWindow()
        screen = Screen(name='finish')
        screen.add_widget(self.finish)
        self.screen_manager.add_widget(screen)


        return self.screen_manager
        
    

if __name__=="__main__":
    sa = SigninApp()
    sa.run()
"""         content="Hello "+self.lineEdit_3.text()+"!\n\nYou have requested for verification. Here is your OTP verification code: "+ self.code+" \n\nDo not share this code with anyone.\n\nAnd thank you so much for connecting with us :) We at TMS will always be there to help you.\n\n\nRegards,\nTeam TMS."
            print(self.code)
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            recipient=[]
            sender='noreply.taxims@gmail.com'
            mail.login('noreply.taxims@gmail.com','tms@98765')
            header="Subject:You just signed up on TMS\n"
            '''"To:"+recipient+"\n"+"From:"+sender+"\n"+'''
            content=header+content
            mail.sendmail(sender,recipient,content)
            mail.close().
            msg = QMessageBox.information(self,"OTP","An OTP has been sent to your Email ID")
"""
