import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.set_page_config(layout="wide")
st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF; /* Change to your desired background color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("""
# Understanding the Gap between MCMF and CPS Datasets in CPS
Within the Chicago Afterschool Provider Ecosystem, there are two central stakeholders: The My Chi, 
         My Future Platform originating from the Mayor's office, and Chicago Public Schools. 
""")
st.write("")
st.write("This webpage is an attempt at articulating the difference between the datasets, as well as thinking through ways to reconcile these differences")
st.write("Below, you will find social networks visualizing both networks, individually. Feel free to have a look around.")
st.header("Chicago Public Schools OST Provider Network, Visualized")
st.write("*Using 2023-2024 Data. Colors correspond to School Network, with Providers in Green. Node Size corresponds to degree.*")

st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2Fd0e78dd111b21c855601b77c9f278211%2Fraw%2Fb58aeec42e99057af1f9067d94a3df15c916d512%2Fcps_linchpin_export.gexf&c=n&s=d-n&sa=d-n&ca[]=p&ca[]=m-s&ca[]=n&st[]=n&st[]=d-n&st[]=p&ec=t&ed=u" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )

st.write("")

st.header("My Chi, My Future OST Provider Network, Visualized")
st.write("*Using 2023-2024 Data. Colors correspond to Neighborhood, with Providers in Purple. Node Size Corresponds to Degree*")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F04090f6b39884db8b6c4af8c9eeadae9%2Fraw%2F5fad181d32a1ca7cf92c20b5574e1e8b32fba56c%2FMCM2324.gexf&sa=r&ca[]=p&ca[]=g&st[]=p&st[]=g&st[]=r" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.write("Do you notice anything? See how many providers you can find that exist both in graphs. ")
st.header("My Chi, My Future and CPS OST Provider Network, Visualized")
st.write("*Using 2023-2024 Data. CPS Providers in Green, MCMF Providers in Purple, overlapping providers in Yellow. Node Size Corresponds to Degree*")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F52ef81dafb46b2657d0ce749093becb8%2Fraw%2F3b9c078e396e2fd5c269f3691bf9451b5c25c2e3%2FOverlapPastel.gexf&ca[]=i-s&ca[]=p&ca[]=o-s&ca[]=d-s&ca[]=wi-s&ca[]=wo-s&ca[]=wd-s&st[]=p&st[]=d-n&nr=0.954&lt=1.598" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )