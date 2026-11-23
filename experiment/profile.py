# CONFIG
from torch.autograd.profiler import ProfilerActivity
from dataclasses import dataclass

@dataclass(slots=True)
class metrics():
    cuda_vram_allocated_mb: float
    cuda_max_vram_reserved_mb : float

@dataclass(slots=True)
class record():
    model_name: str
    precision_format: str
    context_len_tokens: int
    metrics: metrics

profiler = torch.profiler.profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    record_shapes=True,
    profile_memory=True,
    with_stack=True,
    with_flops=True
)