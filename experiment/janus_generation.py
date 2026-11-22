from transformers import AutoModelForCausalLM
from janus.models import MultiModalityCausalLM, VLChatProcessor
from janus.utils.io import load_pil_images

model_path = "deepseek-ai/Janus-Pro-1B"

vl_chat_processor = VLChatProcessor.from_pretrained(model_path)
tokenizer = vl_chat_processor.tokenizer

model = MultiModalityCausalLM.from_pretrained(
    model_path, 
    device_map="auto", 
    torch_dtype=torch.bfloat16
).eval()

conversation = [
    {
        "role": "<|User|>",
        "content": "Generate a visual novel world setting. Theme: Romance, Characters: Kawasaki, Sato, Airi, Yukino, Hayama. Produce 3 background 
    },
    {"role": "Assistant", "content": ""},
]

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

with profiler() as pf:

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

    answer = tokenizer.decode(outputs.sequences[0].cpu().tolist(), skip_special_tokens=True)
    print(answer)