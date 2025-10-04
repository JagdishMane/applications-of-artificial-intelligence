Question : "Summarize the 10-Page rental Contract."

Response(Generic): "This document outlines the terms between a landlord and a tenant, including rent, duration ........"

To fine Tune the Model:
1. Take 500-1000 examples of rental agreements.
2. Lease summaries written by legal experts/
3. Fine-tune the base modeul using these examples.



LoRA Tuning: (Low-Rank Adaptation):

Full fine-tuning of models like LLama or GPT requires Billions of parameters, Huge GPU and Lots of time and money.


1. Technique to fine tune LLMs by using small number of parameters, instead of entire model.
2. LoRA freezes the orinial model weights.
3. Adds small trainable layers to specific parts of the model.
4. Only training those small layers. 
