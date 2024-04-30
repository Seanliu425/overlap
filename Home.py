import streamlit as st

st.set_page_config(
    page_title="Home",
    layout="wide",
)

st.write("# Exploring Chicago's Out-of-School Time Social Networks")

st.sidebar.success("Take a look at different aspects of our exploration above:")

st.markdown(
    """
    As part of a comprehensive Opportunity Landscaping initiative within the City of Chicago, the team at [Digital Youth Network](digitalyouthnetwork.org)
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

    ### How do I read Social Network Graphs?
    Our networks aim to visualize collaboration within Chicago OST networks by leveraging access to multiple city-wide datasets and 
    demonstrating webs of collaboration that may not be immediately visible. 
    
    The nodes in our graphs represent afterschool providers, community organizations, schools, and program locations, amongst others. A link between nodes represents reported collaboration between the two nodes — this could represent a provider reporting they work at a location, a school reporting that they work with a provider, or a provider working with another provider. 
    ***More than anything, these graphs should be understood as depictions of collaboration — a map to help pave future collaborations.*** 

    In many of our graphs, the nodes are sized by ***Degree***, a measure of how many links that each node has. If a graph is dominated by a select few nodes that contain the majority of the links, this is known as a ***Scale-Free Network***
    
    The graph format is arranged using a force-repulsion algorithm, meaning that nodes repel each other, but \
    those with links between them attract each other. The resulting image depicts hubs of collaboration between organizations: \
    nodes that are close in proximity are likely, but not guaranteed, to be connected. The layout of the graphs are structured to facillitate easy identification of collaboration between nodes, but the physical location of each node does not have any specific meaning.

"""
)
