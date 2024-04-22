import streamlit as st
import base64
st.set_page_config(layout="wide")

def embed_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode()
    st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

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
             a method of identifying locally unique providers within a network. You can read more about the methodology in the poster below." )
    pdf_path = "linchpin.pdf"
    st.write("")
    st.write("***Navigating Scale-Free OST Provider Networks within Afterschool Ecosystems:***")

    embed_pdf(pdf_path)

if __name__ == "__main__":
    main()