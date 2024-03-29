# JZ-hydra-submitit-launcher

![GitHub Workflow Build Status](https://github.com/zaccharieramzi/jz-hydra-submitit-launcher/workflows/Continuous%20testing/badge.svg)

A Jean Zay (JZ) tailored Hydra submitit launcher based on [Hydra](https://hydra.cc/docs/intro/) and its [submitit-launcher plugin](https://hydra.cc/docs/plugins/submitit_launcher/).
Basically it extends the submitit-launcher plugin with defaults that make sense for JZ.

## Install

This package can be installed from pypi (using `--user` is required on JZ):
```
pip install --user jz-hydra-submitit-launcher
```

You can also install it from source:
```
git clone https://github.com/zaccharieramzi/jz-hydra-submitit-launcher.git
cd jz-hydra-submitit-launcher
pip install --user .
```

The main command is then installed in your local binaries.
You need to add them to your path in order for the command to be found (and avoid the error `-bash: hydra-submitit-launch: command not found`):

```
echo "export PATH=$PATH:$HOME/.local/bin" >> $HOME/.bashrc
```

Don't forget to `source $HOME/.bashrc` before using the command.

## Use

The primary use is with the `hydra-submitit-launch` command with your script name and the config type:
```
hydra-submitit-launch my_app.py dev
```

### Available configs
6 different configs are available:
- `dev`: with 2 hours, 1 gpu, and qos_gpu-dev.
- `t3`: with 20 hours, 1 gpu, and qos_gpu-t3.
- `t4`: with 100 hours, 1 gpu, and qos_gpu-t4.
- `4gpus_dev`: with 2 hours, 4 gpus, and qos_gpu-dev.
- `4gpus_t3`: with 20 hours, 4 gpus, and qos_gpu-t3.
- `4gpus_t4`: with 100 hours, 4 gpus, and qos_gpu-t4.

By default, all the configs select 32Gb GPUs, use a single node and use the gpu_p1 partition.
### Advanced configs
You can override the SLURM config, the same way you would with any hydra configuration.
The parameters you can override are defined in the `hydra-submitit-launcher` plugin [doc](https://hydra.cc/docs/plugins/submitit_launcher/#usage).

For example, if you want to use the gpu_p2 partition, you would need to do:
```
hydra-submitit-launch my_app.py dev hydra.launcher.setup=null hydra.launcher.partition=gpu_p2 hydra.launcher.cpus_per_task=3
```

In order to change the timeout on the SLURM job to for example 10 hours, you would need to do:
```
hydra-submitit-launch my_app.py base +hours=10
```
This will automatically select the right qos for you (and if you want to force a certain qos, you can always add `hydra.launcher.qos=<your-qos>`).

### Logs
Your SLURM logs are stored in the following path: `launch-dir/multirun/day-of-launch/time-of-launch/.submitit/job_array_task_id/`
This is the default from `hydra` and `submitit` and this can be changed using both the `submitit` plugin parameters (see [here](https://hydra.cc/docs/plugins/submitit_launcher/#usage)) and the `hydra` job configurations (see [here](https://hydra.cc/docs/configure_hydra/job/)). 

## References
- Hydra: https://hydra.cc/docs/intro/
- submitit-launcher: https://hydra.cc/docs/plugins/submitit_launcher/
- submitit: https://github.com/facebookincubator/submitit
- JZ docs: http://www.idris.fr/ or https://jean-zay-doc.readthedocs.io/en/latest/
