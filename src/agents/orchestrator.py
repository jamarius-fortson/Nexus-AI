from typing import List, Dict, Any, Literal
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from src.agents.email_agent import create_email_agent
from src.agents.calendar_agent import create_calendar_agent
from src.agents.task_agent import create_task_agent
from src.utils.config import settings
import logging

logger = logging.getLogger(__name__)

class RouteDecision(BaseModel):
    """The decision of where to route the request."""
    destination: Literal["EMAIL", "CALENDAR", "TASK", "GENERAL"] = Field(description="The intelligence unit to handle the request.")
    reasoning: str = Field(description="The logic behind choosing this destination.")

class MasterOrchestrator:
    def __init__(self):
        # High-end reasoning engine
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro", 
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0
        )
        
        # Specialized Intelligence Units
        self.email_agent = create_email_agent()
        self.calendar_agent = create_calendar_agent()
        self.task_agent = create_task_agent()

    def route_request(self, user_input: str) -> str:
        """
        Orchestrates the routing of user requests using high-dimensional intent analysis.
        """
        router_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are the Nexus Master Orchestrator. 
            Your role is to analyze user requests and route them to the most qualified specialized unit.
            
            UNITS:
            - EMAIL: Handle Gmail communications, summaries, and information extraction from emails.
            - CALENDAR: Handle Google Calendar events, scheduling, and time management.
            - TASK: Handle Notion database entries, task creation, and organizational structure.
            - GENERAL: For requests that fall outside these domains or require meta-discussion.
            
            Be precise. If a request involves multiple units, pick the primary one or use 'GENERAL' to ask for clarification."""),
            ("user", "{input}")
        ])
        
        logger.info(f"Analyzing intent for input: {user_input[:50]}...")
        
        try:
            # Use structured output for reliable routing
            structured_llm = self.llm.with_structured_output(RouteDecision)
            chain = router_prompt | structured_llm
            decision = chain.invoke({"input": user_input})
            
            logger.info(f"Targeting {decision.destination} unit. Reason: {decision.reasoning}")
            
            if decision.destination == "EMAIL":
                return self.email_agent.invoke({"input": user_input})['output']
            elif decision.destination == "CALENDAR":
                return self.calendar_agent.invoke({"input": user_input})['output']
            elif decision.destination == "TASK":
                return self.task_agent.invoke({"input": user_input})['output']
            else:
                return self._handle_general(user_input)
                
        except Exception as e:
            logger.error(f"Routing failed: {e}")
            # Fallback to a safer logic if structured output fails
            return f"I encountered a synchronization error in my neural pathways. Please try rephrasing your request. (Error: {str(e)})"

    def _handle_general(self, user_input: str) -> str:
        """Handles requests that don't fit into specialized silos."""
        response = self.llm.invoke(f"You are Nexus, a helpful AI executive assistant. The user said: {user_input}. Provide a helpful, professional response.")
        return response.content

    def run_workflow(self, workflow_type: str, context: Dict[str, Any] = None):
        """
        Executes predefined multi-step workflows with high-level synthesis.
        """
        if workflow_type == "daily_summary":
            return self._run_daily_summary()
        return "Unrecognized workflow protocol."

    def _run_daily_summary(self):
        logger.info("Initiating Daily Briefing protocol...")
        
        # Parallel-ready execution (simulated here)
        events = self.calendar_agent.invoke({"input": "What are my events for today?"})['output']
        tasks = self.task_agent.invoke({"input": "List my high priority tasks."})['output']
        emails = self.email_agent.invoke({"input": "Summarize my top 3 unread emails."})['output']
        
        briefing_prompt = f"""
        Identity: Nexus Intelligence
        System State: Global Briefing Mode
        
        Contextual Inputs:
        - Temporal Grid (Calendar): {events}
        - Organizational Stack (Tasks): {tasks}
        - Communication Stream (Emails): {emails}
        
        Task: Synthesize a high-fidelity executive briefing. 
        Format:
        1. Momentum Check (Quick summary of the day's vibe)
        2. High-Priority Focus (What MUST happen)
        3. Communication Digest (Key items from inbox)
        4. Tactical Advice (One tip for hyper-productivity based on the data)
        """
        
        summary = self.llm.invoke(briefing_prompt).content
        return summary
