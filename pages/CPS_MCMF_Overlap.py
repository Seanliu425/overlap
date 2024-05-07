import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image 
st.set_page_config(layout="wide")


st.write("""
# Understanding the Gap between MCMF and CPS Datasets in CPS
When navigating the Chicago afterschool ecosystem, there are two names that you will encounter time and again: The My Chi, 
         My Future Platform originating from the Mayor's office, and Chicago Public Schools. 
""")
st.write("")
st.write("This page is an attempt at articulating the difference between the datasets, as well as thinking through ways to reconcile these differences: Below, you will find social networks visualizing both networks, individually. Feel free to have a look around.")
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
st.write("These graphs aim to visually articulate networks of collaboration within the two datasets. They can help to identify the major players within the network, as well as assets within specific communities")

st.write("The graph format is arranged using a force-repulsion algorithm, meaning that nodes repel each other, but \
         those with links between them attract each other. The resulting image depicts hubs of collaboration between organizations: \
         nodes that are close in proximity are likely, but not guaranteed, to be connected.") 

st.write("***Do you notice anything? See how many providers you can find that exist both in graphs.***")
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

st.write("")
st.write("The graph above is an aggregation of the two prior graphs, attempting to capture overlap between providers in both platforms. *Fuzzyjoins were used to ensure that stylistic name variations were accounted for.* ")
st.write("We can see that the MCMF data continent is predominantly in the bottom right corner, with the CPS data grouping in the top left corner. \
         *Note that these directions are arbitrarily assigned and do not have any meaning outside of separating groups.* \
         When looking at the providers that appear in both datasets (in yellow), this means that nodes generally have a higher proportion of MCMF connections in the *southeast corner* and a higher proportion of CPS connections in the *northwest corner*. ")
col2, col1 = st.columns(2)

cpd = Image.open("CPD.png")
col1.write("***CPD found in both datasets, majority MCMF connections***")
col1.image(cpd, use_column_width= True)

ymca = Image.open("YMCA.png")
col2.write("***YMCA found in both datasets, majority CPS connections***")

col2.image(ymca, use_column_width= True)

st.header("MCMF/CPS OST Provider Network, Only Overlapping Providers")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F52ef81dafb46b2657d0ce749093becb8%2Fraw%2F3b9c078e396e2fd5c269f3691bf9451b5c25c2e3%2FOverlapPastel.gexf&ca[]=i-s&ca[]=p&ca[]=o-s&ca[]=d-s&ca[]=wi-s&ca[]=wo-s&ca[]=wd-s&st[]=p&st[]=d-n&p.t=CPS%2FMCMF%20Provider&nr=0.954&lt=1.555" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.write("We can note that most of the overlapping nodes fall generally in between the two main hubs, an intuitive result.") 
st.write("*These graphs are pretty and all, but what can we draw from these insights?*")
st.write("I showed this graph to someone who used to work in Museum Education, and part of his reaction was \"so what? My organization had no interest in working with schools.\" And he was right, to an extent — programs have no obligation to widen their programmatic focus to include in-school *and* out-of-school if that doesn't suit their needs and capabilities.")
st.write("From a top-down data perspective, this splits the visualization into two buckets: Is the minimal overlap due to *lack of data, or lack of interest*? Moreover, if the answer was the latter, and only 5% of providers wanted to work across in-school and out-of-school, what does that say about the sinew of the afterschool ecosystem in Chicago?")
st.header("Assessing Motives")
st.write("I recently attended a stakeholder meeting where both CPS and DFSS — which oversees My Chi, My Future—\
         were in attendance. During the meeting, the DFSS rep voiced that programs in My Chi, My Future felt that they were losing students to in-school programming, and didn't know how to access this population of students. \
         A major contributing factor to this shift was the fact that it is easier for students to stay at their schools and attend on-site programming. ")
st.write("Two observations stem from this: First, it combats the idea that the datasets don't overlap due to their lack of mutual interest, and shines a light on the desire, yet inability, to access certain populations from the MCMF side.\
         Second, it ties into our lab's opportunity landscaping work around where students attend school, versus where they live, and how this affects their geographies of opportunity.")
#st.header("Data:")
#st.write("An easy incongruency to see is the difference in structure between the two data sets: CPS lists their providers in relation to school names, while MCMF lists their providers in relation to physical addresses. Moreover, CPS data is sorted into school networks, while MCMF data is sorted by neighborhood.")
#st.write("Data alignment in these categories would help facillitate further analysis, but these limitations **do not change** the fact that there is so little overlap in the provider category: 22/466 providers can be found in both data sets, or about 4.7%  ")
