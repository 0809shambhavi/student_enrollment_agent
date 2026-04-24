# main.py

from agent import EnrollmentAgent
from memory import Memory

memory = Memory()
agent = EnrollmentAgent(memory)

conversation = [
    "Hi, what programs do you offer in computer science?",
    "What's the application deadline for that?",
    "I already applied. My ID is APP-1042. What's my status?",
    "Can I get a fee waiver?",
    "What documents do I still need to submit?"
]

for i, msg in enumerate(conversation):
    print(f"\nTurn {i+1} USER: {msg}")
    response = agent.handle(msg)
    print(f"Turn {i+1} AGENT: {response}")