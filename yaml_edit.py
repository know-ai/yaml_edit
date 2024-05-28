import argparse, re


def replace_in_yaml(file_path, save_in:str):
    
    with open(file_path, 'r') as f:
        
        lines = f.readlines()
        _newlines = ""

        for line in lines:

            __removed = line
            if not line.startswith(('project:', 'terminal:')):
                
                if len(re.sub(r"\W", "", line)) >5:
                    
                    __removed = line.replace(" -", "-").replace("- ", "-").replace('paremetric', 'parametric').lower()

            _newlines += __removed

    with open(save_in, 'w') as f:
        
        f.write(_newlines)


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-f",
        "--config-file",
        help="Path where the config.yml file is located. i.e. /home/repo/iDetectFugas-Deploy/config.yml",
        required=True,
    )
    argParser.add_argument(
        "-s",
        "--save-as",
        help="Path where the config.yml file is located. i.e. /home/repo/iDetectFugas-Deploy/config.yml",
        required=True,
    )
    args = argParser.parse_args()

    yaml_file = args.config_file
    save_as = args.save_as

    replace_in_yaml(yaml_file, save_as)




    