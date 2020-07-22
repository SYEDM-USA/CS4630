#String search - b04searh.py
import re
myString = "Python for computational data sciences"

tationSS = myString.find('tation')
forcomputSS = myString.find ('forcomput')
tationSS2 = myString.find('tation', 18, 35)
onSSall = re.findall("on", myString)

print ('Given string', myString)
print (tationSS, " ", tationSS2, " ", \
onSSall, forcomputSS )

