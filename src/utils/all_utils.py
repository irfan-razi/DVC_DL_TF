import yaml
import os
import json
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
logging.basicConfig(filename=os.path.join(log_dir, "running_logs.log"),
                    level=logging.INFO, filemode='a')

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"YAML file: {path_to_yaml} loaded.")
    return content


def create_directory(dirs= list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"directory is created at {dir_path}")


def save_local_df(data, data_path,index_status=False):
    data.to_csv(data_path,index=index_status)
    logging.info(f"Data is saved at {data_path}")


def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path,"w") as f:
        json.dump(report, f, indent=indentation)
    logging.info(f"Reports are saved at {report_path}.")