import hydra

from omegaconf import OmegaConf


@hydra.main(config_path='conf', config_name='config')
def example_main(cfg):
    print(OmegaConf.to_container(cfg, resolve=True))
