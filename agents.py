from crewai import Agent
from textwrap import dedent
from search_tools import SearchTools
from calculator_tools import CalculatorTools
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
A = os.getenv('Llama_API_KEY')
'''

Creating Agents Cheat Sheet
- Think like a boss. Work bakwards from the goal and think which employee you need to 
  hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to. 
  Build a top down structure of the crew.

Goal: 
- Create a 7-day travel itinerary with me detailed per-day plans, 
  including budget, packing suggestions, and safety tips.

Captain/ Manager/ Boss:
- Expert Travel Agent

Employees/ Experts to hire:
- City Selection Expert
- Local Tour Guide

Notes:
- Agents should be result driven and have a clear goal in mind.
- Role is their job title.
- Goals should be actionable and specific.
- Backstory should be their resume.


'''


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        #self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, api_key=api_)
        self.Groq = ChatGroq(api_key=A,model = "mixtral-8x7b-32768")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                            Expert in travel planning and logistics. I have decades of experience
                            making travel iteneraries.
                            """),
            goal=dedent(f"""
                            Create a 7-day travel itinerary with detailed per-day plans,
                            including budget, packing suggestions, and safety tips.
                            """),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            verbose=True,
            llm=self.Groq,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f""" 
                            Expert at analyzing travel data to pick ideal destinations.
                            """),
            goal=dedent(f"""
                        Select the best cities based on weather, season, prices, and traveler interests.
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.Groq,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f""" 
                             Knowledgeable local guide with extensive information about the city,
                             it's attraction and customs.
                            """),
            goal=dedent(f"""
                        Provide the best insights about the selected city.
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.Groq,
        )
