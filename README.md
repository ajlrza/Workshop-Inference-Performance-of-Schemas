# Is Constrained Narrating Reliable for Multimodal Visual Novels? An Evaluation of Schematic Input Performance in MLLMs
> Submission Plan: NAACL SRW 2027 (Student Research Workshop at NAACL 2027)

## Abstract

Visual novels are often combined with text and images. Each components in a visual novel serves as parts in a multimodal reasoning. Connecting text and images could introduce concerns in inference. In the case of visual novels, balancing the "world" during inference takes up a lot of resources, especially with how rich in storytelling and narration visual novels are.

We evaluate how constrained multimodal schemas affect multi-turn dialogue and world-state consistency in 2D visual novel worlds across static and dynamic narration modes, analyzing both structured output reliability and decoding overhead. With Qwen3 - 8B and 14B

---

## Experimental Setup

Two visual novel world complexities are tested according to connections within the visual novel. Where each of them are processed with 10 turns.

| # | Mode    | Character Sprites | Background Images | Character Dialogues | Turns |
|---|---------|:-----------------:|:-----------------:|:-------------------:|:-----:|
| 1 | Static  | 5                 | 3                 | 5                   | 10    |
| 2 | Dynamic | 5                 | 3                 | 5                   | 10    |

### Modes

**Static**
- Linear dialogues
- Single state tracking: character sprites, background images, character sprite static expression

**Dynamic**
- Multi-turn dialogues
- Multi state tracking: character sprites, background images, character sprite dynamic expression

### Methodology 
<img width="1024" height="506" alt="image" src="https://github.com/user-attachments/assets/878af706-071a-47e8-b6a6-79359113a924" />

