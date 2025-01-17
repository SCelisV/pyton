#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

IN-WORK-OUT
Created on Wed Aug 19 15:28:50 2020

@author: scelis


# ================================================================
# Que pasaría si intentamos utilizar múltiples variables independientes en el mismo módelo.
"""
# ====================
#  Regresión Polinomial
# ====================
"""
# Regresión con una variable

# DataFrame - [506 rows x 1 columns]
X = df.loc[df.index[0:506], ['LSTAT']]
print(X)

y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
X = boston_dataSet.data[df.index[0:506],[12]].reshape(-1,1)
# Variable de respuesta Array of float - [[24.][21.6] ... [22.][ 11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array


# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión polinomial

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Creando la transformación polinomial
poly = PolynomialFeatures(degree=3) # degree -> grado de la regresión polinomial(transforma de valor númerico a polinomio)

# Python hace una tranformación de los datos originales a un polinomio
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.fit_transform(X_test)

# Creando el módelo de regresión polinomial con una regresión líneal, lmp
lmp = LinearRegression().fit(X_train_poly, y_train)

# lmp.score(X,y) npi

# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.5419571999998836, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmp.coef_

lmp.intercept_

y_train_pred = lmp.predict(X_train_poly) # Predice usando el módelo líneal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmp.predict(X_test_poly) # Predice usando el módelo líneal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.682052397497773
# Prueba 0.6150559372890204

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 36.80278822808814


# Graficamos 
import matplotlib.pyplot as plt
import numpy as np

# Le decimos a python que grafique en el mismo fichero
# Mute inline plotting

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot guardamos valores distribuidos entre 0 y 40
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,40).reshape(-1, 1) # ordenados por columna
# print(X_plot)

# X_plot = np.linspace(0,40).reshape(1, -1) # ordenados por fila
# print(X_plot)

# Con el módelo predecimos X_plot
X_plot_poly = poly.fit_transform(X_plot)
y_plot = lmp.predict(X_plot_poly)

# Graficamos el módelo
plt.plot(X_plot, y_plot,"r--")

# ====================
# Graficando y Creando la transformación polinomial grado 2
poly = PolynomialFeatures(degree=2) # degree -> grado de la regresión polinomial(transforma de valor númerico a polinomio)
# Python hace una tranformación de los datos originales a un polinomio
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.fit_transform(X_test)

# Creando el módelo de regresión polinomial con una regresión líneal, lmp
lmp2 = LinearRegression().fit(X_train_poly, y_train)

# lmp2.score(X,y) npi

# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.5419571999998836, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmp2.coef_

lmp2.intercept_

y_train_pred = lmp2.predict(X_train_poly) # Predice usando el módelo líneal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmp2.predict(X_test_poly) # Predice usando el módelo líneal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.6607355856920534
# Prueba 0.6057480327377572

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 37.69267554739093

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot guardamos valores distribuidos entre 0 y 40
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,40).reshape(-1, 1) # ordenados por columna
# print(X_plot)

# X_plot = np.linspace(0,40).reshape(1, -1) # ordenados por fila
# print(X_plot)

# Con el módelo predecimos X_plot
X_plot_poly = poly.fit_transform(X_plot)
y_plot = lmp2.predict(X_plot_poly)

# Graficamos el módelo - nos genera una curva diferente like una parabola
plt.plot(X_plot, y_plot,"r--")

"""
# ====================
# SVM - SVR - Machine Support Vector Regression
# ====================
"""
# Regresión con una variable

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
X = boston_dataSet.data[df.index[0:506],[12]].reshape(-1,1) # líneas indefinido y una columna
# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)  # líneas indefinido y una columna

# Normalización de datos - Escalamiento de los datos - reduce el rango de las bandas de la máquina vectorial, es decir, si tenemos datos que van de 0-100 por ejemplo, entonces escalará estos a un rango de 0-1
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

# Python hace una tranformación de los datos originales
X = X_scaler.fit_transform(X)
y = y_scaler.fit_transform(y)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array

from sklearn.svm import SVR

#     https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR
#     https://scikit-learn.org/stable/modules/svm.html#tips-on-practical-use

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo SVR - Support Vector Regression
# using linear, polynomial and RBF(default) kernels.

# Fit regression model
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_lin = SVR(kernel='linear', C=100, gamma='auto')
svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
               coef0=1)


# Creando el módelo de soporte vectorial con rbf kernel, svm_rbf

