# # # # # # # # # # # from dotenv import load_dotenv

# # # # # # # # # # # from livekit import agents, rtc
# # # # # # # # # # # from livekit.agents import AgentServer, AgentSession, Agent, room_io
# # # # # # # # # # # from livekit.plugins import (
# # # # # # # # # # #     noise_cancellation,
# # # # # # # # # # # )
# # # # # # # # # # # from livekit.plugins import google
# # # # # # # # # # # from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
# # # # # # # # # # # load_dotenv()

# # # # # # # # # # # class Assistant(Agent):
# # # # # # # # # # #     def __init__(self) -> None:
# # # # # # # # # # #         super().__init__(instructions=AGENT_INSTRUCTION)

# # # # # # # # # # # async def entrypoint(ctx: agents.JobContext):
# # # # # # # # # # #     session = AgentSession(
# # # # # # # # # # #         llm=google.beta.realtime.RealtimeModel(
# # # # # # # # # # #             voice="charon"
# # # # # # # # # # #         )
# # # # # # # # # # #     )

# # # # # # # # # # #     await session.start(
# # # # # # # # # # #         room=ctx.room,
# # # # # # # # # # #         agent=Assistant(),
# # # # # # # # # # #         room_input_options=room_io.RoomInputOptions(
# # # # # # # # # # #             noise_cancellation=noise_cancellation.BVC(),
# # # # # # # # # # #         ),
        
# # # # # # # # # # #     )
# # # # # # # # # # #     await ctx.connect()

# # # # # # # # # # #     await session.generate_reply(
# # # # # # # # # # #         instructions=SESSION_INSTRUCTION
# # # # # # # # # # #     )


# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))


# # # # # # # import logging

# # # # # # # # Configure logging
# # # # # # # logging.basicConfig(
# # # # # # #     level=logging.INFO,  # Use DEBUG for more details
# # # # # # #     format="%(levelname)s %(name)s - %(message)s"
# # # # # # # )

# # # # # # # # Optional: reduce verbose logs from noisy packages
# # # # # # # logging.getLogger("aiohttp").setLevel(logging.WARNING)
# # # # # # # logging.getLogger("opentelemetry").setLevel(logging.WARNING)


# # # # # # # from dotenv import load_dotenv
# # # # # # # from livekit.plugins import noise_cancellation
# # # # # # # from livekit import agents
# # # # # # # from livekit.agents import AgentSession, Agent, room_io
# # # # # # # from livekit.plugins import google
# # # # # # # from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
# # # # # # # load_dotenv()

# # # # # # # class Assistant(Agent):
# # # # # # #     def __init__(self) -> None:
# # # # # # #         super().__init__(instructions=AGENT_INSTRUCTION)

# # # # # # # async def entrypoint(ctx: agents.JobContext):
# # # # # # #     session = AgentSession(
# # # # # # #         llm=google.beta.realtime.RealtimeModel(
# # # # # # #             voice="charon"
# # # # # # #         )
# # # # # # #     )

# # # # # # #     await session.start(
# # # # # # #         room=ctx.room,
# # # # # # #         agent=Assistant(),
# # # # # # #         room_input_options=room_io.RoomInputOptions(
# # # # # # #             noise_cancellation=noise_cancellation.BVC(),
# # # # # # #             min_volume=0.02  # ignore very quiet background noises
# # # # # # #         ),
# # # # # # #     )
# # # # # # #     await ctx.connect()

# # # # # # #     # await session.generate_reply(
# # # # # # #     #     instructions=SESSION_INSTRUCTION

# # # # # # #     await session.say(SESSION_INSTRUCTION.strip()
# # # # # # #     )


# # # # # # # if __name__ == "__main__":
# # # # # # #     agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))





# # # # # # import logging
# # # # # # from dotenv import load_dotenv
# # # # # # from livekit.plugins import noise_cancellation
# # # # # # from livekit import agents
# # # # # # from livekit.agents import AgentSession, Agent, room_io
# # # # # # from livekit.plugins import google
# # # # # # from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION

# # # # # # # Logging setup
# # # # # # logging.basicConfig(
# # # # # #     level=logging.INFO,
# # # # # #     format="%(levelname)s %(name)s - %(message)s"
# # # # # # )
# # # # # # logging.getLogger("aiohttp").setLevel(logging.WARNING)
# # # # # # logging.getLogger("opentelemetry").setLevel(logging.WARNING)

# # # # # # load_dotenv()

# # # # # # class Assistant(Agent):
# # # # # #     def __init__(self) -> None:
# # # # # #         super().__init__(instructions=AGENT_INSTRUCTION)

# # # # # # async def entrypoint(ctx: agents.JobContext):
# # # # # #     session = AgentSession(
# # # # # #         llm=google.beta.realtime.RealtimeModel(
# # # # # #             voice="charon"
# # # # # #         )
# # # # # #     )

# # # # # #     await session.start(
# # # # # #         room=ctx.room,
# # # # # #         agent=Assistant(),
# # # # # #         room_input_options=room_io.RoomInputOptions(
# # # # # #             noise_cancellation=noise_cancellation.BVC(),
# # # # # #         ),
# # # # # #     )
# # # # # #     await ctx.connect()

# # # # # #     # Say greeting
# # # # # #     await session.generate_reply(SESSION_INSTRUCTION.strip())


