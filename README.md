# Raspberry Pi EInk Wall

### Setup on Raspberry Pi
#### Enable SPI
```
sudo raspi-config
Choose Interface Options -> SPI -> Yes Enable SPI interface

sudo ./install.sh

sudo reboot
```

####
pip install RPi.GPIO
pip install gpiozero

#### Run Demo
```
python3 main.py
```

