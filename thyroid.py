import pickle
import streamlit as st


thyroid_model = pickle.load(open('thyroidmodel.sav', 'rb'))

#judul web
st.title('Data Mining')

age = st.number_input('Masukkan Umur Anda : ', 0,1000)
sex = st.radio('Pilih Gender',['Male','Female'])
onthyroxine = st.radio('On thyroxine',['f','t'])
queryonthyroxine = st.radio('Query on thyroxine',['f','t'])
onantithyroidmedication = st.radio('On antithyroid medication',['f','t'])
sick = st.radio('Sick',['f','t'])
pregnant = st.radio('Pregnant',['f','t'])
thyroidsurgery = st.radio('Thyroid surgery',['f','t'])
I131treatment = st.radio('I131 treatment',['f','t'])
queryhypothyroid = st.radio('Query hypothyroid',['f','t'])
queryhyperthyroid = st.radio('Query hyperthyroid',['f','t'])
lithium = st.radio('Lithium',['f','t'])
goitre = st.radio('Goitre',['f','t'])
tumor = st.radio('Tumor',['f','t'])
hypopituitary = st.radio('Hypopituitary',['f','t'])
psych = st.radio('Psych',['f','t'])
TSHMeasured = st.radio('TSH measured',['f','t'])
TSH = st.number_input('TSH : ', -1,1000)
T3Measured = st.radio('T3 measured',['f','t'])    
T3 = st.number_input('T3 : ', -1,1000)
TT4Measured = st.radio('TT4 measured',['f','t'])
TT4 = st.number_input('TT4 : ', -1,1000)
T4UMeasured = st.radio('T4U measured',['f','t'])
T4U = st.number_input('T4U : ', -1,1000)
FTIMeasured = st.radio('FTI measured',['f','t'])
FTI = st.number_input('FTI : ', -1,1000)
TBGMeasured = st.radio('TBG measured',['f'])
referralsource = st.multiselect('Referral source',['SVHC', 'SVI', 'STMW', 'SVHD', 'Other'])

diagnosis = ''

if st.button('Prediksi'):
    prediction = thyroidmodel.predict([[age, sex, onthyroxine, queryonthyroxine, onantithyroidmedication, sick, pregnant, thyroidsurgery , I131treatment, queryhypothyroid, queryhyperthyroid, lithium, goitre, tumor, hypopituitary, psych, TSHMeasured, TSH, T3Measured, T3, TT4Measured, TT4, T4UMeasured, T4U, FTIMeasured, FTI, TBGMeasured, referralsource]])

    if ([no_index] == 0):
        print('Pasien Negative Thyroid')
    else :
        print('Pasien Positive terkena Thyroid')
st.success(diab_diagnosis)
