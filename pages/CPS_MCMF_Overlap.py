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
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F3650b4b6962c3431f4479ade1b58057b%2Fraw%2F621fa230c829901616f46ea11188b81a32032907%2F23-24%252520New.gexf&c=s&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=g&st[]=s&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
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
#st.write("*Using 2023-2024 Data. CPS Providers in Green, MCMF Providers in Purple, overlapping providers in Yellow. Node Size Corresponds to Degree*")
col1, col2 = st.columns([1, 6])

# In the first column (1/5 width)
with col1:
    st.image("code.png", use_column_width=True)
    st.write("*Using 2023-2024 Data. Node Size corresponds to degree")

# In the second column (4/5 width)
with col2:
    st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2Fbdc0e8cba8181445100fc75b62dc6c97%2Fraw%2Fbfd7400cdd91518c7e5703cbd2ff661a37238caa%2FOverlapEdgesNew2.gexf&sa=r&ca=p&st[]=p&st[]=r" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("The graph above is an aggregation of the two prior graphs, attempting to capture overlap between providers in both platforms. *Fuzzyjoins were used to ensure that stylistic name variations were accounted for.* ")
st.write("We can see that the MCMF data continent is predominantly on the left, with the CPS data grouping on the right. \
         *Note that these directions are arbitrarily assigned and do not have any meaning outside of separating groups.* \
         When looking at the providers that appear in both datasets (in yellow), this means that nodes generally have a higher proportion of MCMF connections in the *left side* and a higher proportion of CPS connections in the *right side*. ")
st.write("")
st.write("Consider, for example, the location of *Chicago Park District* as compared to *Urban Initiatives* in the above graph")


st.header("MCMF/CPS OST Provider Network, Only Overlapping Providers and Locations")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2Fbdc0e8cba8181445100fc75b62dc6c97%2Fraw%2Fbfd7400cdd91518c7e5703cbd2ff661a37238caa%2FOverlapEdgesNew2.gexf&sa=r&ca=p&st[]=p&st[]=r&p.t[]=CPS%2FMCMF%20Provider&p.t[]=CPS%2FMCMF%20Location" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.write("We can note that most of the overlapping nodes fall generally in between the two main hubs, an intuitive result.") 
st.write("*These graphs are pretty and all, but what can we draw from these insights?*")
st.header("Assessing Motives")
st.write("I showed this graph to someone who used to work in Museum Education, and part of his reaction was \"so what? My organization had no interest in working with schools.\" And he was right, to an extent — programs have no obligation to widen their programmatic focus to include in-school *and* out-of-school if that doesn't suit their needs and capabilities.")
st.write("From a top-down data perspective, this splits the visualization into two buckets: Is the minimal overlap due to *lack of data, or lack of interest*? Moreover, if the answer was the latter, and only 5% of providers wanted to work across in-school and out-of-school, what does that say about the sinew of the afterschool ecosystem in Chicago?")
st.write("")
st.write("I recently attended a stakeholder meeting where both CPS and DFSS — which oversees My Chi, My Future—\
         were in attendance. During the meeting, the DFSS rep voiced that programs in My Chi, My Future felt that they were losing students to in-school programming, and didn't know how to access this population of students. \
         A major contributing factor to this shift was the fact that it is easier for students to stay at their schools and attend on-site programming. ")
st.write("Two observations stem from this: First, it combats the idea that the datasets don't overlap due to their lack of mutual interest, and shines a light on the desire, yet inability, to access certain populations from the MCMF side.\
         Second, it ties into our lab's opportunity landscaping work around where students attend school, versus where they live, and how this affects their geographies of opportunity.")
st.write("The introduction of selective enrollment and selective transfer into the CPS system has led to an increase in the amount of students that live and go to school in different communities ***(cite?)***.\
         We can think about this in relation to the aforementioned shift in OST provider locations — namely, the possibility of a causal relationship between these\
         two trends. Students moving out of their neighborhood schools is not just an academic decision; it represents a shift in their nearby environments, social circles, and daily routines.\
         The departure from their home community puts them into closer proximity with programming in their new neighborhoods — however, they lack the natural knowledge of the opportunity landscape\
         that is derived from growing up within the community. It is natural, then, that they turn to their place of familiarity in a new neighborhood: Programming run by their school.")
st.write("This shift contains inherent danger towards the health of an overall OST ecosystem. Programming that cannot cultivate participation in their local communities may close, shutting out opportunities for those that remain in their communities or cannot mobilize to hotspots of opportunity. *Is there a specific argument for why it is important to have in-school and out-of school programming? flexibility? resources? freedom from school bureaucracy?*")
st.write("")
#st.header("Data:")
#st.write("An easy incongruency to see is the difference in structure between the two data sets: CPS lists their providers in relation to school names, while MCMF lists their providers in relation to physical addresses. Moreover, CPS data is sorted into school networks, while MCMF data is sorted by neighborhood.")
#st.write("Data alignment in these categories would help facillitate further analysis, but these limitations **do not change** the fact that there is so little overlap in the provider category: 22/466 providers can be found in both data sets, or about 4.7%  ")
st.header("Rethinking OST Outreach Design")
st.image("stream.png" )



