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

while True:
    print("--------------------AI Agent--------------------------")
    question = input("Ask your question (q to quit): ")
    print("------------------------------------------------------")
    if question == "q":
        break

    result = chain.invoke({
        "reviews": [], "question": question
    })

print(result)