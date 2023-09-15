import json
import yaml


def get_config():
    configs = None
    with open("config.yaml", "r") as stream:
        try:
            configs = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return configs

configs = get_config()
f = open(configs["output_json"], encoding="utf-8")
y = json.load(f)
w = open(configs["converted_json"], "w")
i=0
j=0
for line in y["blocks"]:
  j=0
  for item in y["blocks"][i]["textlines"]:
    print(y["blocks"][i]["textlines"][j])
    w.writelines(y["blocks"][i]["textlines"][j] + '\n')
    j += 1
  i +=1

# close file
f.close()
w.close()


