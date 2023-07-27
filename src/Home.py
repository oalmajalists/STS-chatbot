import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="STS | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

 

    st.write("**Webiste:** https://STSArabia.com")
    st.write("**Enhanced by Product Development Team**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>STS-BOT, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm STS-BOT ,a project from STS AI Taskforce , an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript with more coming soon enshallah! 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#STS's Pages
st.subheader("🚀 STS's Pages")
st.write("""
- **STS-Doc**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (can't process the whole file just index useful parts(max 4) for respond to the user ) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) + (soon) Summarize data
- **STS-Sheet** (beta): Chat on tabular data (CSV) | for precise information | can process the whole file (with python code) | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation (experimental)
- **STS-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)

""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**STS-BOT is under regular development by STS AI Task Force.**
""", unsafe_allow_html=True)





