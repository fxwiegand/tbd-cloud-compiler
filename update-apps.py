import os
import yaml

with open("_config.yml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

apps = []
for file in os.listdir("ctag-tbd/spiffs_image/data/sp"):
    if file.endswith(".jsn") and file.startswith("mp-"):
        apps.append(file[3:-4])

data["apps"] = sorted(apps)

with open("_config.yml", 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
