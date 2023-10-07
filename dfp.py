# %%
import pandas as pd
import wget
from zipfile import ZipFile
#import datatable as dt
#from itables import init_notebook_mode
#init_notebook_mode(all_interactive=True)
import yfinance as yf
import plotly.graph_objects as go
import os
from os import listdir , makedirs
from os import remove
from os.path import isfile, join, splitext

# %%
url_base = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/"

print("\nCreating folders")
path = "CVM"
path2 = "dfp"
down_path = 'Consolidado'

if not os.path.exists(path):
    os.makedirs(path)
    print(f"Created folder '{path}'.")
else:
    print(f"Folder '{path}' already exists.")


if not os.path.exists(path2):
    os.makedirs(path2)
    print(f"Created folder '{path2}'.")
else:
    print(f"Folder '{path2}' already exists.")

if not os.path.exists(down_path):
    os.makedirs(down_path)
    print(f"Created folder '{down_path}'.")
else:
    print(f"Folder '{down_path}' already exists.")



def delete_all_files_in_folder(folder):
    for f in listdir(folder):
        if isfile(join(folder, f)):
            remove(join(folder, f))

print("\nErasing files in folder")
delete_all_files_in_folder(path)
delete_all_files_in_folder(path2)
delete_all_files_in_folder(down_path)

# %%
#Criar lista de arquivos com os nomes

arq_zip = []

for ano in range(2018,2023):
    arq_zip.append(f"dfp_cia_aberta_{ano}.zip")
    
#arq_zip

# %%
#Download dos arquivos
for arq in arq_zip:
    wget.download(url_base+arq,out=path2)

# %%
#Extraindo os arquivos

for arq in arq_zip:
    ZipFile(path2+'/'+arq,"r").extractall(path2)

# %%
dre = pd.DataFrame()
for ano in range(2018,2023):
    dre = pd.concat([dre,pd.read_csv(path2+"/dfp_cia_aberta_DRE_con_{}.csv".format(ano),sep=";",decimal=",",encoding="ISO-8859-1")])
dre = dre[dre["ORDEM_EXERC"] == "ÚLTIMO"]
dre.to_csv(down_path + "/dfp_cia_aberta_DRE_con_2018-2022.csv",index=False)

bpa = pd.DataFrame()
for ano in range(2018,2023):
    bpa = pd.concat([bpa,pd.read_csv(path2+"/dfp_cia_aberta_BPA_con_{}.csv".format(ano),sep=";",decimal=",",encoding="ISO-8859-1")])
bpa = bpa[bpa["ORDEM_EXERC"] == "ÚLTIMO"]
bpa.to_csv(down_path + "/dfp_cia_aberta_BPA_con_2018-2022.csv",index=False)

bpp = pd.DataFrame()
for ano in range(2018,2023):
    bpp = pd.concat([bpp,pd.read_csv(path2+"/dfp_cia_aberta_BPA_con_{}.csv".format(ano),sep=";",decimal=",",encoding="ISO-8859-1")])
bpp = bpp[bpp["ORDEM_EXERC"] == "ÚLTIMO"]
bpp.to_csv(down_path + "/dfp_cia_aberta_BPP_con_2018-2022.csv",index=False)

dfc = pd.DataFrame()
for ano in range(2018,2023):
    dfc = pd.concat([dfc,pd.read_csv(path2+"/dfp_cia_aberta_DFC_MI_con_{}.csv".format(ano),sep=";",decimal=",",encoding="ISO-8859-1")])
dfc = dfc[dfc["ORDEM_EXERC"] == "ÚLTIMO"]
dfc.to_csv(down_path + "/dfp_cia_aberta_DFC_MI_con_2018-2022.csv",index=False)

print("\nFiles were generated...")