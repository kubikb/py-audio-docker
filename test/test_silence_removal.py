import os

from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS

dir_path = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(dir_path, "doremi.wav")
print "Test silence removal on %s..." % file_path
[Fs, x] = aIO.readAudioFile(file_path)
segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)

print "Successfully ran silence removal!"
print segments
