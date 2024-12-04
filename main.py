from machine import Pin 
led_pin = Pin(2, Pin.OUT)
from nokia_buzzer import BuzzerPlayer


led_state = True
def blink_led(freq):
    global led_state
    if freq>0:
        led_state = not led_state
        if led_state:
            print("on")
            led_pin.on()
        else:
            print("off")
            led_pin.off()

buzz = BuzzerPlayer(pin=15, callback=blink_led)

#pink_panther="t=150 8#g1 2a1 8b1 2c2 8#g1 8a1 8b1 8c2 8f2 8e2 8a1 8c2 8e2 2#d2 16d2 16c2 16a1 8g1 1a1 8#g1 2a1 8b1 2c2 8#g1 8a1 8b1 8c2 8f2 8e2 8c2 8e2 8a2 1#g2 8#g1 2a1 8b1 2c2 16#g1 8a1 8b1 8c2 8f2 8e2 8a1 8c2 8e2 2#d2 8d2 16c2 16a1"
saMayBahay = "t=150 8d3 8d3 4d3 3g3 8d3 8d3 8#a2 4d3 4c3 4- 8d3 8d3 4d3 3a3 8c4 8#a3 8#f3 4a3 4g3 4- 8d3 8d3 4d3 3g3 8a3 8g3 8d3 4f3 4#d3 8- 8c3 8d3 8#d3 8d3 8d3 8g3 8#a3 8a3 8g3 8#f3 8a3 2g3 8-";
saMayBahay += " 8f3 8g3 4f3 4d3 8- 8f3 8g3 8d3 4f3 4#d3 4- 8#d3 8f3 4#d3 4c3 8- 8f3 8a3 8f3 4g3 4f3 4- 8f3 8g3 4f3 4d3 8- 8d3 8#d3 8f3 4g3 4c4 8- 8#a3 8a3 8g3 8f3 8d3 8f3 8#a3 8a3 8f3 8a3 8c4 2#a3";
nocheBuena = "t=280 4e3 4#d3 2e3 4c3 4b2 2c3 4a2 4b2 4c3 4d3 4e3 4f3 2d3 4f3 4e3 2f3 4d3 4#c3 2d3 4b2 4c3 4d3 4e3 4f3 4g3 2e3 4a3 4#g3 2a3 4e3 4#d3 2e3 4c3 4d3 4e3 4f3 4g3 4a3 2f3 4b3 4a3 2b3 4a3 4#g3 2a3 3#g3 8#f3 3e3 8e3 4#c4 8- 8b3 8a3 2a3";
nocheBuena += " 4e3 4e3 2#c4 4a3 2e3 4e3 4d3 4e3 2#g3 4#f3 2d3 4- 4e3 4e3 2b3 4#g3 2e3 4e3 4d3 4e3 2#f3 4e3 2#c3 4- 4#c3 4d3 2e3 2#f3 2#g3 2a3 3b3 8a3 4b3 4#c4 2d4 4#c4 4b3 2#c4 4b3 4a3 2b3 4a3 4#g3 1a3";
paskoNaNaman = "t=300 4e3 2a3 3b3 8c4 2a3 4e3 4e3 4a3 4#g3 4a3 4b3 2#g3 4- 4e3 2#g3 3a3 8b3 2#g3 3#g3 8a3 4b3 4#g3 4a3 4b3 2c4 4- 4e3 2a3 3b3 8c4 2a3 4#g3 4a3 4#a3 4a3 4g3 4e3 2f3 4- 4d3 2f3 3g3 8a3 2e3 4a3 4c4 3b3 8a3 4#g3 4b3 2a3 4-";
paskoNaNaman += " 4e3 2#c4 4- 4e3 2b3 4- 4e3 4a3 8#g3 8a3 3b3 8a3 2#g3 4b2 4#c3 2d3 2e3 2#g3 3#f3 8#g3 4#f3 4e3 4#d3 4#f3 2e3 4- 4e3 2#c4 4- 4e3 2b3 4- 4e3 4a3 8#g3 8a3 3b3 8a3 2#f3 4#g3 4#f3 2e3 2d4 4#c4 2#c4 4b3 1a3 ";


#duration(1-8) note(a-g, #, -) octave 2
angPaskoSumapit ="t=150 2b2 8b2 8c3 8b2 8#a2 8b2 2g3 2e3 4g3 4g3 8g3 8e3 8a3 8g3 2g3 2#f3 2b2 8b2 8c3 8b2 8#a2 8b2 2f#3 2d#3 4f#3 4f#3 8f#3 8a3 8g3 8f#3 2e3 2b2 "
angPaskoSumapit +=" 2b2 8b2 8c3 8b2 8#a2 8b2 2g3 2e3 8e3 8e3 8#d3 8e3 8f3 8e3 8d3 8b2 2d3 2c3 8c3 8c3 8- 8b2 8a2 8b2 8c3 8e3 8b2 8b2 8- 8a2 8g2 8a2 8b2 8c3 4b2 "
angPaskoSumapit +=" 8#a2 8b2 4g3 4#f3 1e3 4d3 4a2 16b2 8c3 4d3 8c3 8c3 4b2 8a2 4b2 4- 4b2 4#f2 16g2 8a2 4b2 8a2 8a2 4g2 8#f2 4g2 4- 4c3 4a2 16b2 8c3 4d3 8c3 4b2 4g2 16a2 8b2 4c3 8b2 4#a2 8#a2 8#c3 4g3 4#f3 2#f3 "
angPaskoSumapit +="2- 2b2 8b2 8c3 8b2 8#a2 8b2 2g3 2e3 4g3 4g3 8g3 8e3 8a3 8g3 2g3 2#f3 2b2 8b2 8c3 8b2 8#a2 8b2 2f#3 2d#3 4f#3 4f#3 8f#3 8a3 8g3 8f#3 2e3 2b2 2b2 8b2 8c3 8b2 8#a2 8b2 2g3 2e3 8e3 8e3 8#d3 8e3 8f3 8e3 8d3 8b2 2d3 2c3 8c3 8c3 8- 8b2 8a2 8b2 8c3 8e3 8b2 8b2 8- 8a2 8g2 8a2 8b2 8c3 4b2 8#a2 8b2 4g3 4#f3 1e3 "


if __name__ == "__main__":
    buzz.play_nokia_tone(song=angPaskoSumapit, name="Ang Pasko ay Sumapit", transpose = 2)








thankyou ="t=150 2b1 4e2 4- 2c2 4f2 4- 4e2 8e2 8e2 4d2 4e2 4f2 4c2 4f2"
#buzz.play_nokia_tone(song=thankyou, name="Thank you", transpose = 3)






def play_loop():
    while(True):
        buzz.play_nokia_tone(song=saMayBahay, name="Sa may bahay", transpose = 2)
        buzz.play_nokia_tone(song=nocheBuena, name="Noche Buena", transpose = 1)
        buzz.play_nokia_tone(song=paskoNaNaman, name="Pasko na naman", transpose = 1)
        buzz.play_nokia_tone(song=angPaskoSumapit, name="Ang Pasko ay Sumapit", transpose = 2)
        buzz.play_nokia_tone(song=thankyou, name="Thank you", transpose = 3)


