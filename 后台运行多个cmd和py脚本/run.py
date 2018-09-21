# encoding: utf-8
"""
@File: run.python

Created on 2018/9/21 9:49

@author: weiyd

Description:
"""
import os
import multiprocessing
import yaml

TASK_DIR = "tasks"


def get_task_path(task_dir=TASK_DIR):
    """获取指定目录下的python脚本"""
    tack_dict = dict()
    task_dir = os.path.join(task_dir, "python")
    parent_dir = os.path.join(os.getcwd(), task_dir)
    tasks_name = os.listdir(parent_dir)
    for index, task in enumerate(tasks_name):
        tack_dict[task] = os.path.join(parent_dir, task)
    return tack_dict


def get_commands():
    commands = dict()
    # path_cmd
    with open(os.path.join(os.getcwd(), TASK_DIR, "path_cmd", "path_cmd.yaml")) as yaml_file_handle:
        yaml_cmds = yaml.load(yaml_file_handle)
        if yaml_cmds is not None:
            for yaml_cmd in yaml_cmds:
                key = yaml_cmd.split(".")[:-1]
                key = "".join(key)
                commands[key] = yaml_cmd + " " + yaml_cmds[yaml_cmd]
    # python
    tasks_path = get_task_path()
    for task in tasks_path:
        key = task.split(".")[:-1]
        key = "".join(key)
        commands[key] = "python " + tasks_path[task]

    return commands


def run_command(cmd_name, cmd_body):
    cmd_handler = os.popen(cmd_body)
    LOG_DIR = "./log"
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    log_path = "log/" + cmd_name + ".log"

    with open(log_path, mode='w', encoding='utf-8') as log_handler:
        try:
            while True:
                line = cmd_handler.readline()
                # print(line, end='')
                log_handler.write(line)
                log_handler.flush()
        except Exception as err:
            log_handler.write(err)
            log_handler.flush()
    cmd_handler.close()


if __name__ == "__main__":
    cmds = get_commands()
    if len(cmds) > 0:
        pool = multiprocessing.Pool(processes=12)
        for cmd in cmds:
            # run_command(cmd, cmds[cmd])
            pool.apply_async(run_command, (cmd, cmds[cmd],))
        pool.close()
        pool.join()
