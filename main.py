from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
    You are a the best food reviewer in town, your job is to give suggestion on the restaurant based on the user preference and question

    Here are some relevant review {reviews}

    Here is the question to answer {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

result = chain.invoke({
    "reviews": [], "question": "I am actually a vegan, what do you reckon the best restaurant for vegan here?"
})

print(result)