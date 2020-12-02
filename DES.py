import sys, numpy, array

klartext = ''
schlussel = ''
ausgabe_IP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
halfte1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
halfte2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

############################### Überprüfung ##################################
if len(sys.argv) < 3:
	print ('zu wenig Argumente. Klartext als Arg1 und Schlüssel als Arg2')
	quit()
else:
	klartext = str(sys.argv[1])
	schlussel = str(sys.argv[2])

if (len(klartext) != 64) and (len(schlussel) != 48):
	print('Klartext oder Schlüssel zu kurz oder zu lang')
	quit()
############################ Eingangspermutation ##############################
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

for na in range(0,64):
	ausgabe_IP[na] = klartext[IP[na]-1]
	print(ausgabe_IP[na],end="")
print("")
#################### Aufspalten der Permutationsausgabe #######################
for nb in range(0,32):
	halfte1[nb] = ausgabe_IP[nb]
	print(halfte1[nb],end="")
print("")

for nc in range(0,32):
	halfte2[nc] = ausgabe_IP[nc+32]
	print(halfte2[nc],end="")
print("")
###############################################################################
