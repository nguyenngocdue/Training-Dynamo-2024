import clr
clr.AddReference("System")  
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

import os
import shutil
from System.Windows.Forms import Application, Button, Form, Label, TextBox, CheckBox, FolderBrowserDialog, OpenFileDialog, DialogResult, ComboBox, FormBorderStyle

from pyrevit import forms
from pyrevit import script
from pyrevit import EXEC_PARAMS
from pyrevit.loader import sessionmgr
from pyrevit.loader import sessioninfo

def getFoldersInFolder(path, depth=1):
    folders = []
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        if level < depth:
            folders.extend([os.path.join(root, d) for d in dirs])
        elif level == depth:
            folders.extend([os.path.join(root, d) for d in dirs])
            break
    return folders

def getSubfolders(path):
    subfolders = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            subfolders.append(os.path.join(root, dir))
    return subfolders

def getNames(names):
    return [os.path.splitext(os.path.basename(name))[0] for name in names]

def removeDir(parentDir, nameChildrenDir):
    for p in nameChildrenDir:
        shutil.rmtree(os.path.join(parentDir, p))

def write_to_bundle(bundle_path, folder_names):
    with open(bundle_path, "w") as f:
        f.write("layout:\n")
        for name in folder_names:
            f.write("- {}\n".format(name))

parent_dir = r"C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit\Extensions\pyBIM3DM.extension\pyBIM3DM.tab"

# Define the folders to exclude
excluded_folders = ["Development.panel", "Contact.panel", "Del Tools.panel"]

# Get all panel folders at depth 1
panel_folders = getFoldersInFolder(parent_dir, depth=1)
panel_folders = [folder for folder in panel_folders if not any(excluded in folder for excluded in excluded_folders)]

# Get all subfolders of the panel folders
folders = []
for panel_folder in panel_folders:
    subfolders = getSubfolders(panel_folder)
    subfolders = [folder for folder in subfolders if not any(excluded in folder for excluded in excluded_folders)]
    folders.extend(subfolders)

# Get the current file path and panel component
current_file_path = os.path.abspath(__file__)
components = current_file_path.split("\\")
panel_component = components[-3]
folders = [folder for folder in folders if os.path.basename(folder) != panel_component]

# Get names without extensions
name_folder = getNames(folders)

# Prepare data for output (optional)
data = [[i + 1, name_folder[i], "True"] for i in range(len(name_folder))]

# Output data table (optional)
output = script.get_output()
# output.print_table(table_data=data,
#                    title="Tools Table",
#                    columns=["No.", "Tool Name", "Status"],
#                    formats=['', '', ''],
#                    last_line_style='color:blue;')

# Create a tool name
with forms.WarningBar(title='Remove Tools'):
    selFolders = forms.SelectFromList.show(folders,
                                           multiselect=True,
                                           title='Select Tools',
                                           button_name='OK'
                                           )
if not selFolders:
    forms.alert('You must check at least one option to use this tool.', exitscript=True)

selToolNames = getNames(selFolders)
bundle_path = os.path.join(parent_dir, "bundle.yaml")

if selFolders:
    removeDir(parent_dir, selFolders)
    # sessionmgr.reload_pyrevit()

# Write all folder names to bundle.yaml after removal
folders = getFoldersInFolder(parent_dir, depth=2)
toolNamesCurrent = getNames(folders)
write_to_bundle(bundle_path, toolNamesCurrent)

res = True
if EXEC_PARAMS.executed_from_ui:
    res = forms.alert('Restarting pyBIM3DM may take a few seconds and will refresh all tools. '
                      'Do you want to proceed with the restart?',
                      ok=False, yes=True, no=True)

if res:
    logger = script.get_logger()
    results = script.get_results()

    # re-load pyrevit session.
    logger.info('Reloading....')
    sessionmgr.reload_pyrevit()

    results.newsession = sessioninfo.get_session_uuid()
