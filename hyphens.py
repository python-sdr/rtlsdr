#echos rtlsdr read_samples output (without lines starting with hyphen) to console and to ~/finaldata.txt
import os
from rtlsdr import RtlSdr

os.chdir(os.path.expanduser("~/"))
sdr = RtlSdr()

sdr.sample_rate = 2.048e6 #Hz
sdr.center_freq = 70e6 # Hz
sdr.freq_correction = 60 # PPM
sdr.gain = 'auto'

sdroutput = str(sdr.read_samples(512))
savefile = open('finaldata.txt', 'w')
sdr1 = sdroutput.translate(None, '[]').split()
sdr2 = sdr1#.split('\n')
finaldata = ''
for line in sdr2:
    if not "-" in line:
        finaldata+=line+"\n"

print finaldata
savefile.write(finaldata)
savefile.close()
