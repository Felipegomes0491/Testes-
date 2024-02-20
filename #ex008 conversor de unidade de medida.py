#ex008pycharm
#conversor entre unidades de medidas.

medida = float(input('uma distância em metros: '))
km = medida /1000
hm = medida / 100
dam = medida /10
m = medida *1
dm = medida *10
cm = medida *100
mm = medida *1000

#:.2f serve para colocar 2 casas decimais nos números.

print('A medida de {:.2f} m corresponde a {}km, {}hm, {}dam, {}m, {}dm, {}cm e {}mm'. format(medida,km, hm, dam,m, dm, cm, mm))



