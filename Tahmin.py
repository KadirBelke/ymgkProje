# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Veri setinin yüklenmesi
veri = pd.read_csv('result.csv')

#Verinin Sinif sayisinin ve etiklerinin belirlenmesi
label_encoder = LabelEncoder().fit(veri['HKIsonuc'])
labels = label_encoder.transform(veri['HKIsonuc'])
classes = list(label_encoder.classes_)

#Girdi ve çikti verilerinin hazirlanmasi
nb_features = 6
nb_classes = len(classes)
X = veri.drop(['HKIsonuc'], axis=1)
y = labels

#Verilerin standartlasmasi
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#Egitim ve test verilerinin hazirlamanmasi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.1)

# çikti degerlerinin kategorilestirmesi
from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#YSA model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(16,input_dim=6, activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(4,activation="softmax"))
model.summary()

#modelin derlenmesi
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics= ["accuracy"])

#modelin egitilmesi
model.fit(X_train,y_train,validation_data=(X_test,y_test), epochs=500)
#Gerekli bilgilerin verilmesi
print(("Ortalama egitim kaybi: ", np.mean(model.history.history["loss"])))
print(("Ortalama Egitim Basarimi: ", np.mean(model.history.history["accuracy"])))
print(("Ortalama Dogrulama kaybi: ", np.mean(model.history.history["val_loss"])))
print(("Ortalama Dogrulama Basarimi: ", np.mean(model.history.history["val_accuracy"])))


import matplotlib.pyplot as plt
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok sayısı")
plt.legend(["Eğitim","Doğrulama"], loc="upper left")
plt.show()
