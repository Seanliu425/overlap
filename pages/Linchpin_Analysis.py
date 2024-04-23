import streamlit as st
import base64
st.set_page_config(layout="wide")


def main():
    st.title("Identifying Local Uniqueness in Social Networks")
    st.write("You may have noticed that many networks run through a few key nodes, indicative of central funding structures or key civic organizations.\
             These are examples of Scale-Free networks, a term referring to networks where a select few nodes have a disproportionate impact on the overall network. ")
    
    st.write("")
    st.write("Note, for example, the influence of **Chicago's Park District** in our My Chi, My Future Network:")
    st.markdown(
        """
        <div style="border: 2px solid #000000; padding: 0px;">
            <iframe src="https://ouestware.gitlab.io/retina/beta/#/embed/?url=https%3A%2F%2Fgist.githubusercontent.com%2FSeanliu425%2F04090f6b39884db8b6c4af8c9eeadae9%2Fraw%2F5fad181d32a1ca7cf92c20b5574e1e8b32fba56c%2FMCM2324.gexf&n=Chicago%20Park%20District&sa=r&ca[]=p&ca[]=g" width="100%" height="600" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.write("As important as the civic institutions are, we also wanted to shine light on hyperlocal civic organizations that might not\
              have network-wide impact. This led us to the Moen Lab's work on [Linchpins](https://moen-lab.com/linchpin-score#:~:text=Linchpin%20score%20is%20a%20network,specialty%20among%20their%20neighbors'%20ties.)\
             a method of identifying locally unique providers within a network.")
    
    st.write("To highlight smaller nodes in the network, we look to identify their local uniqueness, building on a social network measure known as linchpin score, which captures the tendency of a provider to represent a unique service to its first-degree neighbors (Nemesure et. al, 2021). If the removal of a node from a network severs the surrounding nodes’ ability to access that attribute, it represents a unique link; the score produced is the proportion of these unique links  as compared to the node’s overall number of connections. ")
    
    col1, _, col2 = st.columns([1, 0.1, 2])

# Display image in the first column
    with col1:
        st.image("linchpin.png", caption="Linchpin Score, Visualized", use_column_width=True)

    with col2:
        pass

# Display text in the second column
    with col2:
        st.write("To the left, we can see a visual of the linchpin score, and how it represents uniqueness. For each diagram, those that carry the same attribute as Vi are shown in blue.")
        st.write("We can observe the application of this concept within a network in terms of attributes such as STEM program type: In the figures below, we measure the relevance that a robotics provider has to its direct network. In Figure 1, we observe that our robotics provider, in gold (denoted with a red star), has four direct collaborators within its network (denoted a-d). In Figures 2-5, we can see the connections of those four collaborators — the second-degree connections of our robotics provider — and notice that for each of those collaborators, they are not connected to any other robotics provider. Thus, if the robotics provider were to dissolve or leave its local community, all of its connections would lose access to a robotics provider in their community. In this case, the robotics provider obtains a linchpin score of one — four unique connections out of four total connections. ")
    
    st.write("")
    st.image("figures.png")
    st.write("By zooming out, we begin to understand why measures of local uniqueness are crucial to understanding the nuances of individual communities within a city-wide network. In Figure 6, node sizes represent degree centrality, the number of overall connections that a provider has throughout the network. Here, our low-degree robotics provider is difficult to identify amongst a dense set of alternative providers, as the network is dominated by high-degree actors, characteristic of a scale-free network. In Figure 7, node size is determined by linchpin score. Organizations that provide a unique service to their local communities (high linchpin scores) - such as the robotics provider - are highlighted through their node size and identifiable throughout the network.")
    st.write("Combining network-wide analysis with a focus on local communities allows us to derive stronger micro-level conclusions regarding provider interactions, as well as provide information to providers and communities that they could not typically access. Consider that programs may not be aware of their second-degree partners, the determining factor in deciding a program’s uniqueness. In this case, programs that have high linchpin scores, meaning that their network would be left vulnerable if the program were to dissolve or leave, would not be aware of their own importance. Communities can leverage linchpin data to provide resources that shore up vulnerable spots within their community. Furthermore, a program’s knowledge that they have a high linchpin score gives them agency to request funding on the premise that they hold a particularly important role within their community. On the contrary, the realization that a program has a low linchpin score — their neighborhood is infrastructurally capable of handling their departure — may provide them with the freedom to move to new neighborhoods that don’t share the same luxury. At a city-wide level, the recognition that certain neighborhoods have higher linchpin scores, meaning that they are more siloed and closed off, can be leveraged to foster cross-neighborhood initiatives.")
if __name__ == "__main__":
    main()