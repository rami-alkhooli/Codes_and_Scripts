import sys, numpy, array
############################## Initialisierung ################################
klartext = ''
schlussel = ''
sbox1 = [0] * 6
sbox2 = [0] * 6
sbox3 = [0] * 6
sbox4 = [0] * 6
sbox5 = [0] * 6
sbox6 = [0] * 6
sbox7 = [0] * 6
sbox8 = [0] * 6
sbox_P = [0] * 32
halfteL1 = [0] * 32
halfteR1 = [0] * 32
expX1 = [0] * 48
xorX1 = [0] * 48
ausgabe_IP = [0] * 64
############################## Gegebene Werte #################################
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
IP_1 = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
IP_f = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

sbox1Tabelle = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8], [4,1,14,9,13,6,2,11,15,12,9,7,3,10,5,0], [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
sbox2Tabelle = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
sbox3Tabelle = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8], [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1], [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
sbox4Tabelle = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15], [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9], [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4], [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
sbox5Tabelle = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
sbox6Tabelle = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8], [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
sbox7Tabelle = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6], [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
sbox8Tabelle = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2], [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8], [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
################################ Funktionen ###################################
def schrumpfeArray(array, tabelle):
	saule = int(str(array[1])+str(array[2])+str(array[3])+str(array[4]),2)
	zeile = int(str(array[0])+str(array[5]),2)
	return str(bin(tabelle[zeile][saule])[2:]).rjust(4,'0')
################################ Überprüfung ##################################
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
sbox1[0:6] = xorX1[0:6]
sbox2[0:6] = xorX1[6:12]
sbox3[0:6] = xorX1[12:18]
sbox4[0:6] = xorX1[18:24]
sbox5[0:6] = xorX1[24:30]
sbox6[0:6] = xorX1[30:36]
sbox7[0:6] = xorX1[36:42]
sbox8[0:6] = xorX1[42:48]
print('\nS-Boxes vor dem Schrumpfen:')
print(str(xorX1[0:6]) +'\n'+ str(xorX1[6:12]) +'\n'+ str(xorX1[12:18]) +'\n'+ str(xorX1[18:24]) +'\n'+ str(xorX1[24:30]) +'\n'+ str(xorX1[30:36]) +'\n'+ str(xorX1[36:42]) +'\n'+ str(xorX1[42:48]))
################################ Schrumpfen ###################################
print('S-Boxes nach dem Schrumpfen:')
print('[' + schrumpfeArray(sbox1,sbox1Tabelle) + ']' )
print('[' + schrumpfeArray(sbox2,sbox2Tabelle) + ']' )
print('[' + schrumpfeArray(sbox3,sbox3Tabelle) + ']' )
print('[' + schrumpfeArray(sbox4,sbox4Tabelle) + ']' )
print('[' + schrumpfeArray(sbox5,sbox5Tabelle) + ']' )
print('[' + schrumpfeArray(sbox6,sbox6Tabelle) + ']' )
print('[' + schrumpfeArray(sbox7,sbox7Tabelle) + ']' )
print('[' + schrumpfeArray(sbox8,sbox8Tabelle) + ']' )

zusammengesetzt = schrumpfeArray(sbox1,sbox1Tabelle) + schrumpfeArray(sbox2,sbox2Tabelle) + schrumpfeArray(sbox3,sbox3Tabelle) + schrumpfeArray(sbox4,sbox4Tabelle) + schrumpfeArray(sbox5,sbox5Tabelle) + schrumpfeArray(sbox6,sbox6Tabelle) + schrumpfeArray(sbox7,sbox7Tabelle) + schrumpfeArray(sbox8,sbox8Tabelle)
print('S-Boxes nach dem Schrumpfen zusammengesetzt:\n' + zusammengesetzt)
############################### Permutation ###################################
print('Nach f-Permutation:')
for nf in range(0,32):
	sbox_P[nf] = zusammengesetzt[IP_f[nf]-1]
	print(sbox_P[nf],end="")
print("")
############################# Zusammensetzen ##################################
rechts = ''
print('\nDie rechte Hälfte der verschlüsselten Nachricht in Runde 1 ist:')
for nf in range(0,32):
	print(sbox_P[nf],end="")
	rechts += str(sbox_P[nf])

print('\nDie linke Hälfte der verschlüsselten Nachricht in Runde 1 ist:')
links = ''
for ng in range(0,32):
	print(halfteR1[ng],end="")
	links += str(halfteR1[ng])

print('\nDie verschlüsselte Nachricht in Runde 1 ist:')
all = rechts + links
print(all)
print('-----------------------------------------------------------------------')