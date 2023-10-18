import sys
import os
sys.path.insert(0, '../../ATAG/')

from atag import Atag2
from browserenv import BrowserEnv
from config.atag_config import Atag_config

#Parameters for Atag & algorithm
parameters = {
    "log_to_wandb": True,
    "online_training": False,
    "pretrained_model": None,
    "mode": "normal",
    "K": 20,
    "pct_traj": 1.0,
    "batch_size": 64,
    "model_type": "dt",
    "embed_dim": 512,
    "n_layer": 4,
    "n_head": 4,
    "activation_function": "relu",
    "dropout": 0.1,
    "learning_rate": 1e-4,
    "weight_decay": 5e-4,
    "warmup_steps": 500,
    "num_eval_episodes": 30,
    "max_iters": 5,
    "num_steps_per_iter": 100,
    "device": "cuda",
    "save_model": False,
    "stochastic": True,
    "use_entropy": False,
    "use_action_means": True,
    "online_buffer_size": 1000,
    "eval_only": False,
    "remove_pos_embs": True,
    "eval_context": 5,
    "target_entropy": False,
    "stochastic_tanh": False,
    "approximate_entropy_samples": 1000,
    "dataset_path": "final-models/training_data.json"
}

def main():
    # Config for browserEnvironment
    config = Atag_config()
    # Test environment for Browser library
    browserEnv = BrowserEnv(config)
    # ML algorithm for test generation
    atag_browser = Atag2(env=browserEnv, **parameters)

    # Train 
    atag_browser.experiment()
    browserEnv.terminate()

if __name__ == '__main__':
    main()