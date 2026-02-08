"""Tests for the Trajnor REPL."""

import pytest
from unittest.mock import patch, MagicMock
from src.trajnor.repl import create_agent, run_repl
from pydantic_ai import Agent


def test_create_agent():
    """Test that create_agent returns a properly configured Agent."""
    agent = create_agent()
    
    # Check that it's an Agent instance
    assert isinstance(agent, Agent)


def test_create_agent_uses_test_model():
    """Test that the agent uses TestModel."""
    agent = create_agent()
    
    # Run a simple test to ensure the agent works
    result = agent.run_sync("Hello")
    
    # TestModel returns a result
    assert result.output is not None


@patch("builtins.input")
@patch("builtins.print")
def test_run_repl_exit_command(mock_print, mock_input):
    """Test that the REPL exits on 'exit' command."""
    # Simulate user typing 'exit'
    mock_input.side_effect = ["exit"]
    
    run_repl()
    
    # Check that goodbye message was printed
    assert any("Goodbye!" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_run_repl_quit_command(mock_print, mock_input):
    """Test that the REPL exits on 'quit' command."""
    # Simulate user typing 'quit'
    mock_input.side_effect = ["quit"]
    
    run_repl()
    
    # Check that goodbye message was printed
    assert any("Goodbye!" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_run_repl_keyboard_interrupt(mock_print, mock_input):
    """Test that the REPL handles KeyboardInterrupt gracefully."""
    # Simulate Ctrl+C
    mock_input.side_effect = KeyboardInterrupt()
    
    run_repl()
    
    # Check that goodbye message was printed
    assert any("Goodbye!" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_run_repl_empty_input(mock_print, mock_input):
    """Test that the REPL skips empty input."""
    # Simulate empty input followed by exit
    mock_input.side_effect = ["", "exit"]
    
    run_repl()
    
    # Should exit gracefully without errors
    assert any("Goodbye!" in str(call) for call in mock_print.call_args_list)


@patch("builtins.input")
@patch("builtins.print")
def test_run_repl_processes_input(mock_print, mock_input):
    """Test that the REPL processes user input through the agent."""
    # Simulate user input and then exit
    mock_input.side_effect = ["Hello, agent!", "exit"]
    
    run_repl()
    
    # Check that welcome message was printed
    assert any("Welcome to Trajnor REPL!" in str(call) for call in mock_print.call_args_list)
    
    # Check that agent response was printed (should contain "Agent:")
    agent_responses = [str(call) for call in mock_print.call_args_list if "Agent:" in str(call)]
    assert len(agent_responses) > 0


@patch("builtins.input")
@patch("builtins.print")
@patch("src.trajnor.repl.create_agent")
def test_run_repl_handles_agent_error(mock_create_agent, mock_print, mock_input):
    """Test that the REPL handles agent errors gracefully."""
    # Create a mock agent that raises an error
    mock_agent = MagicMock()
    mock_agent.run_sync.side_effect = RuntimeError("Test error")
    mock_create_agent.return_value = mock_agent
    
    # Simulate user input and then exit
    mock_input.side_effect = ["Test input", "exit"]
    
    run_repl()
    
    # Check that error message was printed
    assert any("Error:" in str(call) for call in mock_print.call_args_list)
