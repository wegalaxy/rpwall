# Raspberry Pi EInk Wall

### Setup on Raspberry Pi
#### Enable SPI
```
sudo raspi-config
Choose Interface Options -> SPI -> Yes Enable SPI interface

sudo reboot
```

####
```

sudo cp rpwall.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable rpwall.service
sudo systemctl start rpwall.service

python -m venv ./venv
source ./venv/bin/activate

pip install -r requirements.txt

pip install RPi.GPIO gpiozero spidev lgpio Jetson.GPIO

```
#### Run Demo
```
python main.py
```


#### For Testing Image
```
from PIL import ImageFont, ImageDraw, Image
image = Image.open("img/db1.jpg")
font = ImageFont.truetype("./fonts/SourceSans3-Regular.ttf", 32)
disp = ImageDraw.Draw(image)
disp.text((190, 90), "Boo!!!", font=font, fill=(7, 138, 28,255))
image.show()


W = 117 #center point
H = 110
_, _, w, h = disp.textbbox((0, 0), "YEAH", font=font)
disp.text((W - w/2, H - h/2), "YEAH", font=font, fill=(7, 138, 28,255))
image.show()

```

#### 7 inch eink color
```
	0, 0, 0, black
	255, 255, 255, white
	67, 138, 28,green
	100, 64, 255, purple
	191, 0, 0, red
	255, 243, 56, yellow
	232, 126, 0 orange
	194 ,164 , 244 purple
```