# Creando el modelo y entrenando
svm_rbf = svr_rbf.fit(X_train,y_train.reshape(-1))
# Prediciendo valores de entrenamiento
y_train_pred = svm_rbf.predict(X_train) # Predice usando el módelo de soporte vectorial con rbf kernel y los datos de entrenamiento
# Prediciendo valores de validación
y_test_pred = svm_rbf.predict(X_test) # Predice usando el módelo de soporte vectorial con rbf kernel y los datos de prueba


# =============================================================================
# type(y_train_pred)
# print(y_train_pred[:5])
# print(y_test_pred[:5])
# =============================================================================


# Graficando
import matplotlib.pyplot as plt
import numpy as np
# Le decimos a jupyter que grafique en  el cuaderno
# %matplotlib inline en Spyder python mute inline plotting of plot menu
# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot generamos 50 valores distribuidos entre 0 y 1 en una columna
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,1).reshape(-1, 1) # ordenados por columna
# print(X_plot)

# Con el modelo predecimos X_plot
y_plot = svm_rbf.predict(X_plot)
# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--")

from sklearn.metrics import r2_score
# Calculamos el error
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.6549670658597863
# Prueba 0.5959466433326346


# Creando el módelo de soporte vectorial con lin kernel, svm_lin

# Creando el modelo y entrenando
svm_lin = svr_lin.fit(X_train,y_train.reshape(-1))
# Prediciendo valores de entrenamiento
y_train_pred = svm_lin.predict(X_train) # Predice usando el módelo de soporte vectorial con lin kernel y los datos de entrenamiento
# Prediciendo valores de validación
y_test_pred = svm_lin.predict(X_test) # Predice usando el módelo de soporte vectorial con lin kernel y los datos de prueba


# =============================================================================
# type(y_train_pred)
# print(y_train_pred[:5])
# print(y_test_pred[:5])
# =============================================================================


# Graficando
import matplotlib.pyplot as plt
import numpy as np
# Le decimos a jupyter que grafique en  el cuaderno
# %matplotlib inline en Spyder python mute inline plotting of plot menu
# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot generamos 50 valores distribuidos entre 0 y 1 en una columna
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,1).reshape(-1, 1) # ordenados por columna
# print(X_plot)

# Con el modelo predecimos X_plot
y_plot = svm_lin.predict(X_plot)
# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--")

from sklearn.metrics import r2_score
# Calculamos el error
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5427835029461732
# Prueba 0.5153691412881033

# Creando el módelo de soporte vectorial con poly kernel, svm_poly

# Creando el modelo y entrenando
svm_poly = svr_poly.fit(X_train,y_train.reshape(-1))
# Prediciendo valores de entrenamiento
y_train_pred = svr_poly.predict(X_train) # Predice usando el módelo de soporte vectorial con lin kernel y los datos de entrenamiento
# Prediciendo valores de validación
y_test_pred = svr_poly.predict(X_test) # Predice usando el módelo de soporte vectorial con lin kernel y los datos de prueba


# =============================================================================
# type(y_train_pred)
# print(y_train_pred[:5])
# print(y_test_pred[:5])
# =============================================================================


# Graficando
import matplotlib.pyplot as plt
import numpy as np
# Le decimos a jupyter que grafique en  el cuaderno
# %matplotlib inline en Spyder python mute inline plotting of plot menu
# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot generamos 50 valores distribuidos entre 0 y 1 en una columna
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,1).reshape(-1, 1) # ordenados por columna
# print(X_plot)

# Con el modelo predecimos X_plot
y_plot = svr_poly.predict(X_plot)
# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--")

from sklearn.metrics import r2_score
# Calculamos el error
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.6807594509701385
# Prueba 0.6128901480469988

# Graficando los tres modelos de soporte vectorial con rbf, lin y poly kernel, 

import matplotlib.pyplot as plt
import numpy as np

# Le decimos a jupyter que grafique en  el cuaderno
# %matplotlib inline en Spyder python mute inline plotting of plot menu

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue", label="Training",alpha=0.3)

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange", label="test",alpha=0.3)

# En X_plot generamos 50 valores distribuidos entre 0 y 1 en una columna
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,1).reshape(-1, 1) # ordenados por columna
# print(X_plot)

