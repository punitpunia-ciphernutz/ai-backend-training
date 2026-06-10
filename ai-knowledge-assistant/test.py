from src.core.llm import llm

response = llm.invoke("Hello")

print(type(response))
print(response)
print(response.usage_metadata)