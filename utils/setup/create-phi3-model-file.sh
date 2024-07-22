#!/bin/bash

# Variables
model_name="phi3"
custom_model_name="crewai-phi3"

# Get the base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./phi3Modelfile