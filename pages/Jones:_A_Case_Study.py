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
st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/graph/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F2f0f8a68e157c036b7db597d0bf3778e%2Fraw%2F5eba0bbfd2a092c7e5f87476d9288e53fb63eaf7%2F15-16.gexf&n=700%20S%20State%20St&ca[]=p&ca[]=g&ca[]=s&ca[]=d-s&ca[]=o-s&st[]=p&st[]=s&st[]=g&st[]=d-n"
  frameBorder="0" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown(
      """
      By 2019, however, 700 S State Street ceased to exist within the My Chi, My Future Dataset, and hasn't re-entered the fold since. 

      If you've read ***"A Decade of My Chi My Future"***, you may note that the same timespan in which Jones disappeared from the data is the timespan in which 
      the number of locations that Chicago Public Schools ran programming at skyrocketed from 87 to 200.

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

