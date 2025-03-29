#!/usr/bin/env python3
"""
Example plugin for Llama CLI

This example shows how to create a custom plugin for Llama CLI.
"""
import os
import sys
import typer
from rich.console import Console

# Create app
app = typer.Typer(help="Example plugin for Llama CLI")
console = Console()


@app.command("hello")
def hello_command(
    name: str = typer.Argument("world", help="Name to greet"),
    uppercase: bool = typer.Option(False, "--uppercase", "-u", help="Convert to uppercase"),
):
    """
    Say hello to someone
    
    Example:
        llama hello
        llama hello John
        llama hello John --uppercase
    """
    message = f"Hello, {name}!"
    if uppercase:
        message = message.upper()
    
    console.print(f"[bold green]{message}[/]")


@app.command("goodbye")
def goodbye_command(
    name: str = typer.Argument("world", help="Name to say goodbye to"),
    style: str = typer.Option("green", "--style", "-s", help="Text style color"),
):
    """
    Say goodbye to someone
    
    Example:
        llama goodbye
        llama goodbye John
        llama goodbye John --style red
    """
    message = f"Goodbye, {name}!"
    console.print(f"[bold {style}]{message}[/]")


def get_commands():
    """
    Return the plugin commands
    
    Returns:
        dict: Plugin commands
    """
    return {
        "hello": app,
        "goodbye": app,
    }


if __name__ == "__main__":
    # This allows the plugin to be run directly for testing
    app() 