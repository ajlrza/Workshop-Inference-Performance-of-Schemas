```python
    schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["background", "general", "avatar", "position", "world", "x", "y"],
        "properties": {
            "background": {
                "type": "string",
                "description": "Visual novel background. Asset ID or filename of the background image (e.g., 'bg_classroom_evening'). Do not output image data."
            },
            "general": {"$ref": "#/$defs/generalState"},
            "avatar": {"$ref": "#/$defs/avatarState"},
            "position": {"$ref": "#/$defs/positionState"},
            "world": {"$ref": "#/$defs/worldState"},
            "x": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Context importance coordinate. Must be a plain decimal number between 0.00 and 1.00 (e.g., 0.55). Do not use scientific notation, NaN, or text. X coordinate -> memoryspace"
            },
            "y": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Context relevance coordinate. Must be a plain decimal number between 0.00 and 1.00 (e.g., 0.55). Do not use scientific notation, NaN, or text. Y coordinate -> memoryspace"
            }
        },
        "$defs": {
            "generalState": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "StateLinker", "StateOne", "StateTwo", "StateThree"],
                "description": "General narrative state for the current scene.",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique ID for this general state (e.g., 'general_012')."
                    },
                    "StateLinker": {
                        "type": ["string", "null"],
                        "description": "ID of the previous generalState this one continues from, or null if this is the first state."
                    },
                    "StateOne": {"type": "string", "description": "First general state value."},
                    "StateTwo": {"type": "string", "description": "Second general state value."},
                    "StateThree": {"type": "string", "description": "Third general state value."}
                }
            },
            "avatarState": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "StateLinker", "Expression", "Sprite"],
                "description": "Current state of the on-screen character.",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique ID for this avatar state (e.g., 'avatar_012')."
                    },
                    "StateLinker": {
                        "type": ["string", "null"],
                        "description": "ID of the previous avatarState this one continues from, or null if this is the first state."
                    },
                    "Expression": {
                        "type": "string",
                        "description": "Character's facial expression (e.g., 'smiling', 'surprised', 'angry')."
                    },
                    "Sprite": {"$ref": "#/$defs/avatarSprite"}
                }
            },
            "avatarSprite": {
                "type": "object",
                "additionalProperties": False,
                "required": ["width", "height", "pixels", "z_buffer", "channel"],
                "description": "Sprite image metadata for the avatar.",
                "properties": {
                    "width": {"type": "integer", "minimum": 1, "description": "Sprite width in pixels."},
                    "height": {"type": "integer", "minimum": 1, "description": "Sprite height in pixels."},
                    "pixels": {
                        "type": "string",
                        "description": "Asset ID or path of the sprite image (e.g., 'sprites/alice_smile.png'). Do not output raw pixel data."
                    },
                    "z_buffer": {
                        "type": ["number", "null"],
                        "description": "Optional draw-order depth. Higher draws in front. Use null if not needed."
                    },
                    "channel": {
                        "type": ["integer", "null"],
                        "description": "Optional number of color channels (3 = RGB, 4 = RGBA). Use null if not needed."
                    }
                }
            },
            "positionState": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "StateLinker", "x", "y", "z"],
                "description": "On-screen position of the avatar.",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique ID for this position state (e.g., 'position_012')."
                    },
                    "StateLinker": {
                        "type": ["string", "null"],
                        "description": "ID of the previous positionState this one continues from, or null if this is the first state."
                    },
                    "x": {"type": "number", "description": "Horizontal position."},
                    "y": {"type": "number", "description": "Vertical position."},
                    "z": {"type": "number", "description": "Depth / layer position."}
                }
            },
            "worldState": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "StateLinker", "Event", "Variables"],
                "description": "Global world state for the story.",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique ID for this world state (e.g., 'world_012')."
                    },
                    "StateLinker": {
                        "type": ["string", "null"],
                        "description": "ID of the previous worldState this one continues from, or null if this is the first state."
                    },
                    "Event": {
                        "type": "string",
                        "description": "The current story event (e.g., 'festival_night_begins')."
                    },
                    "Variables": {
                        "type": "array",
                        "description": "World variables as key/value pairs (e.g., [{'key': 'weather', 'value': 'rain'}]).",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["key", "value"],
                            "properties": {
                                "key": {"type": "string"},
                                "value": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }
    ```