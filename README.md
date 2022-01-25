# Margaret-hydra-submitit-launcher

![GitHub Workflow Build Status](https://github.com/raphaelmeudec/margaret-hydra-submitit-launcher/workflows/Continuous%20testing/badge.svg)

A Margaret tailored Hydra submitit launcher based on [Hydra](https://hydra.cc/docs/intro/) and its [submitit-launcher plugin](https://hydra.cc/docs/plugins/submitit_launcher/).
Basically it extends the submitit-launcher plugin with defaults that make sense for Margaret.

## Install

This package can be installed from pypi:
```
pip install margaret-hydra-submitit-launcher
```

You can also install it from source:
```
git clone https://github.com/raphaelmeudec/margaret-hydra-submitit-launcher.git
cd margaret-hydra-submitit-launcher
pip install .
```

## Use

The primary use is with the `hydra-submitit-launch` command with your script name and the config type:
```
hydra-submitit-launch my_app.py dev
```

### Available configs
5 different configs are available:
- `cpu10`: 10 cpus, partition "parietal"
- `cpu40`: 40 cpus, partition "parietal"
- `cpu100`: 100 cpus, partition "parietal"
- `gpu1`: 1 gpu, 20 cpus, partition "gpu"
- `gpu2`: 2 gpu, 20 cpus, partition "gpu"

By default, all the configs select 32Gb GPUs, use a single node and use the gpu_p1 partition.

### Advanced configs
You can override the SLURM config, the same way you would with any hydra configuration.
The parameters you can override are defined in the `hydra-submitit-launcher` plugin [doc](https://hydra.cc/docs/plugins/submitit_launcher/#usage).

For example, if you want to use the gpu_p2 partition, you would need to do:
```
hydra-submitit-launch my_app.py dev hydra.launcher.setup=null hydra.launcher.partition=gpu_p2
```

## References
- Hydra: https://hydra.cc/docs/intro/
- submitit-launcher: https://hydra.cc/docs/plugins/submitit_launcher/
- submitit: https://github.com/facebookincubator/submitit
