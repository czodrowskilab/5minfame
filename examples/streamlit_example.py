import matplotlib.pyplot as plt
import numpy as np
import py3Dmol
import streamlit as st
from stmol import showmol


def main():
    st.markdown("# 10MinFame - streamlit ![streamlit logo](https://docs.streamlit.io/logo.svg)")
    pages = {
        "Basic functionalities": hv_stream,
        "What others did - streamlit_3dmol": third_party,
    }
    page_titles = pages.keys()

    page_title = st.sidebar.selectbox(
        "Choose the app mode",
        page_titles,
    )
    st.title(page_title)

    page_func = pages[page_title]
    page_func()


def hv_stream():
    # You can use markdown with st.markdown
    st.markdown(
        'According to [streamlit](https://streamlit.io): \n> A faster way to build and share data apps Streamlit '
        'turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.')

    # Text in header format
    st.header("Some features")
    # Text in subheader format
    st.subheader("It understands Markdown:")

    st.subheader("It understands LaTex:")
    # Formula in Latex expression
    st.latex(
        r"{\displaystyle {\vec {\nabla }}\cdot \left[\varepsilon ({\vec {r}}){\vec {\nabla }}\Psi ({\vec {"
        r"r}})\right]=-\left(\rho ^{f}({\vec {r}})+\sum _{i}c_{i}^{\infty }z_{i}\lambda ({\vec {r}})q\exp \left({"
        r"\frac {-z_{i}q\Psi ({\vec {r}})}{kT}}\right)\right)}")
    st.caption("Poisson-Boltzmann equation (from Wikipedia)")

    st.subheader("What else?")

    diss_const = st.slider("Select pKa", 0.0, 14.0, 0.01)

    def species_plot(pka):
        # Plot distribution of acid and corresponding base interactively with st.slider() func
        acid_conc = np.arange(0.00001, 0.99999, 0.00001)
        # Henderson Hasselbalch equation
        ph = pka + np.log10((1 - acid_conc) / acid_conc)

        fig, ax = plt.subplots()
        ax.plot(ph, 1 - (acid_conc / 1), label='A-')
        ax.plot(ph, acid_conc / 1, label='HA')

        ax.set(xlabel='pH', ylabel='microspecies dist',
               title=f'Distribution of monoprotic acid/base with pKa of {pka}',
               xlim=(0.0, 14.0), ylim=(0.0, 1.0))
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        ax.grid()
        return fig

    # st.pyplot plots matplotlib figure
    st.pyplot(species_plot(diss_const))


def third_party():

    # This example was taken from José Manuel Nápoles Duarte streamlit_3dmol and the tds article:
    st.sidebar.title('Show EP structures')

    # PDB structures adapted, aspartic protease endothiapepsin
    prot_str = '4Y3S,3PM4,4Y3P,4Y5C,5OG7,4Y4A,5QBG,4LAP'
    prot_list = prot_str.split(',')
    protein = st.sidebar.selectbox('select protein', prot_list)
    style = st.sidebar.selectbox('style', ['cartoon', 'line', 'cross', 'stick', 'sphere', 'clicksphere'])
    # Default color white
    bcolor = st.sidebar.color_picker('Pick A Color', '#ffffff')
    xyzview = py3Dmol.view(query='pdb:' + protein)
    xyzview.setStyle({style: {'color': 'spectrum'}})
    xyzview.setBackgroundColor(bcolor)
    showmol(xyzview, height=500, width=800)
    st.caption("Adapted from streamlit_3dmol examples")


if __name__ == "__main__":
    main()
