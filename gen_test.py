import torch, gc
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

filename = '/home/zyj/Module-class/damo-vilab/output/test.mp4'

success_gen = [0]

def gen_video(prompt):
    gc.collect()
    torch.cuda.empty_cache()

    pipe = DiffusionPipeline.from_pretrained("text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()

    video_frames = pipe(prompt, num_inference_steps=25, num_frames=40).frames
    video_path = export_to_video(video_frames, output_video_path=filename)

    success_gen[0] = 1
    return
