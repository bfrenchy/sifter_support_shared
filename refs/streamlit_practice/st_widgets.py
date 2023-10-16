import streamlit as st
import pandas as pd

# TEXT INPUT - widgets should alwasy be treated as variables
name = st.text_input('Your name: ')
if name:
    st.write(f"Hello {name}!")

st.divider()  # add horizontal line

# NUMBER INPUT
x = st.number_input('Enter a number', min_value=1, max_value=99, step=1)
st.write(f"The current number is {x}")

st.divider()  # add horizontal line

# BUTTON
clicked = st.button('Click me')
if clicked:
    st.write(':blush:')

st.divider()

# CHECKBOX
agree = st.checkbox('I agree')
if agree:
    'Great, thank you for agreeing'  # Magic
# You can hide or show with these conditions
checked = st.checkbox('Continue', value=True)
if checked:
    ':100:' * 5


df = pd.DataFrame({'Name': ['Ben', 'Bing', 'Bong'],
                   'Age': [30, 25, 40]
                   })
if st.checkbox('Show data'):
    df

st.divider()
"Radio buttons"

# RADIO BUTTON
pets = ['cat', 'dog', 'fish', 'turtle']
pet = st.radio('Favorite pet', pets, index=2, key='your_pet')
st.write(f"Your favorite pet: {pet}")
st.write(f"Your favorite pet: {st.session_state.your_pet * 3}")

st.divider()
# SELECT
"Select"

cities = ['London','Los Angeles','New York City']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You live in {city}.')

st.divider()
# SLIDER
x = st.slider('SLIDER', value=15, min_value=12, max_value=78, step=3)
st.write(f"x is {x}")

st.divider()
# FILE UPLOADER
"Upload a file"
uploaded_file = st.file_uploader('Upload a file:', type=['.xlsx', '.txt', '.csv', '.pdf'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    if uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
    if uploaded_file.type == 'application/pdf':
        st.write("This is a pdf")
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df.head())

st.divider()
# CAMERA INPUT
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3SY2fRkmTMnluD5WdY0MBOolkFkVF3N8ChAGEw8c&s')
