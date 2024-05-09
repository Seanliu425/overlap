import streamlit as st
import base64
from streamlit_folium import folium_static
import folium
st.set_page_config(layout="wide")



st.title("A Case Study of Jones High School")
st.markdown(
      """
      Sometimes when conducting data exploration, you fall down a rabbit hole that leads to more questions than answers. Our exploration of Jones College Prep 
      raises questions around data continuity between platforms, as well as motivations around changes in programming.

      Jones College Prep is one of the most prestigious public high schools in Illinois, housing 2,000 students within its 9-12 programming at its location in Chicago's South Loop. 

      Between 2015-2016, Jones was one of the busiest locations in Chicago's My Chi, My Future platform, with 23 organizations running programs at their building, **700 S State Street.**

    """
    )
st.write("***MCMF 2015-2016 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.write("***If the graph is not visible, click the << in the top left.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/graph/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2Fd6300c2bb749924b940bb5050739107a%2Fraw%2F4b019a6bf20d2712c3ca0714dfd3c82ebd3b79bd%2F15-16%252520new.gexf&n=700%20S%20State%20St&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=g&st[]=p&st[]=s&st[]=d-n"
  frameBorder="0" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown(
      """
      By 2019, however, 700 S State Street ceased to exist within the My Chi, My Future Dataset, and hasn't re-entered the fold since. 

      If you've read ***"A Decade of My Chi My Future"***, you may note that the same timespan in which Jones disappeared from the data is the timespan in which 
      the number of locations that Chicago Public Schools ran programming at skyrocketed from 87 to 200. However, none of those programs were at Jones College Prep.

    """
    )
st.write("***MCMF 2019-2020 Data. Providers in Green, Locations in Red. Node Size corresponds to degree.***")
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/graph/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F9c784d5aeb31c151e90ea30792077264%2Fraw%2F020a0215da43a607d8af8343b1df5f728682892f%2F19-20%252520new.gexf&n=Chicago%20Public%20Schools%20(CPS)&ca[]=p&ca[]=g&ca[]=s&ca[]=i-s&ca[]=o-s&ca[]=d-s&st[]=p&st[]=s&st[]=g&st[]=d-n"
  frameBorder="0" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write("")
st.markdown(
      """
     **So where did Jones go?** 
     
     A dive into CPS's internal dataset shows 119 programs listed from 10/4/21 to 8/1/23, exclusively run by ***School Staff***
     and ***Central Office Employees*** (*shouldn't this be represented as a CPS -> Jones connection on MCMF?*), but no external providers. 
     This reflects a key pattern that is detailed in ***"CPS MCMF Overlap"***: That internal school programs have begun to overtake external provider programming within the Chicago OST ecosystem.

    It can be useful to think about the role of Jones in the OST ecosystem geographically, as well. Jones is just down the street from the City of Chicago's flagship library, Harold Washington Library Center.
    
    Why aren't they working together? Or perhaps a better question to ask is: how can we get them to work together?
    """
    )



st.write("**Jones CP proximity to Harold Washington Library**")
    
    # Create a map centered at a specific location
m = folium.Map(location=[41.87495825121683, -87.62775579917627], zoom_start=16, width = '100%')

    # Add markers for the start and end points
start_point = [41.87311896160743, -87.62792130267754]
end_point = [41.876379062445686, -87.62810510267744]
folium.Marker(start_point, popup='Jones College Prep').add_to(m)
folium.Marker(end_point, popup='Harold Washington Library').add_to(m)

    # Draw a PolyLine between the two points to represent the path
folium.PolyLine(locations=[start_point, end_point], color='blue').add_to(m)

    # Display the map using Folium's built-in function for Streamlit
folium_static(m)

st.markdown(
      """
     The goal of this little deep dive is not to chastise Jones for moving their programs in-house, but rather to start a dialogue around what factors are leading to this.
     Data transparency is also important to help programs in My Chi, My Future understand patterns of participation from their locations. 
     
     From the MCMF side, they can see that Jones stopped running programming, but they can't see where it went — to internal programming. For programs in MCMF that are looking to re-engage with these school populations, this information could be useful.
    """
    )

