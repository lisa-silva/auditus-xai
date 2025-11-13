# 1. Core Setup
import streamlit as st
import time 

# 2. Page Configuration and Title
st.set_page_config(
    page_title="AUDITUS: The Explainer Robot (XAI)",
    layout="centered",
)

st.title("🤖 AUDITUS: The Explainer Robot (XAI)")
st.subheader("Automating Justification Reports for Auditors.")

st.markdown("""
AUDITUS provides the crucial **Explainable AI (XAI)** layer. It translates a system finding (like ARCHON's non-compliant alert) into a clear, auditable, and human-readable justification.
""")

st.write("---") # Separator

# 3. Simulated XAI Logic (The Superpower)
def generate_xai_justification(rule, evidence, keywords):
    """
    Simulates generating a detailed, structured, auditor-friendly justification 
    based on the breach detected by ARCHON.
    """
    
    # 1. Identify the specific keyword that triggered the finding
    found_keywords = [
        keyword.strip() 
        for keyword in keywords.split(',') 
        if keyword.strip().lower() in evidence.lower()
    ]
    
    if not found_keywords:
        # Should not happen if ARCHON already found a breach, but for safety
        return "No specific breach term was found in the evidence. Cannot generate justification."
        
    # 2. Structure the justification (This is the XAI output)
    
    justification = f"""
    ### 📝 XAI Justification Report: Non-Compliance Analysis

    **Finding ID:** XAI-{int(time.time())}
    **Analysis Date:** {time.strftime("%Y-%m-%d")}
    
    ---

    #### 1. Detected Breach
    The evidence was flagged as **NON-COMPLIANT** by the detection engine.

    #### 2. Rationale & Explanation (The 'Why')
    The finding was triggered because the core document evidence contains the defined **Non-Compliant Keyword(s)**: **`{', '.join(found_keywords)}`**. 
    
    The system confirms this violates the primary objective of the Rule:

    > **Governing Rule:** "{rule}"
    
    #### 3. Specific Evidence Trace
    The presence of the term(s) **`{', '.join(found_keywords)}`** directly connects the document text to the regulatory breach threshold defined by the policy. This is a direct, auditable trace linking the input data to the non-compliant classification.
    
    #### 4. Recommended Action
    Immediate action is required to remediate the **unapproved payment**. Finance oversight is recommended.
    """
    return justification

# 4. Input Fields (Pre-filled to simulate receiving data from ARCHON)
with st.container(border=True):
    st.markdown("**1. Data Received from ARCHON Finding:**")
    
    rule_input = st.text_area(
        "Governing Rule:",
        value="All expense reports exceeding $500 must receive prior, written approval from a department head.",
        height=70,
        key="rule_a"
    )
    
    keyword_input = st.text_area(
        "Flagged Keywords:",
        value="unapproved payment, missed deadline, breach of conduct",
        height=50,
        key="keywords_a"
    )


    st.markdown("**2. Document Evidence:**")
    evidence_input = st.text_area(
        "Evidence Text (where the breach occurred):",
        value="The project manager submitted an expense report for $750. The associated email noted 'unapproved payment' for this transaction.",
        height=120,
        key="evidence_a"
    )

# 5. Action Button
if st.button("🧠 Generate XAI Justification Report", use_container_width=True, type="primary"):
    
    if not rule_input or not evidence_input or not keyword_input:
        st.warning("Please ensure all fields are populated with the breach data.")
        st.stop()
        
    # --- Simulation of complex XAI model runtime ---
    st.write("---")
    progress_bar = st.progress(0, text="Analyzing Decision Weights for XAI Report...")
    
    for percent_complete in range(100):
        time.sleep(0.01) # Extremely fast processing
        progress_bar.progress(percent_complete + 1, text=f"Generating structured justification report... {percent_complete + 1}% complete")
    
    progress_bar.empty()
    
    # --- Run XAI Generation Logic ---
    justification_report = generate_xai_justification(rule_input, evidence_input, keyword_input)
    
    # --- Display Results ---
    st.success("## ✨ XAI Report Generated Successfully")
    st.markdown(justification_report, unsafe_allow_html=True)
    
    st.write("---")
    st.caption("Time taken: 1.12 seconds. (Generating explainability reports is complex but fast for the AUDITUS engine.)")
