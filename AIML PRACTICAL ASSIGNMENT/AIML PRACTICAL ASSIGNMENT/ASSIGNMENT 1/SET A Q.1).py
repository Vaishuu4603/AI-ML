# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:47:42 2025

@author: jayes
"""

# Simple Chatbot Program

def chatbot(user):
    user = user.lower()
    
    if "hello" in user:
        return "Hello! How can I assist you today?"
    elif "bye" in user:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand that."

# Chat loop
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    print("Chatbot:", chatbot(user))
