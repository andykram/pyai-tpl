"""CLI REPL for Trajnor using pydantic-ai."""

from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel


def create_agent() -> Agent:
    """Create and configure the pydantic-ai agent.
    
    Returns:
        Agent: Configured pydantic-ai agent
    """
    # Using TestModel for a simple toy example that doesn't require API keys
    # In production, you would use a real model like OpenAI, Anthropic, etc.
    agent = Agent(
        model=TestModel(),
    )
    return agent


def run_repl():
    """Run the interactive REPL."""
    print("Welcome to Trajnor REPL!")
    print("Type 'exit', 'quit', or press Ctrl+C to exit.")
    print("-" * 50)
    
    agent = create_agent()
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            # Run the agent with the user input
            result = agent.run_sync(user_input)
            print(f"Agent: {result.output}")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Main entry point for the CLI."""
    run_repl()


if __name__ == "__main__":
    main()
