#!/usr/bin/env python

from demo_1.crew import Demo1

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI agents for brain computer interfaces with writing code',
    }

    try:
        Demo1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()