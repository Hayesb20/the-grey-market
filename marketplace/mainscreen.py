import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        button = Button(text = "Submit to me",
            font_size = "30sp",
            background_color = (1,1,1,1),
            color =(50,50,50,50),
            size =(15,15),
            size_hint = (.2,.2),
            pos = (400,250))
        button.bind(on_press = self.click)
        return button



    def click(self,evnet):
        print("button pressed")
        print("more please")




if __name__ == "__main__":
    app = MainApp()
    app.run()