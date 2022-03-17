#from cgitb import html
from pandas import describe_option
from pyparsing import col
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from datetime import datetime, date
import streamlit.components.v1 as components
import requests

# Configuring page
st.set_page_config(page_title='MemoBrain', page_icon='🧠', initial_sidebar_state="auto", menu_items=None)

# Navigation Bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: black;">
  <a class="navbar-brand" target="_blank"> <font color = 'white'> MemoBrain </color> </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/mkvph0ch/memobrain" target="_blank">🐈‍⬛ <b> Source code </b></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.oasis-brains.org/" target="_blank">📄 <b> Dataset </b></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.lewagon.com/" target="_blank">🚂 <b>LeWagon</b></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# Menu in SideBar
with st.sidebar.expander('📋 CLICK TO DISPLAY MENU'):
#with st.sidebar():
    choose = option_menu(None, ["Home", "About", "Our App", "Our Project", "Contact"],
                            icons=['house', 'emoji-smile', 'app-indicator','journal-text','person lines fill'],
                            menu_icon="list", default_index=0, orientation='vertical',
                            styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# To choose icons: https://icons.getbootstrap.com/ , https://icons8.com/icons/set/brain


# Home Page
if choose == 'Home':
    new_title = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 42px;"> Welcome to MemoBrain </p>'
    st.markdown(new_title, unsafe_allow_html=True)
    describe = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 18px;"> We use powerful machine learning algorithms to aid in the diagnosis of Alzheimer&apos;s Disease. </p>'
    st.markdown(describe, unsafe_allow_html=True)
    # col1, col2, col3 = st.columns(3)
    # with col2:
    st.image("https://media-exp1.licdn.com/dms/image/C5612AQHP5WYhYOHFRg/article-cover_image-shrink_720_1280/0/1590038951387?e=1652313600&v=beta&t=9W81QeX1liNEpegeLH9FQ0ris8coyYBnDteDOpLcxTE", use_column_width=True)
    start = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 18px;"> 👆🏼 Click on the sidebar menu to start </p>'
    st.markdown(start, unsafe_allow_html=True)
    #components.html("""<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 18px;"> Click on the sidebar menu to start 👆🏼</p>""")

    st.markdown("[![Github](https://img.icons8.com/bubbles/2x/github.png)](https://github.com/mkvph0ch/memobrain) Click to see Under The Hood!")
    st.markdown(" Click for our Streamlit code  [![Github](https://img.icons8.com/bubbles/2x/code.png)](https://github.com/cynthias13w/memobrainweb)")

if choose == "About":
    # Title
    new_title = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 42px;"> Welcome to MemoBrain </p>'
    st.markdown(new_title, unsafe_allow_html=True)
    #col1, col2 = st.columns( [0.8, 0.2])
    #with col1:               # To display the header text using css style



    st.markdown('<p class="font">About the Creators</p>', unsafe_allow_html=True)
    st.write("Hello there! We are Marko, GueHo, Vicente and Cynthia! We attended LeWagon Data Science Bootcamp in Berlin from January 2022 to March 2022. Thank you for visiting our website! ")
    st.write("Here we are pleased to present our final project which encompasses the skills that we acquired during the bootcamp including data analysis, cleaning, and visualization with NumPy and Pandas, machine learning and deep learning with Scikit-learn and Tensorflow, cloud computing with Docker and Google Cloud Platform, and front-end development with Streamlit.")
    marko = Image.open('marko.jpg.png')
    gueho = Image.open('gueho.jpg')
    vicente = Image.open('vicente.jpg.png')
    cynthia = Image.open('cynthia.jpg.png')
    st.write(" ")
    st.write(" ")

    col11, col22, col33, col44 = st.columns(4)
    with col11:
        st.markdown("""**Marko**""")
        st.image(marko)
        st.markdown("[![Github](https://img.icons8.com/small/2x/github.png)](https://github.com/mkvph0ch/)")

    with col22:
        st.markdown("""**GueHo**""")
        st.image(gueho)
        st.markdown("[![Github](https://img.icons8.com/small/2x/github.png)](https://github.com/Gueho/)[![LinkedIn](https://icons.iconarchive.com/icons/danleech/simple/24/linkedin-icon.png)](https://www.linkedin.com/in/guehojang/)")

    with col33:
        st.markdown("""**Vicente**""")
        st.image(vicente)
        st.markdown("[![Github](https://img.icons8.com/small/2x/github.png)](https://github.com/vicentefuhrmann/)[![LinkedIn](https://icons.iconarchive.com/icons/danleech/simple/24/linkedin-icon.png)](https://www.linkedin.com/in/vicente-fuhrmann/)")

    with col44:
        st.markdown("""**Cynthia**""")
        st.image(cynthia)
        st.markdown("[![Github](https://img.icons8.com/small/2x/github.png)](https://github.com/cynthias13w/)[![LinkedIn](https://icons.iconarchive.com/icons/danleech/simple/24/linkedin-icon.png)](https://www.linkedin.com/in/cynthias13w/)")


#with col2:               # To display brand log
    #pass

    st.markdown("""

    Please do not hesitate to contact us 😄



    ~
    """)
    st.markdown('<p class="font">Project Details</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Title**: Neurocognitive Disease Prediction on Metadata and Brain MRI

    **LeWagon Batch**: #815

    **App**: MemoBrain

    **ML model**: Random Forest Classifier""")

    st.markdown(""" <style> .font {
            font-size:35px ; text-align: center; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
            </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">About our Project</p>', unsafe_allow_html=True)
    st.markdown(""" To this day, Alzheimer’s Disease (AD) is diagnosed through medical history, and cognitive and physical tests. To support this diagnosis, brain scans such as Magnetic Resonance Imaging (MRI) can be performed.
    However, it is still a challenge to distinguish between Alzheimer’s and no Alzheimer’s.

    But what if we could train machines to yield a predictive diagnosis? How can a machine compare to human eyes?

    Enter MemoBrain. MemoBrain can predict whether a person may have Alzheimer’s or not based on a total of eight features (sex, age, education, socioeconomic status, score on Mini-Mental State Examination, estimated total intercranial volume (mm3), normalized whole brain volume, and atlas scaling factor).

        """)

# App Page
if choose == "Our App":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> <img src="https://img.icons8.com/pastel-glyph/64/000000/brain--v1.png"/>  MemoBrain </p>', unsafe_allow_html=True)
        st.subheader("Please enter the following information:")
        st.markdown("""



        """)

# List of features: Age, Educ, SES, MMSE, eTIV, nWBV, ASF

    col1, col2 = st.columns(2)
    with col1:
        sex = st.selectbox('SEX:', ('M', 'F'))
        EDUC = st.selectbox('SELECT LEVEL OF EDUCATION COMPLETED:',
     ('Lower than high school', 'Graduated High school', 'Some college', 'College graduate', 'Beyond college'))
        MMSE = st.number_input('SCORE ON MINI-MENTAL STATE EXAMINATION:', min_value = 0, max_value = 30, value = 28, step = 1)
        nWBV = st.number_input("SELECT nWBV:", value = 0.728)

    with col2:
        birthday = str(st.date_input("DATE OF BIRTH:", date(1960, 12, 1)))
        #d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
        SES = st.selectbox('SOCIOECONOMIC STATUS:', ('1', '2', '3', '4', '5'))
        eTIV = st.number_input("SELECT eTIV:", value = 1500)
        ASF = st.number_input("SELECT ASF:", value = 1.194)

    # API
    #birthday = datetime(year=int(birthday[0:4]), month=int(birthday[4:6]), day=int(birthday[6:8]))
    birthday = datetime(year=int(birthday[0:4]), month=int(birthday[5:7]), day=int(birthday[8:10]))
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

#Encode Education
    education = {'Lower than high school': '7',
                'Graduated High school': '11',
                'Some college': '14',
                'College graduate': '17',
                'Beyond college': '21'}

    for k, v in education.items():
        EDUC = EDUC.replace(k, v)

    # for k, v in education.items():
    #     for i in v:
    #         if i in v:
    #             EDUC = EDUC.replace(k, i)
    # #6-8   1 9-12  2 13-15  3 16-19  4 20-23  5


    result = {"M/F": str(sex),
    "Age": float(age),
    "EDUC": float(EDUC),
    "SES": float(SES),
    "MMSE": float(MMSE),
    "eTIV": float(eTIV),
    "nWBV": float(nWBV),
    "ASF": float(ASF)
    }

    submitted = st.button("Submit")
    with st.spinner('Please wait a few seconds...'):
        #time.sleep(5)
        if submitted:

            st.success('Here are your results:')
            url = "https://memobrain-image-zhbxvookva-ew.a.run.app/predict"
            response = requests.get(url, result).json()
            prediction = str(response['diagnosis'])
            #st.metric("Prediction", prediction)

            def prediction():
                prediction = str(response['diagnosis'])
                if prediction == '0':
                    return("You are healthy 😊")
                else:
                    return("You may have Alzheimer's disease")

            #st.metric("OUR PREDICTION", prediction)
            st.metric("OUR PREDICTION", prediction())




    st.markdown("""



    **Note:**

    **MMSE**: Mini-Mental State Examination

    **SES**: Socioeconomic Status

    **eTIV**: Estimated Total Intercranial Volume (mm3)

    **nWBV**: Normalized Whole Brain Volume

    **ASF**: Atlas Scaling Factor
    """)

# Our Project Page
if choose == "Our Project":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Our Project</p>', unsafe_allow_html=True)
        st.write("Here, we provide a description of how we went about the project. Have fun reading!")
        st.subheader("Datasets")
        st.write("Our datasets consisted of Oasis 1 and Oasis 2. The main difference between the two datasets lies in the fact that they are cross-sectional and longitudinal collections respectively. We first visualized our metadata using matplotlib, seaborn and plotly packages. Since the greatest known risk factor of AD is increasing age, most people with Alzheimer's are generally 65 and older. This is reflected in the histogram below which was generated from one of the datasets.")

        image = Image.open('notebooks/oasis1_age.png')
        st.image(image)
        st.image(Image.open('notebooks/oasis1_ses.png'))
        st.image(Image.open('notebooks/oasis1_education.png'))


        st.subheader("Preprocessing of Metadata")
        st.markdown(""" Owing to lack of samples of people with 'moderate' dementia, we decided to reduce our four CDR classes to two classes: whether a person has Alzheimer's Disease or not. """)

        st.subheader("Machine Learning")
        st.markdown("""
        We set out to explore the following supervised machine learning classification models:

        - Logistic Regression
        - Support Vector Classifier
        - KNeighborsClassifier
        - Decision Tree Classifier
        - AdaBoostClassifier
        - RandomForestClassifier
        - AdaBoost

        For each model, we gridsearched the best parameters. Our Random Forest Classifier yielded the highest recall score 85%. After fitting the model with the best parameters, we built an API. Our product, a predictive app, finally lies in the 'Our App' section of this website.
        """)

        st.subheader("Deep Learning")
        st.markdown("""Since our MRI images dataset was a whopping 85GB of data, we first compressed our images. This involved converting 3D images to 2D as well as reducing the number of pixel colours. We also joined three different planes of brain images (transverse, sagittal and coronal) together as shown in the figure below.
        """)

        brains = Image.open('image.png')
        st.image(brains)

        st.markdown("""The joined images were then fed to a convolutional neural network. After grid searching and applying the best parameters, our model achieved 80% accuracy!""")
        st.write('Thank you for reading.')
        st.write('Do not hesitate to reach out to us for more information.')

# Contact Page
if choose == "Contact":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Contact</p>', unsafe_allow_html=True)

        st.write("You may use this form to contact us. Please enter the following details. Thank you.")
        name=st.text_input(label='Name:')
        email = st.text_input(label='Email:')
        Message=st.text_input(label='Message:')
        submitted = st.button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')




# AN EXAMPLE
# url = 'example'
# response = requests.get(url, dictionary).json()
# response = requests.get("https://taxifare.lewagon.ai/predict", dictionary).json()
# fare = "$" + str(round(response['fare'], 2))
# st.metric("ESTIMATED COSTS", fare)
# st.metric("ESTIMATED DISTANCE", distance_func(lat1,lon1,lat2,lon2))
