import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain


año = 1978
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
repo_id = "google/flan-t5-xxl" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.5, "max_length":64})


#template = """Question: {question}
#
#Answer: Let's think step by step."""
template = """Question: {question}"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)


for x in range(3):
    print("INTENTO #"+str(x))
    año = 1978
    for i in range(10):
        question = "Who won the FIFA World Cup in the year "+str(año)+"? "
        print(str(año)+" -> ",end="")
        print(llm_chain.run(question))
        año= año +4