import pickle
import streamlit as st


thyroid_model = pickle.load(open('thyroidmodel.sav', 'rb'))

#judul web
st.title('Data Mining')

age = st.text_input('Masukkan Umur Anda : ')
sex = st.text_input('Gender ? ["Male","Female"]')
onthyroxine = st.text_input('On thyroxine ? ["f","t"]')
queryonthyroxine = st.text_input('Query on thyroxine ? ["f","t"]')
onantithyroidmedication = st.text_input('On antithyroid medication ? ["f","t"]')
sick = st.text_input('Sick  ? ["f","t"]')
pregnant = st.text_input('Pregnant ? ["f","t"]')
thyroidsurgery = st.text_input('Thyroid surgery ? ["f","t"]')
I131treatment = st.text_input('I131 treatment ? ["f","t"]')
queryhypothyroid = st.text_input('Query hypothyroid ? ["f","t"]')
queryhyperthyroid = st.text_input('Query hyperthyroid ? ["f","t"]')
lithium = st.text_input('Lithium ? ["f","t"]')
goitre = st.text_input('Goitre ? ["f","t"]')
tumor = st.text_input('Tumor ? ["f","t"]')
hypopituitary = st.text_input('Hypopituitary ? ["f","t"]')
psych = st.text_input('Psych ? ["f","t"]')
TSHMeasured = st.text_input('TSH measured ? ["f","t"]')
TSH = st.text_input('TSH : ')
T3Measured = st.text_input('T3 measured ? ["f","t"]')    
T3 = st.text_input('T3 : ')
TT4Measured = st.text_input('TT4 measured ? ["f","t"]')
TT4 = st.text_input('TT4 : ')
T4UMeasured = st.text_input('T4U measured ? ["f","t"]')
T4U = st.text_input('T4U : ')
FTIMeasured = st.text_input('FTI measured ? ["f","t"]')
FTI = st.text_input('FTI : ')
TBGMeasured = st.text_input('TBG measured  ? ["f"]')
referralsource = st.text_input('Referral source ? ["SVHC", "SVI", "STMW", "SVHD", "Other"]')

diagnosis = ''

if st.button('Prediksi'):
    prediction = thyroid_model.predict([[age, sex, onthyroxine, queryonthyroxine, onantithyroidmedication, sick, pregnant, thyroidsurgery , I131treatment, queryhypothyroid, queryhyperthyroid, lithium, goitre, tumor, hypopituitary, psych, TSHMeasured, TSH, T3Measured, T3, TT4Measured, TT4, T4UMeasured, T4U, FTIMeasured, FTI, TBGMeasured, referralsource]])

    if (prediction[0] == 0):
        diagnosis = 'Pasien Negative Thyroid'
    else :
        diagnosis = 'Pasien Positive terkena Thyroid'
st.success(diagnosis)
