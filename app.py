from transformers import pipeline
from transformers import Conversation

import gradio as gr

chatbot = pipeline(model="facebook/blenderbot-400M-distill")