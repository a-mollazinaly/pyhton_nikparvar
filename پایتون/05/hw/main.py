kar_nameh = {}
i = 7
#-------------------------------------------------------------#
def karnameh (x,y):
    kar_nameh[x] = y
    vin = open ("result.txt", "+a")
    
    while i == 0:
        vin.write(kar_nameh[i] + "\n")
        i == i-1
    vin.close()
#-------------------------------------------------------------#


