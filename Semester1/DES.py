import sys, numpy, array
############################# Initialisierung ################################
klartext = ''
schlussel = ''
ausgabe_IP = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
halfteL1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
halfteR1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
expX1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xorX1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sbox1 = [0,0,0,0,0,0]
sbox2 = [0,0,0,0,0,0]
sbox3 = [0,0,0,0,0,0]
sbox4 = [0,0,0,0,0,0]
sbox5 = [0,0,0,0,0,0]
sbox6 = [0,0,0,0,0,0]
sbox7 = [0,0,0,0,0,0]
sbox8 = [0,0,0,0,0,0]
sbox1Tabelle = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8], [4,1,14,9,13,6,2,11,15,12,9,7,3,10,5,0], [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
sbox2Tabelle = [[], [], [], []]
sbox3Tabelle = [[], [], [], []]
sbox4Tabelle = [[], [], [], []]
sbox5Tabelle = [[], [], [], []]
sbox6Tabelle = [[], [], [], []]
sbox7Tabelle = [[], [], [], []]
sbox8Tabelle = [[], [], [], []]
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
print('-----------------------------------------------------------------------')
print('Klartext:\n' + klartext)
############################ Eingangspermutation ##############################
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
print('Nach 1. Permutation:')
for na in range(0,64):
	ausgabe_IP[na] = klartext[IP[na]-1]
	print(ausgabe_IP[na],end="")
print("")
#################### Aufspalten der Permutationsausgabe #######################
print('Erste linke Hälfte:')
for nb in range(0,32):
	halfteL1[nb] = ausgabe_IP[nb]
	print(halfteL1[nb],end="")

print('\nErste rechte Hälfte:')
for nc in range(0,32):
	halfteR1[nc] = ausgabe_IP[nc+32]
	print(halfteR1[nc],end="")
################################# Expansion ###################################
E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
print('\nRechte Hälfte nach der Expansion:')
for nd in range(0,48):
	expX1[nd] = halfteR1[int(E[nd])-1]
	print(expX1[nd],end="")
################################### XOR #######################################
print('\nRechte Hälfte nach der XOR-Addition mit dem Schlüssel:')
for ne in range(0,48):
	xorX1[ne] = int(schlussel[ne]) ^ int(expX1[ne])
	print(xorX1[ne],end="")
################################# S-Boxes #####################################
sbox1[0:5] = xorX1[0:5]
sbox2[0:5] = xorX1[6:11]
sbox3[0:5] = xorX1[12:17]
sbox4[0:5] = xorX1[18:23]
sbox5[0:5] = xorX1[24:29]
sbox6[0:5] = xorX1[30:35]
sbox7[0:5] = xorX1[36:41]
sbox8[0:5] = xorX1[42:47]
print('\nS-Boxes vor dem Schrumpfen:')
print(str(xorX1[0:5]) +'\n'+ str(xorX1[6:11]) +'\n'+ str(xorX1[12:17]) +'\n'+ str(xorX1[18:23]) +'\n'+ str(xorX1[24:29]) +'\n'+ str(xorX1[30:35]) +'\n'+ str(xorX1[36:41]) +'\n'+ str(xorX1[42:47]))
################################ Schrumpfen ###################################
saule = int(str(sbox8[1])+str(sbox8[2])+str(sbox8[3])+str(sbox8[4]),2)
zeile = int(str(sbox8[0])+str(sbox8[5]),2)

print('\nS-Boxes nach dem Schrumpfen:')

print('\n-----------------------------------------------------------------------')