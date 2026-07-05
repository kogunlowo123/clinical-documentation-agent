"""Clinical Documentation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_transcribe_dictation():
    """Test Transcribe physician dictation into structured clinical note."""
    tools = AgentTools()
    result = await tools.transcribe_dictation(audio_source="test", note_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_suggest_codes():
    """Test Suggest ICD-10, CPT, and HCPCS codes from clinical documentation."""
    tools = AgentTools()
    result = await tools.suggest_codes(clinical_note="test", encounter_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_completeness():
    """Test Check clinical documentation for required elements and gaps."""
    tools = AgentTools()
    result = await tools.check_completeness(note_id="test", requirements="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_apply_template():
    """Test Apply a documentation template for a specific encounter type."""
    tools = AgentTools()
    result = await tools.apply_template(encounter_type="test", patient_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.clinical_documentation_agent_agent import ClinicalDocumentationAgentAgent
    agent = ClinicalDocumentationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
