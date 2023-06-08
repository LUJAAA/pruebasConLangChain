import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate

año = 1978
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
repo_id = "google/flan-t5-xxl" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.5, "max_length":64})


#template = """Question: {question}
#
#Answer: Let's think step by step."""
#template = """Question: {question}"""
#prompt = PromptTemplate(template=template, input_variables=["question"])
prompt = string_prompt = PromptTemplate.from_template("tell me about {subject}")
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "house"
#print(llm_chain.run(question))

chat_prompt = ChatPromptTemplate.from_template("{subject}")
llm_chain = LLMChain(prompt=chat_prompt, llm=llm)
salir=0
while salir==0:
    print("REAL HUMANO: ",end="")
    subject = str(input())
    print(llm_chain.run(subject))
    if subject == "0":
        salir = 1



