import xml.etree.ElementTree as ET
import subprocess

FILE_PATH = "cheats.xml"

def parse_xml_and_execute(file_path):

    tree = ET.parse(file_path)
    root = tree.getroot()

    for game in root.findall('game'):

        name = game.find('name').text if game.find('name') is not None else "N/A"

        gameid = game.find('gameid').text if game.find('gameid') is not None else ""
        gameid_prefix = gameid[:4]  # First 4 letters from <gameid> tag 

        try:
            
            command = f'cargo run -- {gameid_prefix} cheats.xml "{name} [{gameid_prefix}].mch"'
            print('Executing ' + command + '...')
            subprocess.run(command, shell=True, capture_output=True, text=True)

        except Exception as e:
            print(f"Exception occurred: {e}")

parse_xml_and_execute(FILE_PATH)
