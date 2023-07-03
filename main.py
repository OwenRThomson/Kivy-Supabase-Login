from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

class LogIn(App):



    def build(self):
        #returns a window object with all it's widgets
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

# image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.userLbl = Label(
                        text= "Username",
                        font_size= 18,
                        color= '#9c9c9c',
                        )
        
        
        
        self.userLbl.bind(size=self.userLbl.setter('text_size'))
        
        self.window.add_widget(self.userLbl)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    size_hint= (1, 0.5),
                    font_size= 20
                    )
        
        self.window.add_widget(self.user)

        self.pwdLabel = Label(
                        text= "Password",
                        font_size= 18,
                        color= '#9c9c9c'
                        )
        self.pwdLabel.bind(size=self.pwdLabel.setter('text_size'))
        
        self.window.add_widget(self.pwdLabel)

        # text input widget
        self.password = TextInput(
                    multiline= False,
                    size_hint= (1, 0.5),
                    font_size= 20,
                    password=True
                    )

        self.window.add_widget(self.password)


        # button widget
        self.button = Button(
                      text= "Sign-In",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#32de84',
                      background_normal = "",
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):

        try:
            res = self.supabase.auth.sign_up({
                    "email": self.user.text,
                    "password": self.password.text,
            })
            
            popup = Popup(title='Test popup', content=Label(text=f"Account created for {self.user.text}"),
              auto_dismiss=True)
            popup.open()
            
        except(Exception):
            print("Error occured:", Exception)

LogIn().run()