# # # # # # if __name__ == "__main__":
# # # # # #     agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))





# # # # # import logging
# # # # # from dotenv import load_dotenv

# # # # # from livekit import agents, rtc
# # # # # from livekit.agents import Agent, AgentSession, room_io
# # # # # from livekit.plugins import google, noise_cancellation

# # # # # from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION

# # # # # load_dotenv()

# # # # # # -----------------------------------------
# # # # # # Logging (keep it simple)
# # # # # # -----------------------------------------
# # # # # logging.basicConfig(
# # # # #     level=logging.INFO,
# # # # #     format="%(levelname)s %(name)s - %(message)s"
# # # # # )


# # # # # # -----------------------------------------
# # # # # # AGENT
# # # # # # -----------------------------------------
# # # # # class Size24Assistant(Agent):
# # # # #     def __init__(self):
# # # # #         super().__init__(instructions=AGENT_INSTRUCTION)


# # # # # # -----------------------------------------
# # # # # # ENTRYPOINT
# # # # # # -----------------------------------------
# # # # # async def entrypoint(ctx: agents.JobContext):

# # # # #     # The REAL-TIME VOICE MODEL (Google Gemini Realtime)
# # # # #     session = AgentSession(
# # # # #         llm=google.beta.realtime.RealtimeModel(
# # # # #             voice="charon",        # TTS voice     # <-- IMPORTANT
# # # # #         )
# # # # #     )

# # # # #     # Start the session inside a LiveKit Room
# # # # #     await session.start(
# # # # #         room=ctx.room,
# # # # #         agent=Size24Assistant(),
# # # # #         # Mic → Noise Cancel → AI
# # # # #         room_input_options=room_io.RoomInputOptions(
# # # # #             noise_cancellation=noise_cancellation.BVC(),
# # # # #         ),
# # # # #     )

# # # # #     await ctx.connect()

# # # # #     # -----------------------------------------
# # # # #     # BOT SHOULD TALK FIRST
# # # # #     # -----------------------------------------
# # # # #     await session.say("Welcome to Size24! How may I help you today?")

# # # # #     # Load session rules
# # # # #     await session.update_instructions(SESSION_INSTRUCTION)

# # # # #     # Always keep listening & replying
# # # # #     while True:
# # # # #         await session.generate_reply()


# # # # # # -----------------------------------------
# # # # # # WORKER
# # # # # # -----------------------------------------
# # # # # if __name__ == "__main__":
# # # # #     agents.cli.run_app(
# # # # #         agents.WorkerOptions(
# # # # #             entrypoint_fnc=entrypoint
# # # # #         )
# # # # #     )





# # # # import logging
# # # # from dotenv import load_dotenv

# # # # from livekit import agents, rtc
# # # # from livekit.agents import Agent, AgentSession, room_io
# # # # from livekit.plugins import google, noise_cancellation

# # # # from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION

# # # # load_dotenv()

# # # # # -----------------------------------------
# # # # # Logging
# # # # # -----------------------------------------
# # # # logging.basicConfig(
# # # #     level=logging.INFO,
# # # #     format="%(levelname)s %(name)s - %(message)s"
# # # # )

# # # # logging.getLogger("aiohttp").setLevel(logging.WARNING)
# # # # logging.getLogger("opentelemetry").setLevel(logging.WARNING)

# # # # # -----------------------------------------
# # # # # Agent
# # # # # -----------------------------------------
# # # # class Assistant(Agent):
# # # #     def __init__(self):
# # # #         super().__init__(instructions=AGENT_INSTRUCTION)


# # # # # -----------------------------------------
# # # # # Entry point
# # # # # -----------------------------------------
# # # # async def entrypoint(ctx: agents.JobContext):

# # # #     session = AgentSession(
# # # #         llm=google.beta.realtime.RealtimeModel(
# # # #             voice="charon"  # TTS voice
# # # #         )
# # # #     )

# # # #     # Start session with mic input and noise cancellation
# # # #     await session.start(
# # # #         room=ctx.room,
# # # #         agent=Assistant(),
# # # #         room_input_options=room_io.RoomInputOptions(
# # # #             noise_cancellation=noise_cancellation.BVC(),
# # # #             # min_volume=0.02  # Uncomment if your SDK supports it
# # # #         ),
# # # #     )

# # # #     await ctx.connect()

# # # #     # Bot speaks first
# # # #     await session.say("Welcome to Size24! How may I help you today?")

# # # #     # Load session instructions (rules)
# # # #     await session.update_instructions(SESSION_INSTRUCTION)

# # # #     # Continuous listening & replying
# # # #     while True:
# # # #         await session.generate_reply()


# # # # # -----------------------------------------
# # # # # Worker
# # # # # -----------------------------------------
# # # # if __name__ == "__main__":
# # # #     agents.cli.run_app(
# # # #         agents.WorkerOptions(
# # # #             entrypoint_fnc=entrypoint
# # # #         )
# # # #     )

from dotenv import load_dotenv
from livekit import agents, rtc
from livekit.agents import AgentServer, AgentSession, Agent, room_io
from livekit.plugins import (
    noise_cancellation,
)
from livekit.plugins import google
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
load_dotenv()

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTION)

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="charon"
        )
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=room_io.RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
        
    )
    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
#



