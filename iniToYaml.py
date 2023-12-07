import argparse
import subprocess
import json
import yaml

def ini_to_yaml(ini_file, yaml_file):
    # Execute ansible-inventory command
    command = ['ansible-inventory', '-i', ini_file, '--list']
    output = subprocess.check_output(command, universal_newlines=True)

    # Convert JSON to YAML
    data = json.loads(output)
    yaml_data = yaml.dump(data, default_flow_style=False)

    # Write the YAML data to a file
    with open(yaml_file, 'w') as f:
        f.write(yaml_data)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Convert INI inventory file to YAML.')
parser.add_argument('-f', '--input-file', required=True, help='Path to the input INI inventory file')
parser.add_argument('-o', '--output-file', required=True, help='Path to the output YAML inventory file')
args = parser.parse_args()

# Convert INI to YAML
ini_to_yaml(args.input_file, args.output_file)
