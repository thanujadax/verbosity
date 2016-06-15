from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''
Textinput widget is used
https://kivy.org/docs/api-kivy.uix.textinput.html
Unicode, multiline, cursor navigation, selection and clipboard features are supported.
'''

class TextBrowserApp(App):
# layout
    def build(self):
        '''
        Method called to build up the UI. Defines all the widgets involved
        '''
        # BoxLayout arranges widgets in an adjacent manner, either vertically or horizontally
        mainLayout = BoxLayout(padding=10, orientation='vertical')
        
        # label1
        self.lbl1 = Label(text="Curent selection: ")
        mainLayout.add_widget(self.lbl1)

        # text input 1
        self.txt1 = TextInput(text='Type here ...', multiline=True)
        (self.txt1).bind(text=self.on_text)
        mainLayout.add_widget(self.txt1)
       
        # sub layout to hold 4 buttons to label the 4 different levels
        buttonRowLayout = BoxLayout(padding=10, orientation='horizontal')
        
        # button1
        btn1 = Button(text="L1")
        # define callback for button press
        btn1.bind(on_press=self.buttonClicked)
        buttonRowLayout.add_widget(btn1)
        
        # button2
        btn2 = Button(text="L2")
        # define callback for button press
        btn2.bind(on_press=self.buttonClicked)
        buttonRowLayout.add_widget(btn2)
        
        # button3
        btn3 = Button(text="L3")
        # define callback for button press
        btn3.bind(on_press=self.buttonClicked)
        buttonRowLayout.add_widget(btn3)
        
        # button4
        btn4 = Button(text="L4")
        # define callback for button press
        btn4.bind(on_press=self.buttonClicked)
        buttonRowLayout.add_widget(btn4)        

        mainLayout.add_widget(buttonRowLayout)
        return mainLayout

# button click callback
    def buttonClicked(self,btn):
        '''
        When button is clicked, display the highlighted text in lbl1
        '''
        # self.lbl1.text = "Keywords: " + self.txt1.text
        # You can get the currently selected text from the TextInput.selection_text property
        self.lbl1.text = "Current selection: " + self.txt1.selection_text

# text changed callback 
    def on_text(self, instance, value):
        '''
        Update different UI widget (label) realtime with the entered text from text input 1
        '''
        # print('Instance:',instance,' Value:',value)
        # self.lbl2.text = "Repeat text: " + value

# run app
if __name__ == "__main__":
    TextBrowserApp().run()
