- Quantization - Model weights, speeding up inferences

from transformers import AutoModelForCausalLM, BitsAndBytestConfig

quant_config = BitsAndBytesConfig(local_in_4bit=True, bnb_4bit_quant_type="nf4")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct, quantization_config=quant_config)

|Type|Size|Precision|Use Case|
!---!---|---|---|
|float32|Largest|High|Full Precision(training)|
|float16|Medium|Moderate| GPU accelerated inference|
|int8|Small|Good | Faster on CPUs and GPUs|
|4-bit| Tiny| Acceptable | Extreme compression (QLoRA)|