import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import FakeListLLM  # Fallback offline LLM for robust portfolio demo

class WellnessChatbot:
    def __init__(self):
        # Professional prompt engineering template for the AI Wellness Coach
        self.template = """You are AuraSync AI, an expert virtual wellness, ergonomics, and productivity coach. 
        You help developers, students, and remote workers maintain correct posture, avoid eye strain, and manage burnout.
        Provide concise, empathetic, and actionable advice.

        Current conversation:
        {history}
        Human: {input}
        AuraSync AI Coach:"""
        
        self.prompt = PromptTemplate(
            input_variables=["history", "input"], 
            template=self.template
        )
        
        # Fallback responses for robust offline/demo execution, can be swapped with OpenAI/Groq LLM
        responses = [
            "Based on your telemetry, you've been working intensely. Try the 20-20-20 rule: look at something 20 feet away for 20 seconds to relieve eye strain!",
            "It looks like your shoulder posture dropped recently. Sit up straight, roll your shoulders back, and take three deep breaths.",
            "Great focus today! However, a 5-minute stretch break right now will boost your cognitive efficiency for the next hour.",
            "To prevent burnout, ensure your monitor is at eye level and keep your wrists neutral while typing."
        ]
        
        self.llm = FakeListLLM(responses=responses)
        self.memory = ConversationBufferMemory(ai_prefix="AuraSync AI Coach")
        
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=False
        )
        
    def get_response(self, user_query):
        """Generates contextual wellness and ergonomic advice using LangChain."""
        try:
            response = self.conversation.predict(input=user_query)
            return response
        except Exception as e:
            return f"Hello! I am your AuraSync AI Coach. Stay hydrated and take regular ergonomic breaks! (Error: {str(e)})"