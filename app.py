from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "CV.pdf"
profile_pic = current_dir / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Tai Nguyen"
PAGE_ICON = ":wave:"
NAME = "Tai Nguyen"
DESCRIPTION = """
Data Scientist, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "tai.nguyent0@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/tainguyent/",
    "GitHub": "https://github.com/TaiNg365",
}
#PROJECTS = {
#    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
#}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ `4+` Years experience extracting actionable insights from big data
- ✔️ Strong hands on experience and knowledge in Python, R, SQL, and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong verbal and written communication skills as demonstrated by received the first place award at Michigan Louis Stokes Alliance for Minority Participation (MI-LSAMP) Conferences
"""
)



# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 🧑🏻‍💻 Programming: `Python` , `R`, `SQL`
- 🧑🏻‍💻 Data processing/wrangling: `SQL`, `pandas`, `numpy`
- 📊 Data Visualization: `matplotlib`, `seaborn`, `plotly`, `ggplot2`, `PowerBI`, `MS Excel`
- 🤖 Machine Learning: `scikit-learn`
- 🏞 Deep Learning: `Tensorflow`
- 📚 Natural Language Processing: `NLTK`, `SpaCy`, `GenSim`
- 🗄️ Databases: `MongoDB`, `MySQL`
- 📚 Modeling: `Logistic Regression`, `Linear Regression`, `Decision Trees`
- 👨🏻‍🔧 Model Deployment: `streamlit`, `R Shiny`, `AWS`
"""
)


# --- EDUCATIONS ---
st.write("#")
st.subheader("Educations")
st.write(
    """
- 🎓 Master of Science (Applied Mathematics): Michigan State University, East Lansing, MI
- 2017 - 2018
- 🎓 Bachelor of Science (Mathematics): Michigan State University, East Lansing, MI
- 2013 - 2017
- 🎓 Bachelor of Science (Actuarial Science): Michigan State University, East Lansing, MI
- 2013 - 2017
    """
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("💼", "**METHODOLOGY LEAD | NielsenIQ | Chicago, IL**")
st.write("August 2020-Present")
st.write(
    """
- ► Developing methodology for new analytic products to meet clients' requirement.
- ► Leading End-to-End project from developing to the delivery of project to clients.
- ► Developing effective data visualization dashboard to showcase the analytics deliverable to clients.  
- ► Supporting the discovery of new partners and vendors to lower investment costs and minimize margin.
- ► Supporting deep-dive analytics and data science execution for new and existing pilot projects. 
"""
)

# --- JOB 2
st.write("#")
st.write("💼", "**DATA SCIENTIST | NielsenIQ | Chicago, IL**")
st.write("August 2019 - August 2020")
st.write(
    """
- ► Utilized statistical methodology to resolve specific client inquires.
- ► Developed robotic process automation using python to reduce the investigative time spent on an inquiry, reducing costs by `$60,000` annually.
- ► Enhanced sales data flagging system using SARIMA machine learning model and improve accuracy by `30%`.
"""
)

# --- JOB 3
st.write("#")
st.write("💼", "**PREDICTIVE MODELER | Auto-Owners Insurance Company | East Lansing, MI**")
st.write("January 2018 - August 2019")
st.write(
    """
- ► Applied machine learning techniques to develop a new competitor's territory metric, increasing the accuracy of competitors' relativities by `10%`.
- ► Built random forest and gradient boost model using R to accurately represent the usage distribution of vehicles for policy underwriting.
- ► Revived and updated the company's Auto DataMart to optimize data storage efficiency.
- ► Built, evaluated, and documented predictive models using Emblem.
"""
)


# --- Projects & Accomplishments ---
#st.write("#")
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")