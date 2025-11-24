"""
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            \"\"\"
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            \"\"\",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
"""


# main.py
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Dial
from livekit.agents import AgentSession
from livekit.plugins import google, noise_cancellation
from agent import Assistant  # your agent.py class
import asyncio

app = Flask(__name__)

# Keep track of active sessions
active_sessions = {}

@app.route("/twilio-voice", methods=["POST"])
def twilio_voice():
    from_number = request.form.get("From")
    call_sid = request.form.get("CallSid")

    # Twilio response
    resp = VoiceResponse()

    # Optional: if user wants human, redirect
    # For example, press 1 to speak with human
    if request.form.get("Digits") == "1":
        dial = Dial()
        dial.number("+919876543210")  # Your live executive number
        resp.append(dial)
        return Response(str(resp), mimetype="text/xml")

    # Otherwise, connect to agent
    resp.say("Connecting you to Size24 support...")
    resp.pause(length=1)

    # Start background async session
    asyncio.create_task(start_agent_session(call_sid, from_number))

    return Response(str(resp), mimetype="text/xml")


async def start_agent_session(call_sid, from_number):
    # Create LiveKit agent session for this caller
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="charon"
        )
    )
    agent = Assistant()

    # Connect session (LiveKit room or audio forwarding logic)
    await session.start(
        room=None,  # Can be a dynamic room per call
        agent=agent,
        room_input_options=noise_cancellation.BVC()
    )

    # Optional: Store session for reference
    active_sessions[call_sid] = session

    # Send initial greeting
    await session.generate_reply(
        instructions="Hello! This is Size24 support. How may I help you today?"
    )

# Run Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
