from omegaconf import OmegaConf

OmegaConf.register_new_resolver("multiply10", lambda x: x * 10)
