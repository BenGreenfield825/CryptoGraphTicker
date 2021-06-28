# CryptoGraphTicker
## Intro
This repo is the software for a raspberry-pi based cryptocurrency price and graph ticker. This code allows a user to
choose between different formats of data, i.e. switching between price charts, viewing different coin prices, viewing
information from a user's crypto account, etc.  
<br>*put pictures here eventually*

## Current Version v0.1.0:
- Includes basic functionality
- Currently only has 1 display option - 4coin screen
- Can be run with
>python3 main.py
- Lots more to come

## Hardware Used
- Raspberry Pi Zero W
- 3.2" TFT LCD with Touchscreen Breakout Board w/MicroSD Socket - ILI9341 (https://www.adafruit.com/product/1743)
- 3D printed enclosure/stand
- Momentary switches

## Usage
### Library Dependencies
***Note:** this project was designed with a Raspberry Pi Zero W as the intended board, hence here are some things to note*
- If you are using a raspberry pi zero, make sure you use python3 and pip3 commands as the default on that board is to 
  use python 2.
- You can use the following command to automatically install all the libraries needed (check next note if using pi zero)
  >pip3 install -r requirements.txt
- ***Important:*** At the time of writing, these specific library versions are needed for this program to work on the
raspberry pi zero
  >matplotlib==3.3.3
  >
  >numpy==1.16.2
  > 
  >pandas==1.1.5
  - The pi zero does not support the latest version of numpy which creates problems for other dependencies. Through my
    own testing, these library versions will all work together. **You will probably have to first uninstall these
    libraries, and then reinstall while stating the specific version.**
    
### Software Setup

## FAQ
### Why not use CoinMarketCap?
The coinmarketcap api requires the use of a key which requires an account to generate, while the CoinbasePro api does 
not. I also wanted to use it as I personally use CoinbasePro, so I can pull personal data related to my account if
I want to (or any user if you change the settings in this project). The output to the ticker is also only on a *n* minute
update interval, so speed and precise data isn't required.

## Possible Todo's
- Include live price updating functionality as a screen option using websockets
- Web UI to easily control settings from your phone or another computer