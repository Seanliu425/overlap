import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
from PIL import Image 
st.set_page_config(layout="wide")


st.write("""
# A Decade of My Chi, My Future
My Chi, My Future, founded as Chicago City of Learning in 2014 and rebranded to MCMF under former Mayor Lori Lightfoot, has been the City of Chicago's primary resource for out-of-school time (OST) programmming for the last ten years.  
""")

st.write("After a decade of use, three mayors, and one pandemic, how has the MCMF data adapted?")
st.write("This page attempts to answer that through a series of two-year social networks -- Let's start 10 years, ago, with the first iteration of the network in 2015-2016:")

st.write("***MCMF 2015-2016 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")

st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2Fd6300c2bb749924b940bb5050739107a%2Fraw%2F4b019a6bf20d2712c3ca0714dfd3c82ebd3b79bd%2F15-16%252520new.gexf&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=g&st[]=p&st[]=s&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )
st.write("")
st.write("The resulting graph, 130 providers and 909 locations, shows a heavy emphasis on core civic providers within the city. **Afterschool Matters**, in particular, has a strong influence on the network, running programs at 492 different locations, more than 50% of all the locations shown. This theme continues in 2017-2018, shown below: ")
st.write("")    
st.write("***MCMF 2017-2018 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F1851a45cbe5f3858bd441c5b6f47263f%2Fraw%2F66956755f6f208b415b4c44a75498dc4db3b7c88%2F17-18%252520New.gexf&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=g&st[]=s&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )
st.write("")
st.write("In 2017-2018, the number of providers consolidates slightly, with 108 providers and 932 locations. However, the rich get richer, with the two largest nodes continuing their expansions. **Chicago Park District** increases from 273 to 343 locations, and **Afterschool Matters** increases to 508 locations. ")
st.write("")
st.write("***MCMF 2019-2020 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F9c784d5aeb31c151e90ea30792077264%2Fraw%2F020a0215da43a607d8af8343b1df5f728682892f%2F19-20%252520new.gexf&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=s&st[]=g&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )
st.write("")
st.write("2019-2020 marks the onset of COVID-19, and the ramifications can be seen clearly throughout the network. **Afterschool Matters** sees a 100% decrease in number of programming locations; on the flipside, virtual programming sees over 100% growth in number of providers. **Chicago Park District** sees a reduction in locations as well, but not as large as ASM: could this be a result of the outdoor space being more pandemic suitable?")
st.write("Something else to keep an eye on: **Chicago Public Schools** increases its programming locations to 200 during this period, its only two-year stretch breaking 100 locations during the past decade. The manner in which schools decided to bring programs in house, and whether that had lasting ramifications, is something that I would like to explore further")
st.write("")
st.write("***MCMF 2021-2022 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F49156de47944d2c860361be16baf9642%2Fraw%2F8a580e88e9eede03bf0345f9d9e0e32cbb972ff5%2F21-22%252520New.gexf&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=g&st[]=s&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )
st.write("")
st.write("2021-2022 sees virtual programming continue its increase, up to over 200 programs. Conversely, Afterschool Matters continued its decline, down to 203 locations, with CPS also declining from 200 locations down to 57. Chicago Park District increased by nearly 100 locations during this time span. This, then, brings us to the current state of programming in MCMF. ")
st.write("")
st.write("***MCMF 2023-2024 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F3650b4b6962c3431f4479ade1b58057b%2Fraw%2F621fa230c829901616f46ea11188b81a32032907%2F23-24%252520New.gexf&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=g&st[]=s&st[]=d-n" width="100%" height="600" style="border:none;"></iframe>
        </div>
    
        """,
        
        unsafe_allow_html=True
    )
st.write("")
st.write("The graph of 2023-24, above, sees a recession in amount of virtual programming, along with new programs such as ***Cycle Breakers*** entering the fray -- Chicago Park District and Afterschool Matters continue their strong hold on the network, while Chicago Public Schools continues to decline, working at only 40 locations. ")
st.write("You may have noticed that we only spoke about a small subset of the programs in My Chi, My Future over the duration of the time-span. This is partly due to the fact that MCMF represents a *scale-free* network, meaning that a few nodes dominate most of the links within the network -- In this case, providers such as Chicago Park District and After School Matters.")
st.write("If you'd like to learn more about the work we are doing to help spotlight smaller nodes within the network, please see our page on ***Linchpin Analysis*** in the sidebar")
st.header("Notes on Data and Methodology:")
st.write("These graphs are meant primarily to support data exploration and spark conversation around observations from the data. We acknowledge that the amount of locations that a provider works at isn't a perfect proxy for organizational impact, nor does it capture depth of impact at any singular location. ")
st.write("A link between a provider and location represents that the provider has reported running programs at that location. Our data does not include provider-provider or location-location collaborations")

import streamlit as st
import pandas as pd
import altair as alt

import streamlit as st
import pandas as pd
import altair as alt

# Sample data
data = pd.DataFrame({
    'date': ['2015-2016', '2017-2018', '2019-2020', '2021-2022', '2023-24'],
    'Afterschool Matters': [492, 508, 267, 203, 207],
    'Chicago Public Schools': [100, 87, 200, 57, 40],
    'Chicago Park District': [273, 343, 261, 350, 344],
    'Chicago Public Library': [116, 116, 101, 130, 148],
    '# of Virtual Programs': [68, 73, 148, 201, 101 ]
})

# Convert 'date' column to string type
data['date'] = data['date'].astype(str)

# Create Altair chart
chart = alt.Chart(data).transform_fold(
    ['Afterschool Matters', 'Chicago Public Schools', 'Chicago Park District', 'Chicago Public Library', '# of Virtual Programs'],
    as_=['Variable', 'Value']
).mark_line().encode(
    x=alt.X('date:N', title='Year Span', axis=alt.Axis(labelAngle=0)),  # Set label angle to 0 degrees
    y=alt.Y('Value:Q', title='# of Locations'),
    color='Variable:N'
).properties(
    width=500,
    height=300,
    title='Variations in # of Locations in High Density Nodes (2015-2024)'
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

# Display Altair chart using st.altair_chart()
st.altair_chart(chart, use_container_width=True)
