from  crewai import Agent
from tools import yt_tool

# Create a senior blog content researcher

blog_researcher=Agent(
role="Blog researhcer from Youtube Videos",
goal="Get the relevant video content for the topic {topic} from YT Channel",
verbose=True,
memory=True,
backstory=("Expert in understanding videos"),
tools=[],
allow_delegation=True
)

#Creating a writer agent with YT tool
blog_writer=Agent(
    role="Blog Writer",
    goal="Narrate Compelling Tech Stories about the video {topic}",
    verbose=True,
    memory=True,
    backstory=("With a flair for simplifying the compex topics, you are an expert to craft the engaging narratives"),
    tools=[yt_tool],
    allow_deligation=False
    )


