from inference_linear_withprompts import main

# ==========================
# CONFIGURAÇÃO
# ==========================

EXPERIMENT_NAME = "soccer_test"

PROMPT = "A soccer ball is kicked at an angle with an initial speed. The camera captures the motion from the side, showing the ball rising, reaching its peak, and descending under gravity. The scene takes place on a sunlit football field with green grass, white boundary lines, and distant goalposts visible in the background, adding depth and realism."

SAMPLE_PATH = "inference/3dmove/NoiseWarp_set_a"

MODEL_NAME = "T2V5B_blendnorm_i18000_DATASET_lora_weights"

# ==========================
# EXECUÇÃO
# ==========================

OUTPUT_MP4 = f"output/{EXPERIMENT_NAME}.mp4"

main(
    sample_path=SAMPLE_PATH,
    output_mp4_path=OUTPUT_MP4,
    prompt=PROMPT,
    degradation=0.5,
    model_name=MODEL_NAME,
    low_vram=True,
    device=None,
    noise_downtemp_interp="nearest",
    image=None,
    num_inference_steps=30,
    guidance_scale=6,
)

print(f' video gerado está em {OUTPUT_MP4}')