for name, svr, s in zip(["RBF","Linear","Poly"],[svr_rbf,svr_lin,svr_poly],["r--","g--","b--"]):
    svr.fit(X_train,y_train.reshape(-1))
    y_train_pred = svr.predict(X_train)
    y_test_pred = svr.predict(X_test)    
    # Con el modelo predecimos X_plot
    y_plot = svr.predict(X_plot)
    # Graficamos el modelo
    plt.plot(X_plot, y_plot, s,label=name)
    # Calculamos el error
    print(name, "Entrenamiento", r2_score(y_train, y_train_pred))
    print(name, "Prueba", r2_score(y_test, y_test_pred))

plt.legend()

# svm_rbf
# Entrenamiento 0.6549670658597863
# Prueba 0.5959466433326346

# svm_lin
# Entrenamiento 0.5427835029461732
# Prueba 0.5153691412881033

# svm_poly
# Entrenamiento 0.6807594509701385
# Prueba 0.6128901480469988

# ====================

# Using seaborn - esteticamente
plt.style.use("seaborn")
plt.figure(figsize=(6,6))


svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_lin = SVR(kernel='linear', C=100, gamma='auto')
svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1, coef0=1)

# Deshacemos la transformación que Python hace de los datos originales

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_scaler.inverse_transform(X_train), y_scaler.inverse_transform(y_train.reshape(-1,1)),label="Training",alpha=0.5)
# Creamos un scatter plot con los datos de validación
plt.scatter(X_scaler.inverse_transform(X_test), y_scaler.inverse_transform(y_test.reshape(-1,1)),label="Testing",alpha=0.5)
# En X_plot guardamos valores distribuidos entre 0 y 1
X_plot = np.linspace(0,1).reshape(-1, 1)
    
for name, svr, s in zip(["RBF","Linear","Poly"],[svr_rbf,svr_lin,svr_poly],["r--","g--","b--"]):
    svr.fit(X_train,y_train.reshape(-1))
    y_train_pred = svr.predict(X_train)
    y_test_pred = svr.predict(X_test)    
    # Con el modelo predecimos X_plot
    y_plot = svr.predict(X_plot)
    # Graficamos el modelo
    plt.plot(X_scaler.inverse_transform(X_plot), y_scaler.inverse_transform(y_plot.reshape(-1,1)), s,label=name)
    # Calculamos el error
    print(name, "Entrenamiento", r2_score(y_train, y_train_pred))
    print(name, "Prueba", r2_score(y_test, y_test_pred))
    print("----")

plt.legend();
# ====================

"""

# ====================
# Árboles de decisión - CART
# ====================
"""
# Regresión con una variable

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
X = boston_dataSet.data[df.index[0:506],[12]].reshape(-1,1) # líneas indefinido y una columna
# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)  # líneas indefinido y una columna

# Normalización de datos - Escalamiento de los datos - reduce el rango de las bandas de la máquina vectorial, es decir, si tenemos datos que van de 0-100 por ejemplo, entonces escalará estos a un rango de 0-1
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

# Python hace una tranformación de los datos originales
X = X_scaler.fit_transform(X)
y = y_scaler.fit_transform(y)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array

from sklearn.tree import DecisionTreeRegressor #(Árbol de decision de regresión)
tree_2 = DecisionTreeRegressor(max_depth=2) # profundidad máxima del árbol de regresión

# Creando el módelo del árbol de decisión , treerm_2

# Creando el modelo y entrenando
treerm_2 = tree_2.fit(X_train,y_train.reshape(-1))
# Prediciendo valores de entrenamiento
y_train_pred = treerm_2.predict(X_train) # Predice usando el módelo del árbol de decisión de Regresión y los datos de entrenamiento
# Prediciendo valores de validación
y_test_pred = treerm_2.predict(X_test) # Predice usando el módelo del árbol de decisión de Regresión y los datos de prueba

# Gráficamos
import matplotlib.pyplot as plt
import numpy as np
# Le decimos a jupyter que grafique en  el cuaderno
# %matplotlib inline
# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train,alpha=0.5)
# Creamos un scatter plot con los datos de validación
plt.scatter(X_test, y_test,alpha=0.5)
# En X_plot guardamos valores distribuidos entre 0 y 40
X_plot = np.linspace(0,1,1000).reshape(-1, 1)
# Con el modelo predecimos X_plot
y_plot = treerm_2.predict(X_plot)
# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--");

from sklearn.metrics import r2_score
# Calculamos el error
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.686183783521107
# Prueba 0.5894049706991193

