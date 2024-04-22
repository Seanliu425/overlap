import streamlit as st

st.set_page_config(
    page_title="Home",
    layout="wide",
)

st.write("# Exploring Chicago's Out-of-School Time Social Networks")

st.sidebar.success("Take a look at different aspects of our exploration above:")

st.markdown(
    """
    As part of a comprehensive Opportunity Landscaping initiative within the City of Chicago, the team at [Digital Youth Network](digitalyouthnetwork.com)
    has been exploring social network analysis as a lens through which to understand opportunity distribution, and identify ways to map opportunity equitably.
    
    This page serves to document the corpus of work that DYN has been tinkering with over the past year. Please navigate the search bar to see examples of our work. 

    ### What is Social Network Analysis?
    Social network analysis is the process of investigating social structures 
    through the use of networks and graph theory. It characterizes networked structures 
    in terms of nodes and the ties, edges, or links that connect them.

    Our work builds on early contributions to OST and Social Network Analysis by Martha G. Russell and Marc Smith:
    [Network Analysis of a Regional Ecosystem of Afterschool Programs](https://files.eric.ed.gov/fulltext/EJ980174.pdf) as well
    as partnerships with Northwestern University, the City of Chicago, Chicago Public Schools, and Argonne National Laboratories, amongst others. 

    Our graphs are hosted using Ouestware's [Retina](https://ouestware.gitlab.io/retina/beta/#/) tool.

"""
)