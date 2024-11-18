from langchain_huggingface import HuggingFaceEndpoint

# Initialize the HuggingFace model endpoint with parameters specified directly
llm_huggingface = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    temperature=1.0,  # Specify temperature directly
    max_length=64,    # Specify max_length directly
    huggingfacehub_api_token="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"
)

# Invoke the model with a prompt
output = llm_huggingface.invoke("What is Generative AI")

# Print the output
print(output)