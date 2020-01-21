from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager , Screen
from gtts import gTTS
from pygame import mixer
import pyttsx3



class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        sa.screen_manager.current = "Second"

    def change1(self):
        sa.screen_manager.current = "Third"

    def change2(Fourth):
        sa.screen_manager.current = "Fourth"

    def change3(self):
        sa.screen_manager.current = "Fifth"

    def change4(self):
        sa.screen_manager.current = "Shape"


class SecondWindow(Screen):
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
        sa.screen_manager.current = "main"



class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk2(self):
        print("btn2")

        mixer.init()
        mixer.music.load("count.mp3")
        mixer.music.play()

    def change(self):
        sa.screen_manager.current = "main"

class FourthWindow(Screen):
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
        sa.screen_manager.current = "main"


class FifthWindow(Screen):
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
        sa.screen_manager.current = "main"


class ShapeWindow(Screen):
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
        sa.screen_manager.current = "main"


class CircleWindow(Screen):
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





class RectangleWindow(Screen):
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


class SquareWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def btn_clk(self):
#         txt="""
# वर्ग एक नियमित चतुर्भुज है, जिसका अर्थ है कि इसके चार बराबर पक्ष और चार बराबर कोण (90-डिग्री कोण) हैं"""
#         obj = gTTS(text=txt, slow=False, lang='hi')
#         obj.save("square.mp3")
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



class TriangleWindow(Screen):
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
        sa.screen_manager.current = "main"



class FirstApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main = MainWindow()
        screen = Screen(name='main')
        screen.add_widget(self.main)
        self.screen_manager.add_widget(screen)

        self.Second = SecondWindow()
        screen = Screen(name='Second')
        screen.add_widget(self.Second)
        self.screen_manager.add_widget(screen)

        self.Third = ThirdWindow()
        screen = Screen(name='Third')
        screen.add_widget(self.Third)
        self.screen_manager.add_widget(screen)

        self.Fourth = FourthWindow()
        screen = Screen(name='Fourth')
        screen.add_widget(self.Fourth)
        self.screen_manager.add_widget(screen)

        self.Fifth = FifthWindow()
        screen = Screen(name='Fifth')
        screen.add_widget(self.Fifth)
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

        return self.screen_manager

if __name__ == "__main__":
    sa=FirstApp()
    sa.run()

