from pathlib import Path
import pydub
from pydub.playback import play
import tkinter as tk
# loop = pydub.AudioSegment.from_mp3("mp3s/test_audio_01.mp3")
# pydub.playback.play(loop)

class AudioPlayer:
    def __init__(self, audio_path):
        file = Path(audio_path)
        self.audio = pydub.AudioSegment.from_wav(file)

    def push(self):
        play(self.audio)


if __name__ == '__main__':
    dave_testvoice01 = AudioPlayer("waves/test_audio_01.wav")
    dave_testvoice02 = AudioPlayer("waves/test_audio_02.wav")
    master = tk.Tk()
    buttons = tk.Frame(master)
    buttons.pack()
    leave_buttons=tk.Frame()
    leave_buttons.pack(side='bottom')
    button_img = tk.PhotoImage(file='images/yellow.png')
    print(button_img)
    button_01 = tk.Button(buttons, text='testvoice01', image=button_img, width=350, height=100, command=dave_testvoice01.push)
    button_01.pack(side='left')
    button_02 = tk.Button(buttons, text='testvoice02', image=button_img, width=350, height=100, command=dave_testvoice02.push)
    button_02.pack(side='right')
    kill = tk.Button(leave_buttons, text='Exit', width=25, command=master.destroy)
    kill.pack(side='bottom')
    master.mainloop()
