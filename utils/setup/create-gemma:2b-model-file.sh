#!/bin/bash

# Variables
model_name="gemma:2b"
custom_model_name="crewai-gemma:2b"

# Get the base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./gemma:2bModelfile