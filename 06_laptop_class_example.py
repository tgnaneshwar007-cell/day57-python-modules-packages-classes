class Laptop:
    color = "White"
    screen_size = "14 inch"
    ram = 32
    storage = "1 TB"
    panel = "OLED"
    keys = 36
    body = "Metal"
    processor = "Intel Core Ultra 9 Series"
    battery = "75 Wh"

    def play(self):
        print("Playing video")


laptop1 = Laptop()

print(laptop1.color)
print(laptop1.screen_size)
print(laptop1.ram)
print(laptop1.keys)
print(laptop1.body)
print(laptop1.processor)
print(laptop1.panel)
print(laptop1.storage)
print(laptop1.battery)

laptop1.play()


laptop2 = Laptop()
print(laptop2.color)

laptop3 = Laptop()
laptop3.play()