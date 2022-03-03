# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:02:00 2020

@author: Rogelio Torres
"""
#Proyecto final

import pandas as pd
import numpy as np
import matplotlib as mp

file=('t1.csv')
xCausa= pd.read_csv(file)
xCausa.head(5)
xCausa.head()

file2=('t2.csv')
xPais= pd.read_csv(file2)
xPais.head(5)

xPais[['Year', 'Both sexes', 'Male', 'Female','Both sexesT', 'MaleT', 'FemaleT']].head(5)

#total de muertes por año 
muertesXAho=xPais.groupby('Year').agg({'Both sexesT': np.sum})
muertesXAho.plot(kind='barh')
mp.pyplot.xlabel('total deaths in thousands')
mp.pyplot.ylabel('year')
mp.pyplot.title('Total deaths per year')


#promedio de muertos por pais por equis enfermedad
promMuertosXEnfermedad=xCausa.groupby('Causes').agg({'Both sexes': np.mean})
promMuertosXEnfermedad.plot(kind='barh')
mp.pyplot.xlabel('avg deaths per country')
mp.pyplot.ylabel('disease')
mp.pyplot.title('Average deaths per country by disease')


# top 10 paises con mayor prom de muertos x año/Países con tasa de mortalidad más alta (top10)
promMuertesXPais=xPais.groupby('Country').agg({'Both sexesT': np.mean})
promMuertesXPais.nlargest(10, columns='Both sexesT').head(10).plot(kind='bar')
mp.pyplot.ylabel('avg deaths (in thousands) per year')
mp.pyplot.xlabel('top countries')
mp.pyplot.title('Top 10 countries with biggest average mortality rate')


#top 10 paises con menor prom de muertos x año/País con tasa de mortalidad más baja (top 10)
promMuertesXPais=xPais.groupby('Country').agg({'Both sexesT': np.mean})
promMuertesXPais.nsmallest(10, columns='Both sexesT').tail(10).plot(kind='bar')
mp.pyplot.ylabel('avg deaths (in thousands) per year')
mp.pyplot.xlabel('top countries')
mp.pyplot.title('Top 10 countries with smallest average mortality rate')


#top 5 paises y años con mayores tasas de mortalidad registradas
x=xPais.groupby(['Year', 'Country']).agg({'Both sexes': np.mean})
x.nlargest(5, columns='Both sexes').tail(5)

#top 5 paises y años con menores tasas de mortalidad registradas
x=xPais.groupby(['Year', 'Country']).agg({'Both sexes': np.mean})
x.nsmallest(5, columns='Both sexes').tail(5)


#Lista de los paises que vamos a analizar de latinoamerica
latin = ['Mexico','Peru','Honduras','Ecuador','Belize']

# mortalidad promedio de cada pais
promMortalidadLatin = xPais[xPais['Country'].isin(latin)].groupby('Country').agg({'Both sexes': np.mean})
promMortalidadLatin.plot(kind = 'bar')
mp.pyplot.title('Average mortality rate')

# proporcion de muertes promedio por enfermedad
enfermedades = ['Cardiovascular diseases','Chronic obstructive pulmonary disease','Diabetes mellitus','Malignant neoplasms ']
for i in latin:
    
    enfermedadMexico = xCausa[xCausa['Country']==i].groupby('Causes').agg({'Both sexes': np.mean})
    fig1 = mp.pyplot.subplot()
    fig1.pie(enfermedadMexico, labels = enfermedades, autopct = '%2.1f%%')
    fig1.set_title('Ratio of deaths by disease in '+i)
    mp.pyplot.show()

#muertes promedio de hombres y  mujeres por pais/Muertes Promedio para hombres y mujeres
promMuertesGenero = xPais[xPais['Country'].isin(latin)].groupby('Country').agg({'MaleT': np.mean,'FemaleT': np.mean})
promMuertesGenero.plot(kind = 'bar')
mp.pyplot.ylabel('Avg deaths (in thousands) per year')
mp.pyplot.xlabel('Countries')
mp.pyplot.title('Avergae deaths (in thousands) per year by gender')

#País con menores muertes promedio
menosMuer=xPais[xPais["Country"].isin(latin)].groupby("Country").agg({"Both sexes":np.mean})
print(menosMuer.loc[menosMuer["Both sexes"] == menosMuer.values.min()])

#Muertes promedio por año por pais

for pais in latin:
    muerAho=xPais[xPais["Country"]==pais].groupby("Year").agg({"Both sexes":np.mean})
    muerAho.plot(kind="bar")
    mp.pyplot.ylabel('Deaths (per 100,000 population)')
    mp.pyplot.xlabel('Year')
    mp.pyplot.title('Deaths per year (per 100 population) ' +pais)

#Gráfica de muertes netas por enfermedad de un país
for pais in latin:
    muerEnf=xCausa[xCausa["Country"]==pais].groupby("Causes").agg({"Both sexes":np.mean})
    muerEnf.plot(kind="bar")
    mp.pyplot.ylabel('Deaths (per 100,000 population) ')
    mp.pyplot.xlabel('Enfermedad')
    mp.pyplot.title('Accumulated deaths (per 100,000 population) by sickness in ' +pais)

#País con mayores muertes promedio
masMuer=xPais[xPais["Country"].isin(latin)].groupby("Country").agg({"Both sexes":np.mean})
print(masMuer.loc[menosMuer["Both sexes"] == menosMuer.values.max()])

#  mas muertes por una sola enfermedad año por cada país latinoamerica

for pais in latin:
    enfMasMortalPorAnoPorPais=xCausa[xCausa["Country"]==pais].groupby("Year").agg("Both sexes")
    print(pais,enfMasMortalPorAnoPorPais.max())
    
# menos muertes por una sola enfermedad por año por país latinoamerica
    
for pais in latin:
   enfMasMortalPorAnoPorPais=xCausa[xCausa["Country"]==pais].groupby("Causes").agg({"Both sexes": sum})
   print(pais,enfMasMortalPorAnoPorPais.loc[enfMasMortalPorAnoPorPais["Both sexes"]==enfMasMortalPorAnoPorPais.values.max()],enfMasMortalPorAnoPorPais.max())   

    
    
    