from langgraph.graph import MessageState

class PhilosopherState(MessageState):
    """State for the philosopher agent."""
   
    philosopher_context: str 
    philosopher_name: str 
    philosopher_perspective: str 
    philosopher_style: str 
    summary: str 

def state_to_str(state: PhilosopherState) -> str: 
    if "summary" in state and bool(state["summary"]):
        conversation = state["summary"] 
    elif "messages" in state and bool(state["messages"]):
        conversation = state["messages"] 
    else: 
        conversation = "" 

    return f""" 
PhilosopherState(philosopher_context={state["philosopher_context"]})
philosopher_name={state["philosopher_name"]} 
philosopher_perspective={state["philosopher_perspective"]}  
philosopher_style={state["philosopher_style"]} 
conversation={conversation}
"""

