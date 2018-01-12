f=open("201705-citibike-tripdata.csv","r")
#f2=open("201705-citibike-tripdata_sample.csv","w")
f2=open("201705-citibike-tripdata_filtered.csv","w")

connjunto_inicio=set()
conjunto_final=set()
count=1
# for line in f:
# 	if(count<10001):
# 		print(count)
# 		f2.write(line)
# 	count+=1
encabezado=f.readline()
f2.write(encabezado)
for line in f:
	linea=line
	datos=line.strip().split(",")
	start_id=datos[3]
	end_id=datos[7]
	if(start_id not in connjunto_inicio or end_id not in conjunto_final):
		f2.write(linea)
	connjunto_inicio.add(start_id)
	conjunto_final.add(end_id)

	
print(conjunto_final)
print(connjunto_inicio)
f.close()
f2.close()