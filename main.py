from inference_linear_withprompts import main

prompt = "A single apple is thrown at an angle with an initial speed. The camera captures the motion from the side, showing the apple rising, reaching its peak, and then descending under gravity. The scene takes place in a bright open field under a clear blue sky, with soft sunlight casting gentle shadows on the ground. The background shows green grass and distant trees, adding depth and realism."

config_list = [
    dict(
        z0=[6.9901, 9.3459, 5.558, -4.8493, 0.0, 0.0, 0.594, 0.7497, 0.4453],
        DT=0.02,
        METER_PER_PX=0.05,
        chosen_shape="circle",
        output_name="set_a"
    ),
    dict(
        z0=[7.2499, 9.9899, 5.4111, -2.2692, 0.0, 0.0, 1.5469, 2.6043, 0.3305],
        DT=0.02,
        METER_PER_PX=0.05,
        chosen_shape="rectangle",
        output_name="set_b"
    ),
    dict(
        z0=[7.3491, 8.542, 4.4844, -2.0627, 0.0, 0.0, 1.6509, 2.745, 0.4849],
        DT=0.02,
        METER_PER_PX=0.05,
        chosen_shape="circle",
        output_name="set_c"
    ),
]