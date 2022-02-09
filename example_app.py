import hydra

from omegaconf import OmegaConf

import multiprocessing


@hydra.main(config_path='conf', config_name='config')
def example_main(cfg):
    print(OmegaConf.to_container(cfg, resolve=True))
    print(multiprocessing.cpu_count())

if __name__ == '__main__':
    example_main()
