import streamlit as st
import pickle

def main():
    st.markdown("<h1 style='text-align: center; color:Blue;'>Insurance Premium Prediction</h1>",
                 unsafe_allow_html=True)
    #Load the train model
    with open('gb_reg_model.pkl','rb') as pkl:
        train_model = pickle.load(pkl)

    
    age = st.slider('Enter Your Age', 18,100)
    sex = st.selectbox('Sex', ('Male','Female'))
    if(sex=='Male'):
        sex=1
    else:
        sex=0
    bmi = st.number_input('Enter BMI Value',10,100)
    children =st.selectbox('Enter No of children',(0,1,2,3,4))
    smoker = st.selectbox('smoker', ('Yes', 'No'))
    if(smoker=='Yes'):
          smoker=1
    else:
          smoker=0

    region = st.selectbox('Enter your Region', ('Southwest', 'Southeast','Northwest','Northeast'))
    if(region=='Southwest'):
          region=1
    elif(region=='Southeast'):
          region=2
    elif(region=='Northwest'):
          region=3
    else:
          region=4

    button = st.button('Predict')

    #if button is clicked make prediction
    if button:
        result = train_model.predict([[age, sex, bmi, children, smoker, region]])
        st.success(f"Predicted Insurance Amount: {result}")



        

if __name__ == '__main__':
     main()

