from aiy.voice.tts import *
from aiy.cloudspeech import *
from aiy.board import Board
from aiy.leds import Leds, Color

def main():
    client = CloudSpeechClient()
    with Board() as board, Leds() as leds:
        while True:
            print("press to begin recording...")
            board.button.wait_for_press()
            leds.update(Leds.rgb_on(Color.PURPLE))
            text = client.recognize()
            print("press again for reply...")
            board.button.wait_for_press()
            leds.update(Leds.rgb_off())
            say(text)



if __name__ == "__main__":
    main()


