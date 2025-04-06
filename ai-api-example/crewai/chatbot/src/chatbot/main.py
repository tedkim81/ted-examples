#!/usr/bin/env python
import warnings

from datetime import datetime

from chatbot.crew import Chatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    while True:
        user_message = input("사용자: ")
        if user_message.lower() in ['quit', 'exit', 'bye']:
            break
            
        inputs = {
            'user_message': user_message
        }
        
        try:
            response = Chatbot().crew().kickoff(inputs=inputs)
            print(f"챗봇: {response}")
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
