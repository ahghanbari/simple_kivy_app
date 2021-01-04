#!/usr/bin/python3

# Written by arash.ph

# Profesor: Dr Amiri
# TA: Mr Mahdi BG
# Algorighm Design
# amirhosein ghanbari 9706393

# Project 2

# First Part of Algorithm Part : Merge Sort, Line 110
# Second Part of Algorithm Part : Implementation of Algorithm, Line 146

# Library for GUI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# Library for handling wrong input
import re


# Main Class for GUI Design
class MainApp(App):

    def build(self):
        Window.clearcolor = (0, .5, 1, 0)

        main_layout = BoxLayout(padding=30, spacing=50)
        keyB_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=False, halign="left", font_size=25, hint_text="I am empty :("
        )
        img = Image(source='welcome.jpeg',
                    size_hint=(3, 3),
                    pos_hint={'center_x':.5, 'center_y':.5})

        keyB_layout.add_widget(img)
        keyB_layout.add_widget(Label(text='Hello Sweet Heart :)', font_size=25))
        keyB_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["0", "space", "c"],
        ]
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=25,
                    size_hint=(.9, .8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            keyB_layout.add_widget(h_layout)

        h_layout = BoxLayout(spacing=10)
        btnExit = Button(
                    text='Exit',
                    font_size=25,
                    size_hint=(.9, .8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
        btnExit.bind(on_press=self.exit)
        h_layout.add_widget(btnExit)
        keyB_layout.add_widget(h_layout)

        main_layout.add_widget(keyB_layout)
        Righ_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(Righ_layout)
    
        self.bob_layout = BoxLayout(orientation="horizontal")
        
        Righ_layout.add_widget(self.bob_layout)
        
        self.patrick_layout = BoxLayout(orientation="horizontal")
        Righ_layout.add_widget(self.patrick_layout)
        
        Clock.schedule_interval(self.solve, 1)

        return main_layout


    def exit(self):
        exitCheck = True
        

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "space":
            # Clear the solution widget
            self.solution.text += " "
        elif button_text == "c":
            self.solution.text = self.solution.text[:-1]
        else:
            self.solution.text = current + button_text
        

    # MergeSort
    # First part of Algorith Part
    def mergeSort(self, arr):
        if len(arr) > 1:

            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        # End of First part of Algorith Part


    # Second Part of Algorithm Part
    def solve(self, instance):
        if self.solution.text == '':
            return

        tempList = re.findall('[0-9\s]+', self.solution.text)
        
        WrongInput = False
        if tempList == [] or tempList[0] != self.solution.text:
            WrongInput = True

        if not WrongInput:
            cards = list(map(int, self.solution.text.split()))
            patrick = []
            bob = []
            self.mergeSort(cards)
            cards = cards[::-1]

            pat_score = 0
            bob_score = 0

            for i in cards:
                if i == 0:
                    continue
                if pat_score < bob_score:
                    patrick.append(i)
                    pat_score += i
                else:
                    bob.append(i)
                    bob_score += i

            # End of Second Part of Algorithm Part
            # now, we have 2 list, patrick and bob, the array of their Cards, and
            # their score in bob_score and pat_score

            temp_bob = str(bob)
            num = 0
            for i in bob:
                num += i
            temp_bob = '{' + temp_bob[1:-1] + '}' + "\nScore: " + str(num)

            temp_pat = str(patrick)
            num = 0
            for i in patrick:
                num += i
            signature = '\n\n\n         [color=#000000][size=12]arash.ph17@gmail.com[/size][/color]'
            temp_pat = '\n\n\n{' + temp_pat[1:-1] + '}' + "\nScore: " + str(num) + signature

        else:
            signature = '\n\n\n         [color=#000000][size=12]arash.ph17@gmail.com[/size][/color]'
            temp_bob = "Hey Dude!\nWhat's wrong\nwith you?!"
            temp_pat = "\n\n\nPlease use\nonly numbers." + signature
     

        self.patrick_layout.clear_widgets()
        self.bob_layout.clear_widgets()

        img_bob = Image(source='b.png',
                    size_hint=(.5, .5),
                    pos_hint={'center_x':0, 'center_y':.5})

        self.bob_layout.add_widget(Label(text=temp_bob , font_size ='30sp'))
        self.bob_layout.add_widget(img_bob)

        img_patrick = Image(source='p.png',
                    size_hint=(.5, .5),
                    pos_hint={'center_x':1, 'center_y':.5})
        self.patrick_layout.add_widget(img_patrick)
        self.patrick_layout.add_widget(Label(text=temp_pat, font_size ='30sp', markup=True))


        
# running the App
if __name__ == '__main__':
    MainApp().run()
