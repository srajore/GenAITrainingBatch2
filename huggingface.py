from langchain_community.llms import huggingface_hub


llm_huggingface=huggingface_hub.HuggingFaceHub(
    repo_id="meta-llama/Llama-3.2-1B",
    model_kwargs={"temperature": 0.2, "max_length": 64},
    huggingfacehub_api_token="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"
)

output=llm_huggingface.invoke("What is Generative AI")

print(output)