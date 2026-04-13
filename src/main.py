import logging
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import settings
from src.agents.orchestrator import MasterOrchestrator

# Configure rich console
console = Console()

logging.basicConfig(
    level=settings.LOG_LEVEL, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("nexus_ai.log"), logging.StreamHandler(sys.stdout)] if settings.LOG_LEVEL == "DEBUG" else [logging.FileHandler("nexus_ai.log")]
)
logger = logging.getLogger("NexusAI")

def welcome_banner():
    console.print(Panel(
        Text("🌌 NEXUS AI: THE AUTONOMOUS DIGITAL EXECUTIVE", style="bold magenta", justify="center"),
        subtitle="Quantum-Level Productivity Orchestration",
        border_style="cyan"
    ))

def main():
    welcome_banner()
    
    with console.status("[bold green]Initializing Nexus Core Intelligence...") as status:
        try:
            orchestrator = MasterOrchestrator()
            console.print("[bold blue]✓ Systems at 100%. Neural pathways established.[/bold blue]")
        except Exception as e:
            console.print(f"[bold red]CRITICAL FAILURE: {e}[/bold red]")
            return

    console.print("\n[bold yellow]Nexus is ready. How can I reclaim your time today?[/bold yellow]")
    
    while True:
        try:
            user_input = console.input("\n[bold cyan]λ Nexus > [/bold cyan]")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                console.print("[bold magenta]Nexus signing off. Stay productive.[/bold magenta]")
                break
            
            if not user_input.strip():
                continue

            with console.status("[bold green]Synthesizing intelligence...") as status:
                response = orchestrator.route_request(user_input)
            
            console.print(Panel(response, title="[bold magenta]Nexus Response[/bold magenta]", border_style="green"))
            
        except KeyboardInterrupt:
            console.print("\n[bold magenta]Nexus signing off. Stay productive.[/bold magenta]")
            break
        except Exception as e:
            console.print(f"[bold red]An error occurred: {e}[/bold red]")
            logger.error(f"Error in main loop: {e}", exc_info=True)

if __name__ == "__main__":
    main()
