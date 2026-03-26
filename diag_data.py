              import serial, time

              s = serial.Serial('/dev/ttyUSB1', 9600, timeout=3)
              s.write(b'\x05')
              time.sleep(1)

              data = b''
              while True:
                  chunk = s.read(256)
                  if not chunk:
                      break
                  data += chunk

              s.close()

              # Parse and print nicely
              lines = data.decode('ascii', errors='ignore').strip().split('\r\n')
              print('--- GLUCOMETER DATA ---')
              for line in lines:
                  line = line.strip('\x01\x02\x03')
                  if ',' in line:
                      parts = line.split(',')
                      if len(parts) == 8:
                          idx, yr, mo, day, hr, mn, val, unit = parts
                          print(f'Record {idx}: {yr}-{mo}-{day} {hr}:{mn} -> {val} {unit}')
                  else:
                      print(line)
