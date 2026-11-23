import torch
from dataclasses import dataclass
from transformers import AutoModelForCausalLM, AutoTokenizer
from lmformatenforcer import JsonSchemaParser
from lmformatenforcer.integrations.transformers import build_transformers_prefix_allowed_tokens_fn

from profile import metrics, record, profiler


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if torch.cuda.is_available():
    print(f"GPU Count: {torch.cuda.device_count()}")
    print(f"Device Name: {torch.cuda.get_device_name(0)}")

N_TURNS = 10

MODELS = [
    "Qwen/Qwen3.5-9B",
    "Qwen/Qwen3.5-27B"
]

SCENE_IMAGE_MODEL = "Qwen/Qwen-Image-2.1 "

lapse = 0
lapse_per_mode = {"mode": "", "lapse": lapse}

for model in MODELS:

    model_infer = None
    model_tokenizer = None
    logs = {}

    previous_scene = None
    
    try:
        model_infer = AutoModelForCausalLM.from_pretrained(
            model, 
            device_map="auto",
            torch_dtype=torch.bfloat16
        ).eval()
        model_tokenizer = AutoTokenizer.from_pretrained(model)
        
    except Exception as e:
        print(e)
        print(f"Skipping {model}...")
        continue
        
    for turn in range(N_TURNS):

        messages = [
            {"role": "user", "content": image_scene_schema},
        ]
        
        inputs = tokenizer.apply_chat_template(
        	messages,
        	add_generation_prompt=True,
        	tokenize=True,
        	return_dict=True,
        	return_tensors="pt",
        ).to(model.device)
        
        outputs = model.generate(**inputs, max_new_tokens=256)
        
        sft_format = vl_chat_processor.apply_sft_template_for_multi_turn_prompts(
            conversations=conversation,
            sft_format=vl_chat_processor.sft_format,
            system_prompt="",
        )
        prompt = sft_format + vl_chat_processor.image_start_tag
        
        # 3. Prepare inputs and run inference
        pil_images = load_pil_images(conversation)
        prepare_inputs = vl_chat_processor(
            conversations=conversation, force_batchify=True
        ).to(model.device)
        
        inputs_embeds = model.prepare_inputs_embeds(**prepare_inputs)
        
        with profiler as pf:
        
            outputs = model.language_model.generate(
                inputs_embeds=inputs_embeds,
                attention_mask=prepare_inputs.attention_mask,
                pad_token_id=tokenizer.eos_token_id,
                bos_token_id=tokenizer.bos_token_id,
                eos_token_id=tokenizer.eos_token_id,
                return_dict_in_generate=True,
                max_new_tokens=512,
                do_sample=False,
            )
        
            pf.step()
        
            answer = tokenizer.decode(outputs.sequences[0].cpu().tolist(), skip_special_tokens=True)
            print(answer)


        logs[model][f"scene {turn}"] = None # empty for now as a test