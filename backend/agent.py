from langchain_openai import ChatOpenAI

from langchain.tools import tool
from langsmith import Client

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.agents.agent import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent

from langchain_classic import hub

from rag import retrieve_context

from github_tool import (
    get_readme,
    get_commits,
    get_repo_details
)

# =========================
# LLM
# =========================

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# =========================
# TOOLS
# =========================

@tool
def rag_tool(query: str) -> str:
    """
    Use this for:
    - resume
    - skills
    - education
    - projects
    - experience
    """

    return retrieve_context(query)


@tool
def github_readme_tool(repo_name: str) -> str:
    """
    Use this for:
    - repo architecture
    - implementation
    - project explanation
    """

    return get_readme(repo_name)


@tool
def github_commits_tool(repo_name: str) -> str:
    """
    Use this for:
    - latest changes
    - commit history
    - recent updates
    """

    return get_commits(repo_name)


@tool
def github_repo_tool(repo_name: str) -> str:
    """
    Use this for:
    - tech stack
    - repo metadata
    - languages used
    """

    return get_repo_details(repo_name)

# =========================
# TOOL LIST
# =========================

tools = [
    rag_tool,
    github_readme_tool,
    github_commits_tool,
    github_repo_tool
]

# =========================
# PROMPT
# =========================
# Initialize the client
client = Client()

# Pull the latest version of the prompt

prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)

# =========================
# CREATE AGENT
# =========================

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# =========================
# EXECUTOR
# =========================

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
You are Brij Patel's AI representative.

Rules:
- Never hallucinate
- Never invent experience
- Stay grounded in available information
- If unsure, say you do not know
"""

# =========================
# ASK FUNCTION
# =========================

def ask_agent(question: str):

    final_input = f"""
{SYSTEM_PROMPT}

User Question:
{question}
"""

    response = agent_executor.invoke(
        {
            "input": final_input
        }
    )

    return response["output"]