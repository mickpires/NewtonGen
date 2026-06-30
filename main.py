from inference_linear_withprompts import main

# ==========================
# CONFIGURAÇÃO
# ==========================

EXPERIMENT_NAME = "metal2_test"

PROMPT = "A metal block sliding quickly down an inclined steel ramp in a laboratory, reflections on the shiny surface, equipment and cables in the background, captured from a fixed side camera parallel to the ramp."

SAMPLE_PATH = "inference/3dmove/NoiseWarp_set_a_copy6"

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