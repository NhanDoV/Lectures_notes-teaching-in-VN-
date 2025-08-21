import streamlit as st

# ======= Title of the page =======
st.set_page_config(layout="wide")
st.title("📚 DVN_App Learning Stats")

# ======= Sidebar for topic selection =======
topic = st.sidebar.selectbox(
    "Select a topic to explore:",
    ("Distribution comparision", "Clearify by proofs", "Other notes")
)
distribution_ls = ["Bernoulli", "Binomial", "Poisson", "Geometry", "HyperGeometry", "Negative Binomial", "Negative HyperGeometry",
                    "Uniform (descrete type)", "Uniform (continuous type)", "Normal", "Exponential", "Student", "Chi-squared",
                    "Fisher", "Beta", "Gamma", "Cauchy"
                    ]
features = ["Notation", "Description", "Parameters", "Domain", 
            "pmf / pdf", "cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", 
            "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"
            ]

# ======= Content rendering based on topic =======
if topic == "Distribution comparision":
    import libs.all_distr_helper as all_distr
    st.header("Comparision")
    # Select 2 distributions and show all the table of each params
    c1, c2 = st.columns(2)
    with c1:
        distr_1 = st.selectbox("Select the target-distribution", distribution_ls)
    with c2:
        distribution_ls.remove(distr_1)
        distr_2 = st.selectbox("Select other distribution to compare", distribution_ls)
    
    st.subheader("Comparison table \n")
    a1, a2, a3 = st.columns([1,4,4])
    
    # Build table rows
    table_rows = []
    for fea in features:
        val1 = all_distr.get_distr_features(distr_name=distr_1, features_name=fea) or "-"
        val2 = all_distr.get_distr_features(distr_name=distr_2, features_name=fea) or "-"
        table_rows.append([fea, val1, val2])
        
    import pandas as pd
    df = pd.DataFrame(table_rows, columns=["Feature", distr_1, distr_2])

    # Custom markdown render for LaTeX support in columns     
    st.markdown(all_distr.render_latex_table(df, distr_1, distr_2), unsafe_allow_html=True)

elif topic == "Clearify by proofs":
    st.header("Clarify with proofs")
    from libs.proofs import *
    # Select objects to see (distribution type - features)
    c1, _, c2, c3 = st.columns([5,1,5,5])
    with c1:
        topic = st.selectbox("Select a topic", proof_dict.keys()) 
    with c2:
        branch_1 = st.selectbox("Select one of", proof_dict[topic].keys())
    with c3:
        branch_2 = st.selectbox("Proof of", proof_dict[topic][branch_1]) 

    display_proofs(topic, branch_1, branch_2)
                        
else:
    st.header("Some notes")
    from libs.other_notes import *
    c1, c2 = st.columns(2)
    with c1:
        tips_type = st.selectbox("Select one of", ["Replacement tips", "Distribution tips", "Markov chain", "Regression", "Convergence Theorems"]) 
    with c2:
        note = st.selectbox("Select field", dict_notes[tips_type]) 

    show_notes(tips_type, note)

# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit | Demo by NhanDV 😎")