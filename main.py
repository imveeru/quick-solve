import streamlit as st

st.set_page_config(
    page_title="Quick Solve",
    page_icon="📝",
    # initial_sidebar_state="expanded",
)

#hide streamlit default
hide_st_style ='''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("📝Quick Solve")

option = st.radio(
    "Choose the type of question.",
    ('General Math', 'Solving Equations', 'Word Problems'),horizontal=True)

query=st.text_input("Type your question here.")

from langchain.llms import VertexAI
from langchain import LLMMathChain
# from langchain.chains import PALChain
from langchain.chains.llm_symbolic_math.base import LLMSymbolicMathChain

llm = VertexAI()
llm_math = LLMMathChain.from_llm(llm, verbose=True)
llm_symbolic_math = LLMSymbolicMathChain.from_llm(llm)
# pal_chain = PALChain.from_math_prompt(llm, verbose=True)

if query:
    with st.spinner("Working it out..."):
        if option=="General Math":
            res=llm_math.run(query)
        elif option=="Solving Equations":
            res=llm_symbolic_math.run(query)
        elif option=="Word Problems":
            res=llm(f'''Assume yourself as a mathematics professor and answer the given word problem.
                        Question: {query}''')
    
        st.markdown(res)

# question = "Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?"
# res=pal_chain.run(question)