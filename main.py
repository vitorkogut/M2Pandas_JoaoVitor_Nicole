from optparse import Values
from xml.dom.expatbuilder import parseString
import matplotlib.pyplot as plt
import pandas as pd

PATH = "Spotify 2010 - 2019 Top 100.csv" #Path do CSV



file = pd.read_csv(PATH) #Leitura do file CSV
df = pd.DataFrame(file) #Criação do dataframe
resultados = pd.DataFrame()


print("\n\n---------------------------------------------TOP 100 MÚSICAS POR ANO 2010-2019 ---------------------------------------------\n\n")

# filtro por coluna
print("Filtrar por genero? (s/n): ")
f_genero = input()
if(f_genero == 's'):
    generos = df['top genre'].tolist()
    unique_generos = []

    for this_genero in generos:
        if this_genero not in unique_generos:
            unique_generos.append(this_genero)
    unique_generos.pop(len(unique_generos) - 1) # remover ultimo item que é NaN

    for i in range(len(unique_generos)):
        print("[{}] - {}".format(i,unique_generos[i]))

    print("\nInsira o ID do genero desejado: ")
    id_genero = int(input()) 

    value = unique_generos[id_genero]

    coluna_filtrada = file[file['top genre'] == value]
    df = coluna_filtrada
    print("Quantidade atual de resultados apos o filtro: " + str( len(df) )) #Concatena para filtrar a coluna

    if(len(df) == 0):
        print("NENHUM RESULTADO ENCONTRADO")
        exit()

# filtro por parte do titulo
print("\nFiltrar por titulo? (s/n)")
f_titulo = input()
if(f_titulo == 's'):
    print("Insira o titulo (ou parte dele): ")
    titulo_search = str(input())
    musicas_filtradas = df[ df['title'].str.contains(titulo_search, na=False) ]
    df = musicas_filtradas
    print("Quantidade atual de resultados apos o filtro: " + str(len(df))) 

    if(len(df) == 0):
        print("NENHUM RESULTADO ENCONTRADO")
        exit()

# filtro por parte do ano
print("\nFiltrar por ano? (s/n)")
f_ano = input()
if(f_ano == 's'):
    print("Insira o ano (xxxx): ")
    ano_search = int(input())
    musicas_filtradas = df[ df['top year'] == ano_search]
    df = musicas_filtradas
    print("Quantidade atual de resultados apos o filtro: " + str(len(df)))
    
    if(len(df) == 0):
        print("NENHUM RESULTADO ENCONTRADO")
        exit()


#Agrupa por BPM
print("\nAgrupar por BPM? (s/n):")
g_bpm = input()
if(g_bpm == 's'):
    options = df.groupby('bpm')
    print("BPM: ")
    bpm_grupo = int(input())
    df = options.get_group(bpm_grupo)

    if(len(df) == 0):
        print("NENHUM RESULTADO ENCONTRADO")
        exit()

#Agrupa por artista
print("\nAgrupar por tipo de artista? (s/n):")
g_grupo = input()
if(g_grupo == 's'):
    options = df.groupby('artist type')
    print("tipo de artista (Solo,Duo,Band/Group): ")
    grupo_grupo = input()
    df = options.get_group(grupo_grupo)

    if(len(df) == 0):
        print("NENHUM RESULTADO ENCONTRADO")
        exit()

###### IMPRESSÃO DE GRÁFICOS
print("\nImprimir graficos BPM? (s/n):")
o_grap = input()
if(o_grap == 's'):
   graph = df.groupby('top year')
   graph = graph['bpm']
   graph.plot()
   plt.legend(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
   plt.ylabel('BPM')
   plt.xlabel('musicas')
   plt.show()

print("\nImprimir graficos db? (s/n):")
o_grap = input()
if(o_grap == 's'):
   graph = df.groupby('top year')
   graph = graph['dB']
   graph.plot()
   plt.legend(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
   plt.ylabel('db')
   plt.xlabel('musicas')
   plt.show()

print("\nImprimir graficos duração? (s/n):")
o_grap = input()
if(o_grap == 's'):
   graph = df.groupby('top year')
   graph = graph['dur']
   graph.plot()
   plt.legend(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
   plt.ylabel('duração')
   plt.xlabel('musicas')
   plt.show()


###### SALVA OU IMPRIME
print("\n\n[1]Salvar resultados CSV | [2]Imprimir resultados | [3]Imprimir resultados e salvar CSV")
opc_final = int(input())

if(opc_final == 1):
    print("Salvando...")
    pd.DataFrame.to_csv(df,"saida.csv")
elif(opc_final == 2):
    print(df)
elif(opc_final == 3):
    print(df)
    pd.DataFrame.to_csv(df,"saida.csv")