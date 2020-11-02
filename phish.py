import string
from fontTools.ttLib import TTFont
import sys 

def openTTF():
	return TTFont(sys.argv[1])


def shiftTTF(nShifts, font, diccLower, diccUpper):
	for table in font['cmap'].tables:
		for char in diccLower:
			table.cmap[diccLower[char]] = char 
		for char in diccUpper:
			table.cmap[diccUpper[char]] = char
	font.save(sys.argv[3])
	print("[*] Shifting and saving our new TTF")

def shiftString(text, nShifts, diccLower, dicUpper):
	final = ''
	fullDic = {}
	fullDic.update(diccLower)
	fullDic.update(dicUpper)

	for char in text:
		if char in string.ascii_letters:
			final = final + chr(fullDic[char])
		else:
			final = final + char
	print("[*] Finish shifting our input test")
	return final


###def shiftString(text, nShifts):
###	return "".join([chr(ord(x) - nShifts) if x in string.ascii_letters else x for x in text])

def setupDicc(nShifts):
        azLower = list(string.ascii_lowercase)
        azUpper = list(string.ascii_uppercase)
        diccLower = {}
        diccUpper = {}
        shiftedLower = azLower
        shiftedUpper = azUpper
        i = 0
        cLower = 97
        cUpper = 65
        while i < nShifts:
                shiftedLower.append(shiftedLower.pop(0))
                shiftedUpper.append(shiftedUpper.pop(0))
                i = i + 1
        for c, char in enumerate(shiftedLower):
                diccLower[char] = cLower
                cLower = cLower + 1 
        for c, char in enumerate(shiftedUpper):
                diccUpper[char] = cUpper
                cUpper = cUpper + 1 
        print("[*] Finish setting up the dictionary")
        return diccLower, diccUpper


def main():
	shift = int(sys.argv[4])
	font = openTTF()
	diccLower, diccUpper = setupDicc(shift)	
	shiftTTF(shift, font, diccLower, diccUpper)
	text = open(sys.argv[2], 'r+')
	shiftedText = shiftString(text.read(), shift, diccLower, diccUpper)
	text.seek(0)
	text.truncate()
        text.write(shiftedText)
	text.close()

main()
