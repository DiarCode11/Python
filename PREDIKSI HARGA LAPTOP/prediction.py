import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder


# Gunakan File .csv
data = pd.read_csv('dataset/Laptop_price.csv')

# Label Encoder
encoder = LabelEncoder()
data['Brand'] = encoder.fit_transform(data['Brand'])
print(data['Brand'])

# Pisahkan Fitur dan Target
X = data.drop('Price', axis=1)
y = data['Price']

# Membagi data menjadi 80% untuk training dan 20% untuk testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model
model = LinearRegression()

# Melatih model dengan data train
model.fit(X_train, y_train)

# Definisikan nama folder
folder_path = "models/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Simpan model ke dalam folder
joblib.dump(model, os.path.join(folder_path, 'linear_regression_model.pkl'))

# # Membuat prediksi menggunakan data test
# y_pred = model.predict(X_test)

# # Menampilkan koefisien dan intersep dari model
# print("Koefisien:", model.coef_)
# print("Intersep:", model.intercept_)

# # Print MAE dan MSE
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print('MAE : ', mae)
# print('MSE : ', mse)
# print('R2 Score : ', r2)


# # Visualisasi dengan plot
# plt.figure(figsize=(8, 6))
# # Plot nilai aktual (y_test) dengan warna merah
# plt.scatter(np.arange(len(y_test)), y_test, color='red', label='Nilai Aktual')
# # Plot nilai prediksi (y_pred) dengan warna biru
# plt.scatter(np.arange(len(y_test)), y_pred, color='blue', label='Nilai Prediksi')

# plt.xlabel('Index Data')
# plt.ylabel('Nilai')
# plt.title('Perbandingan Nilai Aktual dan Nilai Prediksi')
# plt.legend()
# plt.show()

