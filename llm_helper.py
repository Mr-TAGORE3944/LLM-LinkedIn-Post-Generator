from langchain_groq import ChatGroq
import os
# from dotenv import load_dotenv

# load_dotenv()
llm = ChatGroq(groq_api_key="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", model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





