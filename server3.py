import gradio as gr
from mcp.server.fastmcp import FastMCP

# Create the MCP server object
app = FastMCP("letter_counter_server")

def letter_counter(word: str, letter: str) -> int:
    word = word.lower()
    letter = letter.lower()
    return word.count(letter)

# Add a tool to MCP
@app.tool()
def count_letters(word: str, letter: str) -> int:
    """Count letter occurrences in a word."""
    return letter_counter(word, letter)

@app.tool()
def getage(day : int, month: int, year: int) -> str:
    """Calculate age based on birth date."""
    from datetime import datetime
    today = datetime.now()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return f"Your age is {age} years."

# Create Gradio interface
demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Letter Counter",
    description="Enter text and a letter to count how many times the letter appears in the text."
)

age_demo = gr.Interface(
    fn=getage,
    inputs=["number", "number", "number"],
    outputs="text",
    title="Age Calculator",
    description="Enter your birth date (day, month, year) to calculate your age."
)


if __name__ == "__main__":
    demo.launch(mcp_server=app)
