# JZ-hydra-submitit-launcher

![GitHub Workflow Build Status](https://github.com/zaccharieramzi/jz-hydra-submitit-launcher/workflows/Continuous%20testing/badge.svg)

A Jean Zay tailored Hydra submitit launcher based on [Hydra](https://hydra.cc/docs/intro/) and its [submitit-launcher plugin](https://hydra.cc/docs/plugins/submitit_launcher/).
Basically it extends the submitit-launcher plugin with defaults that make sense for Jean Zay.

## Install

This package can be installed from pypi:
```
pip install jz-hydra-submitit-launcher
```

You can also install it from source:
```
git clone https://github.com/zaccharieramzi/jz-hydra-submitit-launcher.git
cd jz-hydra-submitit-launcher
pip install .
```

## Use

The primary use is with the `hydra-submitit-launch` command with your script name and the config type:
```
hydra-submitit-launch my_app.py dev
```

## Available configs

## Advanced use


## References
- Hydra: https://hydra.cc/docs/intro/
- submitit-launcher: https://hydra.cc/docs/plugins/submitit_launcher/
- submitit: https://github.com/facebookincubator/submitit