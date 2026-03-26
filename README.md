# diagno-check-smart
A python script to extract data from the glucosemeter  "Diagno Check Smart" for linux (windows has its own software, though it didn't work in my own testing)

## Usage:

`python3  diagno_data.py`

it outputs to the terminal, if you want it to output to a .txt file, you can simply run it with:

`python3 diagno_data.py > glucometer_results.txt`

You might wanna edit the ttyusb1 to ttyusb0 in `s = serial.Serial('/dev/ttyUSB1', 9600, timeout=3)`, it depends on your machine
