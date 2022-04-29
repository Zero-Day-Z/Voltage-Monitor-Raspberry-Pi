# Voltage-Moitor-Raspberry-Pi
# Description
This project measures the ADC value and the voltage using the potentiometer on Raspberry Pi

# Materials Needed
## Hardware
1. Raspberry Pi x1
2. GPIO Extension Board & Ribbon Cable x1
3. Breadboard x1
4. Female-to-Female Jumper Wires x11
5. Rotary potentiometer x1
6. ADC module x1

## Software
1. ADCDevice Library
2. I2C-Tools

# Setup and Configuration
## Hardware
Below is the following pinout for this project:

![image](https://user-images.githubusercontent.com/66813474/166069353-075b1209-2701-46f9-be54-19558c3a7fe3.png)

## Software
This is where we will install the libraries listed above

### Enabling I2C
1. From the terminal, type 'sudo raspi-config'
2. Choose Interface 5 > P5 I2C > Yes > Finish
3. Type 'sudo reboot' in the command line
4. After restarting, check to make sure the module has started by typing 'lsmod | grep 12c'
5. Install 12C Tools by typing 'sudo apt-get install i2c-tools'
### Install Smbus Module
7. Install the smbus module by typing 'sudo apt-get install python3-smbus'
