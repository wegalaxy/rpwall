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
python -m venv ./venv
source ./venv/bin/activate

pip install -r requirements.txt

pip install RPi.GPIO gpiozero spidev lgpio Jetson.GPIO

```
#### Run Demo
```
python main.py
```

