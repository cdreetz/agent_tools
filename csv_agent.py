from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent


import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="My Terminal Tool")
    parser.add_argument("file_path", help="Path to the file")
    # Add more arguments if needed
    return parser.parse_args()

def run_tool(file_path):
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        file_path,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    print("Agent initialized. Enter 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    args = parse_arguments()
    run_tool(args.file_path)


