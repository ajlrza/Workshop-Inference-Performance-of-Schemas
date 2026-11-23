```json
world_building_schema = {
    "type": "function",
    "function": {
        "name": "generate_schema_one",
        "description": "Generate 5 character sprites, 3 backgrounds, and dialogues for 5 characters.",
        "parameters": {
            "type": "object",
            "properties": {
                "Sprites": {
                    "type": "object",
                    "properties": {
                        "Character_Sprite_One": {"type": "string"},
                        "Character_Sprite_Two": {"type": "string"},
                        "Character_Sprite_Three": {"type": "string"},
                        "Character_Sprite_Four": {"type": "string"},
                        "Character_Sprite_Five": {"type": "string"},
                    },
                    "required": [
                        "Character_Sprite_One",
                        "Character_Sprite_Two",
                        "Character_Sprite_Three",
                        "Character_Sprite_Four",
                        "Character_Sprite_Five",
                    ],
                },
                "Backgrounds": {
                    "type": "object",
                    "properties": {
                        "Background_Image_One": {"type": "string"},
                        "Background_Image_Two": {"type": "string"},
                        "Background_Image_Three": {"type": "string"},
                    },
                    "required": [
                        "Background_Image_One",
                        "Background_Image_Two",
                        "Background_Image_Three",
                    ],
                },
                "Dialogues": {
                    "type": "object",
                    "properties": {
                        "Character_One_Dialogue": {"type": "string"},
                        "Character_Two_Dialogue": {"type": "string"},
                        "Character_Three_Dialogue": {"type": "string"},
                        "Character_Four_Dialogue": {"type": "string"},
                        "Character_Five_Dialogue": {"type": "string"},
                    },
                    "required": [
                        "Character_One_Dialogue",
                        "Character_Two_Dialogue",
                        "Character_Three_Dialogue",
                        "Character_Four_Dialogue",
                        "Character_Five_Dialogue",
                    ],
                },
            },
            "required": ["Sprites", "Backgrounds", "Dialogues"],
        },
    },
}

text_scene_schema = {
    "type": "function",
    "function": {
        "name": f"{character_name} scene",
        "description": "Generate the scene text description displaying the character sprite with corresponding background and dialogue.",
        "parameters": {
            "type": "object",
            "properties": {
                "sprite-image": {
                    "type": "object",
                    "properties": {
                        "character_sprite": {"type": "string"},
                    },
                    "required": [
                        "character_sprite",
                    ],
                },
                "background-image": {
                    "type": "object",
                    "properties": {
                        "background_image": {"type": "string"},
                    },
                    "required": [
                        "background_image",
                    ],
                },
                "dialogue": {
                    "type": "object",
                    "properties": {
                        "character_dialogue": {"type": "string"},
                    },
                    "required": [
                        "cCharacter_dialogue",
                    ],
                },
            },
            "required": ["sprites", "Backgrounds", "Dialogues"],
        },
    },
}

image_scene_schema = {
    "type": "function",
    "function": {
        "name": f"{character_name} scene",
        "description": "Generate the scene image displaying the character sprite with corresponding background and dialogue.",
        "parameters": {
            "type": "object",
            "properties": {
                "sprite-image": {
                    "type": "object",
                    "properties": {
                        "character_sprite": {"type": "string"},
                    },
                    "required": [
                        "character_sprite",
                    ],
                },
                "background-image": {
                    "type": "object",
                    "properties": {
                        "background_image": {"type": "string"},
                    },
                    "required": [
                        "background_image",
                    ],
                },
                "dialogue": {
                    "type": "object",
                    "properties": {
                        "character_dialogue": {"type": "string"},
                    },
                    "required": [
                        "cCharacter_dialogue",
                    ],
                },
            },
            "required": ["sprites", "Backgrounds", "Dialogues"],
        },
    },
}
```