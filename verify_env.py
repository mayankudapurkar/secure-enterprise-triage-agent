import sys
import importlib.metadata

def main():
    print("--- Environment Verification ---")
    print(f"Python Version: {sys.version}")
    print(f"Executable: {sys.executable}")
    
    # Verify package installation versions
    packages = ["google-adk", "google-agents-cli"]
    for pkg in packages:
        try:
            ver = importlib.metadata.version(pkg)
            print(f"Package '{pkg}' version: {ver}")
        except importlib.metadata.PackageNotFoundError:
            print(f"Package '{pkg}' is NOT installed!")
            sys.exit(1)
            
    # Verify importing google.adk classes
    print("\nAttempting imports from `google.adk`...")
    try:
        from google.adk import Agent, Workflow
        print("Successfully imported Agent and Workflow from google.adk")
        
        # Test basic instantiation
        agent_a = Agent(name="verifier_agent_a", instruction="Test instruction")
        agent_b = Agent(name="verifier_agent_b", instruction="Another instruction")
        
        # Check Workflow setup
        flow = Workflow(
            name="test_verification_workflow",
            edges=[
                ("START", agent_a, agent_b)
            ]
        )
        print("Successfully defined verification graph Workflow with Agent nodes!")
        print(f"Workflow: {flow.name}")
        print("Workflow Edges:")
        for edge in flow.edges:
            print(f"  {edge}")
            
    except Exception as e:
        print(f"Error during ADK 2.0 import or instantiation: {e}")
        sys.exit(1)
        
    print("\nEnvironment is ready for ADK 2.0 graph workflows!")

if __name__ == "__main__":
    main()
