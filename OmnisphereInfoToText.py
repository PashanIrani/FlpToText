import re
import xml.etree.ElementTree as ET
import glob
import argparse
import datetime, os

""" I know this code be written better, but I had to be FAST!"""
def run(args):
    try:
        out = open(args.input, 'w')
    except AttributeError:
        out = open('OmniPresetsToText.txt', 'w')

    pattern = re.compile('<ENTRYDESCR  name=')

    out.write("Omnishpere presets in .flp files from " + os.path.dirname(os.path.realpath(__file__)) + " written on [" + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + "]\n\n")
    out.write("~ A Program created by Pashan\n")
    out.write("https://github.com/PashanIrani/OmnispherePresetInfoToText.git\n\n")

    for filename in glob.glob("*.flp"):
        flp = open(filename, "r")

        list = ""

        for line in flp:

            matchFound = pattern.match(line)
            if matchFound:
                el = ET.fromstring(line + "</ENTRYDESCR>")
                if el.attrib['name'] != "" and el.attrib['name'] != 'Default':
                    presetName = "\t- " + str(el.attrib['name']) + "\n"

                    list = list + presetName

        if list != "":
            out.write(filename + ':\n' + list + "\n")

        print('Done: ' + filename + "")


def main():
    parser = argparse.ArgumentParser(description="Gets Omnishpere plugin names from .flps and outputs to a text file")
    parser.add_argument("-out",help="name of output file" , dest="output", type=str, required=False, default='OmniPresetsToText.txt')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()