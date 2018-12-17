import qrcode

if __name__ == "__main__":
    img = qrcode.make("https://beta.itunes.apple.com/v1/app/1182814395?build=26851166")
    img.save("c:\\test.png", "png")