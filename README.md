# Agent Interaction Workflow

A simplified implementation of the multi-agent workflow for processing employer documents using IBM watsonx Orchestrate.

## Workflow Overview

1. **Employer Uploads Documents** - Documents are received by the system
2. **Control (Orchestrator) Agent** - Coordinates the workflow
3. **Parallel Processing** - Three specialized agents process documents simultaneously:
   - Job & Specialty Agent
   - Beneficiary & Status Agent
   - Employer Control & Company Agent
4. **Completeness & Consistency Agent** - Validates all processing results
5. **Control Agent Decision** - Final decision:
   - ✓ Submission Ready
   - X Block + Required Uploads

## Configuration

### IBM watsonx Orchestrate API Keys

The workflow uses IBM watsonx Orchestrate API keys. Configure them using one of these methods:

#### Option 1: Environment Variables (Recommended)

Set the following environment variables:

```bash
export WATSONX_API_KEY="your-api-key-here"
export WATSONX_PROJECT_ID="your-project-id-here"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"  # Optional
export WATSONX_INSTANCE_ID="your-instance-id-here"  # Optional
```

#### Option 2: .env File

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your actual API credentials

3. Install python-dotenv (optional):
   ```bash
   pip install python-dotenv
   ```

4. Uncomment the dotenv import in `workflow.py`:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

#### Option 3: Pass Directly to Orchestrator

```python
orchestrator = ControlOrchestratorAgent(
    api_key="your-api-key",
    project_id="your-project-id",
    url="https://us-south.ml.cloud.ibm.com",
    instance_id="your-instance-id"
)
```

## Usage

```bash
python workflow.py
```

## Structure

- `workflow.py` - Main workflow implementation with all agents
- `requirements.txt` - Dependencies
- `.env.example` - Template for environment variables
- `README.md` - This file

## Customization

You can customize the agents by:
- Modifying the `process()` methods in each agent
- Adjusting the completeness criteria in `_make_decision()`
- Adding more document types or validation rules
- Integrating with IBM watsonx Orchestrate API calls