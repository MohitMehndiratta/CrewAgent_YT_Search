from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


#Research Task
research_task=Task(
    description=(
        "Identify the video {topic}."
        "Get the detailed information about the video from the youtube channel."
    ),
    expected_output="A Comprehensive 3 paragraphs long report based on the {topic} of the video content"&
    "from the youtube video channel"
    ,
    agent=blog_researcher,
    tools=[yt_tool]
                   )

# Writing task with language model configuration
write_task=Task(
    description=("get the info from the youtube channel on the {topic}"),
    agent=blog_writer,
    expected_output="summarize the related info from the youtube channel on the topic-{topic}",
    tools=[yt_tool],
    async_execution=False,
    output_file='new-blog-post.md'
    )