"""
Agent Interaction Workflow - Simplified Implementation
Based on the workflow diagram for processing employer documents
"""

import asyncio
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class Decision(Enum):
    """Final decision outcomes"""
    SUBMISSION_READY = "✓ Submission Ready"
    BLOCK_REQUIRED_UPLOADS = "X Block + Required Uploads"


@dataclass
class Document:
    """Represents uploaded documents"""
    content: str
    document_type: str


@dataclass
class ProcessingResult:
    """Result from agent processing"""
    agent_name: str
    is_complete: bool
    is_consistent: bool
    missing_fields: List[str]
    data: Dict


class JobSpecialtyAgent:
    """Processes job and specialty information"""
    
    def process(self, documents: List[Document]) -> ProcessingResult:
        """Process job and specialty related documents"""
        print(f"[Job & Specialty Agent] Processing {len(documents)} documents...")
        
        # Simulate processing
        job_data = {}
        for doc in documents:
            if "job" in doc.document_type.lower() or "specialty" in doc.document_type.lower():
                job_data["job_title"] = "Extracted from document"
                job_data["specialty"] = "Extracted from document"
        
        is_complete = len(job_data) >= 2
        missing = ["job_title", "specialty"] if not is_complete else []
        
        return ProcessingResult(
            agent_name="Job & Specialty Agent",
            is_complete=is_complete,
            is_consistent=True,
            missing_fields=missing,
            data=job_data
        )


class BeneficiaryStatusAgent:
    """Processes beneficiary and status information"""
    
    def process(self, documents: List[Document]) -> ProcessingResult:
        """Process beneficiary and status related documents"""
        print(f"[Beneficiary & Status Agent] Processing {len(documents)} documents...")
        
        # Simulate processing
        beneficiary_data = {}
        for doc in documents:
            if "beneficiary" in doc.document_type.lower() or "status" in doc.document_type.lower():
                beneficiary_data["beneficiary_name"] = "Extracted from document"
                beneficiary_data["status"] = "Extracted from document"
        
        is_complete = len(beneficiary_data) >= 2
        missing = ["beneficiary_name", "status"] if not is_complete else []
        
        return ProcessingResult(
            agent_name="Beneficiary & Status Agent",
            is_complete=is_complete,
            is_consistent=True,
            missing_fields=missing,
            data=beneficiary_data
        )


class EmployerControlCompanyAgent:
    """Processes employer control and company information"""
    
    def process(self, documents: List[Document]) -> ProcessingResult:
        """Process employer control and company related documents"""
        print(f"[Employer Control & Company Agent] Processing {len(documents)} documents...")
        
        # Simulate processing
        employer_data = {}
        for doc in documents:
            if "employer" in doc.document_type.lower() or "company" in doc.document_type.lower():
                employer_data["company_name"] = "Extracted from document"
                employer_data["control_number"] = "Extracted from document"
        
        is_complete = len(employer_data) >= 2
        missing = ["company_name", "control_number"] if not is_complete else []
        
        return ProcessingResult(
            agent_name="Employer Control & Company Agent",
            is_complete=is_complete,
            is_consistent=True,
            missing_fields=missing,
            data=employer_data
        )


class CompletenessConsistencyAgent:
    """Checks completeness and consistency of all processing results"""
    
    def check(self, results: List[ProcessingResult]) -> Dict:
        """Check completeness and consistency across all agent results"""
        print(f"[Completeness & Consistency Agent] Checking {len(results)} agent results...")
        
        all_complete = all(r.is_complete for r in results)
        all_consistent = all(r.is_consistent for r in results)
        
        all_missing_fields = []
        for result in results:
            all_missing_fields.extend(result.missing_fields)
        
        return {
            "all_complete": all_complete,
            "all_consistent": all_consistent,
            "missing_fields": all_missing_fields,
            "agent_results": results
        }


class ControlOrchestratorAgent:
    """Main orchestrator that coordinates the workflow"""
    
    def __init__(self):
        self.job_agent = JobSpecialtyAgent()
        self.beneficiary_agent = BeneficiaryStatusAgent()
        self.employer_agent = EmployerControlCompanyAgent()
        self.consistency_agent = CompletenessConsistencyAgent()
    
    async def process_documents(self, documents: List[Document]) -> Decision:
        """
        Main workflow:
        1. Receive documents
        2. Process in parallel with specialized agents
        3. Check completeness and consistency
        4. Make final decision
        """
        print("\n" + "="*60)
        print("WORKFLOW STARTED: Employer Uploads Documents")
        print("="*60)
        
        # Step 1: Orchestrator receives documents
        print(f"\n[Control Orchestrator] Received {len(documents)} documents")
        
        # Step 2: Parallel processing by specialized agents
        print("\n[Control Orchestrator] Dispatching to specialized agents (parallel processing)...")
        
        # Run agents in parallel (simulated with asyncio)
        loop = asyncio.get_event_loop()
        results = await asyncio.gather(
            loop.run_in_executor(None, self.job_agent.process, documents),
            loop.run_in_executor(None, self.beneficiary_agent.process, documents),
            loop.run_in_executor(None, self.employer_agent.process, documents)
        )
        
        print("\n[Control Orchestrator] All specialized agents completed processing")
        
        # Step 3: Completeness & Consistency check
        print("\n[Control Orchestrator] Sending results to Completeness & Consistency Agent...")
        consistency_check = self.consistency_agent.check(results)
        
        # Step 4: Final decision
        print("\n[Control Orchestrator] Making final decision...")
        decision = self._make_decision(consistency_check)
        
        print("\n" + "="*60)
        print(f"FINAL DECISION: {decision.value}")
        print("="*60 + "\n")
        
        return decision
    
    def _make_decision(self, consistency_check: Dict) -> Decision:
        """Make final decision based on completeness and consistency"""
        if consistency_check["all_complete"] and consistency_check["all_consistent"]:
            return Decision.SUBMISSION_READY
        else:
            missing = ", ".join(consistency_check["missing_fields"])
            print(f"  Missing fields: {missing}")
            return Decision.BLOCK_REQUIRED_UPLOADS


# Example usage
async def main():
    """Example workflow execution"""
    # Simulate employer uploading documents
    documents = [
        Document(content="Job description document", document_type="job_description"),
        Document(content="Beneficiary information", document_type="beneficiary_info"),
        Document(content="Company details", document_type="company_info"),
    ]
    
    # Initialize orchestrator
    orchestrator = ControlOrchestratorAgent()
    
    # Execute workflow
    decision = await orchestrator.process_documents(documents)
    
    return decision


if __name__ == "__main__":
    # Run the workflow
    result = asyncio.run(main())
    print(f"\nWorkflow completed with decision: {result.value}")
