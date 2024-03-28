import joblib
import pandas as pd

# Muat kembali model dari file
model = joblib.load('models/linear_regression_model.pkl')

new_data = pd.DataFrame({
            'Brand': [1],
            'Processor_Speed': [2.268096586],
            'RAM_Size': [3],
            'Storage_Capacity': [32],
            'Screen_Size': [11.3113718],
            'Weight': [3.857612952]
})


prediction = model.predict(new_data)
real_price = prediction 
print('Prediksi Harga (dalam juta): ',real_price)