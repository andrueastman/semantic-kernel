# Copyright (c) Microsoft. All rights reserved.

from enum import Enum

from semantic_kernel.utils.experimental_decorator import experimental_class


@experimental_class
class BedrockAgentEventType(str, Enum):
    """Bedrock Agent Event Type."""

    # Contains the text response from the agent.
    CHUNK = "chunk"
    # Contains the trace information (reasoning process) from the agent.
    TRACE = "trace"
    # Contains the function call requests from the agent.
    RETURN_CONTROL = "returnControl"
    # Contains the files generated by the agent using the code interpreter.
    FILES = "files"
