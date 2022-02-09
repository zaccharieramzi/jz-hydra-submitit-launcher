from omegaconf import OmegaConf


def time_to_qos(timeout_hour):
    timeout_hour = int(timeout_hour)
    if timeout_hour > 20:
        qos = 't4'
    elif timeout_hour > 2:
        qos = 't3'
    else:
        qos = 'dev'

    qos = f'qos_gpu-{qos}'
    return qos

OmegaConf.register_new_resolver("qos_from_hours", time_to_qos, replace=True)
OmegaConf.register_new_resolver("cpu_from_gpu", lambda x,y: x*y, replace=True)
