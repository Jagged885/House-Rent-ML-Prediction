import pandas as pd
import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open('randompicklet.pkl','rb'))
def welcome():
    return 'Welcome'

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

def main():
    st.title("This is nice")
    html_temp = '''
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-allign:center;">Streamlit This is nice ML App </h2>
# #     </div>'''
# Furnished	Semi-Furnished	Unfurnished	Bachelors	Bachelors/Family	Family	Bangalore	Chennai	Delhi	Hyderabad	
# Kolkata   Mumbai   Built Area  Carpet Area	Super Area	BHK	Size	Bathroom	Floor_Available
# Total_No_Of_Floors	Year_of_Posting	Month_of_Posting
    st.markdown(html_temp, unsafe_allow_html=True)
    #Gender = st.text_input("Gender", "Type Here")
    Furnishing=st.selectbox('Furnishing',options=['Furnished',	'Semi-Furnished',	'Unfurnished'])
    Preferred_Tenant = st.selectbox('Preferred Tenant',options=['Bachelors',	'Bachelors/Family',	'Family'])
    City = st.selectbox("City", options=['Bangalore',	'Chennai',	'Delhi',	'Hyderabad',	'Kolkata', 'Mumbai'])
    Area_Locality = st.selectbox('Area Locality',options=['Built Area',  'Carpet Area',	'Super Area'])
    bhk = st.slider("No. of Bedrooms, Halls and Kitchens", 0, 50)
    Size = st.slider("Size in Square Feet", 0, 10000)
    Bath = st.slider("No. of Bathrooms", 0, 50)
    Floor_Available = st.slider("Floor_Available", 0, 1000)
    Total_No_Of_Floors = st.slider("Total_No_Of_Floors", 0, 1000)
    Year_of_Posting = st.selectbox("Year_of_Posting", options=[2022])
    Month_of_Posting = st.selectbox('Month_of_Posting',options=['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    furnished , semi_furnished, unfurnished  = 0,0,0
    if Furnishing == 'Furnished':
        furnished = 1
    elif Furnishing == 'Semi-Furnished':
        semi_furnished = 1
    else:
        unfurnished = 1
        
    Bachelors,	BacheFam,	Family  = 0,0,0
    if Preferred_Tenant == 'Bachelors':
        Bachelors = 1
    elif Preferred_Tenant == 'Family':
        Family = 1
    else:
        BacheFam   = 1
    
    Bangalore, Chennai, Delhi,	Hyderabad, Kolkata, Mumbai = 0,0,0,0,0,0
    if City == 'Bangalore':
        Bangalore = 1
    elif City == 'Chennai':
        Chennai = 1
    elif City == 'Delhi':
        Delhi = 1
    elif City == 'Hyderabad':
        Hyderabad = 1
    elif City == 'Kolkata':
        Kolkata = 1
    else:
        Mumbai = 1
        
    Built_Area, Carpet_Area, Super_Area = 0,0,0
    if Area_Locality == 'Built Area':
        Built_Area = 1
    elif Area_Locality ==  'Carpet Area':
        Carpet_Area = 1
    else:
        Super_Area = 1
        
    month = 0
    if Month_of_Posting == 'January':
        month = 1
    elif Month_of_Posting == 'Febuary':
        month = 2
    elif Month_of_Posting == 'March':
        month = 3
    elif Month_of_Posting == 'April':
        month = 4
    elif Month_of_Posting == 'May':
        month = 5
    elif Month_of_Posting == 'June':
        month = 6
    elif Month_of_Posting == 'July':
        month = 7
    elif Month_of_Posting == 'August':
        month = 8
    elif Month_of_Posting == 'September':
        month = 9
    elif Month_of_Posting == "October":
        month = 10
    elif Month_of_Posting == 'November':
        month = 11
    else:
        month = 12

# Furnished	Semi-Furnished	Unfurnished	Bachelors	Bachelors/Family	Family	Bangalore	Chennai	Delhi	Hyderabad	
# Kolkata   Mumbai   Built Area  Carpet Area	Super Area	BHK	Size	Bathroom	Floor_Available
# Total_No_Of_Floors	Year_of_Posting	Month_of_Posting
    
    data1={
        'Furnishing': [furnished, semi_furnished, unfurnished],
        'Preferred_Tenant': [Bachelors, BacheFam, Family],
        'City': [Bangalore, Chennai, Delhi, Hyderabad, Kolkata, Mumbai],
        'Area_Locality':[Built_Area, Carpet_Area,Super_Area],
        'BHK':bhk,
        'Size':Size,
        'Bath': Bath,
        'Floor_Available':Floor_Available,
        'Tots':Total_No_Of_Floors,
        'Yr': Year_of_Posting,
        'Month': month,
        }

    feature_list=[data1['Furnishing'][0],data1['Furnishing'][1],data1['Furnishing'][2],data1['Preferred_Tenant'][0],data1['Preferred_Tenant'][1],data1['Preferred_Tenant'][2],data1['City'][0],data1['City'][1],data1['City'][2],data1['City'][3],data1['City'][4],data1['City'][5],data1['Area_Locality'][0],data1['Area_Locality'][1],data1['Area_Locality'][2],bhk, Size, Bath, Floor_Available, Total_No_Of_Floors, Year_of_Posting, month]

    single_sample = np.array(feature_list).reshape(1,-1)


    result = ""
    if st.button('Predict'):
        result = model.predict(single_sample)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()