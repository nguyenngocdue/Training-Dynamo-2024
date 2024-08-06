import clr
import System
 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import*
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import Selection
from  Autodesk.Revit.UI.Selection import ISelectionFilter

import os
import shutil

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
#########################################################################
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################

username = os.getlogin()
defaultTabPath = rf'C:\Users\{username}\AppData\Roaming\pyRevit\Extensions\pyBIM3DM.extension\pyBIM3DM.tab'
typeSource = ['.py', '.dyn', '.dll']

class MainForm(System.Windows.Forms.Form):
	def __init__(self):
		self.InitializeComponent()
		self._cbbSourceFile.SelectionChangeCommitted += self.OnSourceFileChanged
		self._btnSelTabPath.Click += self.BtnSelTabPathClick
		self._btnSelIcon.Click += self.BtnSelIconClick

	def InitializeComponent(self):
		self._labelExtTab = System.Windows.Forms.Label()
		self._txtbExtTabPath = System.Windows.Forms.TextBox()
		self._btnSelTabPath = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._txtbPanel = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._cbbSourceFile = System.Windows.Forms.ComboBox()
		self._label5 = System.Windows.Forms.Label()
		self._txtbIconPath = System.Windows.Forms.TextBox()
		self._btnSelIcon = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._btnOk = System.Windows.Forms.Button()
		self._txtbBtn = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._txtbSourceFilePath = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# labelExtTab
		# 
		self._labelExtTab.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._labelExtTab.Location = System.Drawing.Point(33, 18)
		self._labelExtTab.Name = "labelExtTab"
		self._labelExtTab.Size = System.Drawing.Size(112, 23)
		self._labelExtTab.TabIndex = 0
		self._labelExtTab.Text = "Extension Tab:"
		self._labelExtTab.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# txtbExtTabPath
		# 
		self._txtbExtTabPath.Location = System.Drawing.Point(151, 20)
		self._txtbExtTabPath.Name = "txtbExtTabPath"
		self._txtbExtTabPath.Size = System.Drawing.Size(501, 20)
		self._txtbExtTabPath.TabIndex = 1
		self._txtbExtTabPath.Text = defaultTabPath
		# 
		# btnSelTabPath
		# 
		self._btnSelTabPath.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnSelTabPath.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btnSelTabPath.Location = System.Drawing.Point(658, 18)
		self._btnSelTabPath.Name = "btnSelTabPath"
		self._btnSelTabPath.Size = System.Drawing.Size(86, 23)
		self._btnSelTabPath.TabIndex = 2
		self._btnSelTabPath.Text = "Browse"
		self._btnSelTabPath.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(19, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Panel Name:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# txtbPanel
		# 
		self._txtbPanel.Location = System.Drawing.Point(125, 30)
		self._txtbPanel.Name = "txtbPanel"
		self._txtbPanel.Size = System.Drawing.Size(205, 23)
		self._txtbPanel.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(392, 30)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Button Name:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(19, 30)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 0
		self._label4.Text = "Select A File:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# cbbSourceFile
		# 
		self._cbbSourceFile.FormattingEnabled = True
		self._cbbSourceFile.Location = System.Drawing.Point(125, 30)
		self._cbbSourceFile.Name = "cbbSourceFile"
		self._cbbSourceFile.Size = System.Drawing.Size(205, 24)
		self._cbbSourceFile.Items.AddRange(System.Array[System.Object](typeSource))
		self._cbbSourceFile.SelectedIndex = 0
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(19, 30)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 0
		self._label5.Text = "Icon Path:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# txtbIconPath
		# 
		self._txtbIconPath.Location = System.Drawing.Point(125, 30)
		self._txtbIconPath.Name = "txtbIconPath"
		self._txtbIconPath.Size = System.Drawing.Size(501, 23)
		self._txtbIconPath.TabIndex = 1
		# 
		# btnSelIcon
		# 
		self._btnSelIcon.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnSelIcon.Location = System.Drawing.Point(632, 30)
		self._btnSelIcon.Name = "btnSelIcon"
		self._btnSelIcon.Size = System.Drawing.Size(86, 23)
		self._btnSelIcon.TabIndex = 2
		self._btnSelIcon.Text = "Browse"
		self._btnSelIcon.UseVisualStyleBackColor = False
		# 
		# btnCancel
		# 
		self._btnCancel.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnCancel.Location = System.Drawing.Point(498, 312)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(114, 30)
		self._btnCancel.TabIndex = 6
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = False
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# btnOk
		# 
		self._btnOk.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnOk.Location = System.Drawing.Point(628, 312)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(114, 30)
		self._btnOk.TabIndex = 7
		self._btnOk.Text = "OK"
		self._btnOk.UseVisualStyleBackColor = False
		self._btnOk.Click += self.BtnOkClick
		# 
		# txtbBtn
		# 
		self._txtbBtn.Location = System.Drawing.Point(512, 30)
		self._txtbBtn.Name = "txtbBtn"
		self._txtbBtn.Size = System.Drawing.Size(204, 23)
		self._txtbBtn.TabIndex = 3
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._txtbIconPath)
		self._groupBox1.Controls.Add(self._btnSelIcon)
		self._groupBox1.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(26, 234)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(724, 72)
		self._groupBox1.TabIndex = 5
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Icon"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Controls.Add(self._txtbPanel)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._txtbBtn)
		self._groupBox2.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(26, 60)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(724, 72)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Button"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._txtbSourceFilePath)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._cbbSourceFile)
		self._groupBox3.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(26, 140)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(724, 88)
		self._groupBox3.TabIndex = 4
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Source"
		# 
		# txtbSourceFilePath
		# 
		self._txtbSourceFilePath.Location = System.Drawing.Point(125, 59)
		self._txtbSourceFilePath.Name = "txtbSourceFilePath"
		self._txtbSourceFilePath.ReadOnly = True
		self._txtbSourceFilePath.Size = System.Drawing.Size(593, 23)
		self._txtbSourceFilePath.TabIndex = 2
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self.ClientSize = System.Drawing.Size(780, 353)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._labelExtTab)
		self.Controls.Add(self._txtbExtTabPath)
		self.Controls.Add(self._btnSelTabPath)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
		self.Name = "MainForm"
		self.RightToLeft = System.Windows.Forms.RightToLeft.No
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Revit Tool Setup"
		self.TopMost = True
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

	def OnSourceFileChanged(self, sender, e):
		selectedType = self._cbbSourceFile.SelectedItem
		if selectedType == '.py':
			self._txtbSourceFilePath.Text = ""
		elif selectedType in ['.dyn', '.dll']:
			dialog = System.Windows.Forms.OpenFileDialog()
			dialog.Filter = f"{selectedType} files (*{selectedType})|*{selectedType}|All files (*.*)|*.*"
			if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
				self._txtbSourceFilePath.Text = dialog.FileName

	def BtnSelTabPathClick(self, sender, e):
		dialog = System.Windows.Forms.FolderBrowserDialog()
		if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
			self._txtbExtTabPath.Text = dialog.SelectedPath

	def BtnCancelClick(self, sender, e):
		self.Close()

	def BtnOkClick(self, sender, e):
		panelName = self._txtbPanel.Text
		buttonName = self._txtbBtn.Text
		extTabPath = self._txtbExtTabPath.Text

		# Create panel directory
		panelDir = os.path.join(extTabPath, f"{panelName}.panel")
		os.makedirs(panelDir, exist_ok=True)

		# Create button directory inside panel directory
		buttonDir = os.path.join(panelDir, f"{buttonName}.pushbutton")
		os.makedirs(buttonDir, exist_ok=True)

		# Update bundle.yaml in BIM3DM.tab folder
		bundleFile = os.path.join(extTabPath, 'bundle.yaml')
		panelEntry = f" - {panelName}"  # Add two leading spaces
		if not os.path.exists(bundleFile):
			with open(bundleFile, 'w') as file:
				file.write(f"{panelEntry}\n")
		else:
			with open(bundleFile, 'r') as file:
				content = file.readlines()
			
			if panelEntry not in content:
				content.append(f"{panelEntry}\n")
			
			with open(bundleFile, 'w') as file:
				file.writelines(content)

		# Handle file operations based on selected file type
		selectedType = self._cbbSourceFile.SelectedItem
		sourceFilePath = self._txtbSourceFilePath.Text  # Get the selected file path from the text box

		if selectedType == '.py':
			pyFilePath = os.path.join(buttonDir, 'script.py')
			with open(pyFilePath, 'w') as pyFile:
				pyFile.write("print('Welcome to BIM3DM')")
		elif selectedType == '.dyn':
			if os.path.exists(sourceFilePath):
				destinationFilePath = os.path.join(buttonDir, os.path.basename(sourceFilePath))
				shutil.copy2(sourceFilePath, destinationFilePath)

				# Copy the original file and rename it to _script.dyn
				scriptFilePath = os.path.splitext(destinationFilePath)[0] + '_script.dyn'
				shutil.copy2(sourceFilePath, scriptFilePath)
		elif selectedType == '.dll':
			if os.path.exists(sourceFilePath):
				destinationFilePath = os.path.join(buttonDir, os.path.basename(sourceFilePath))
				shutil.copy2(sourceFilePath, destinationFilePath)

		# Copy the selected icon file into the pushbutton directory and rename it to icon.png
		iconFilePath = self._txtbIconPath.Text
		if os.path.exists(iconFilePath):
			iconDestPath = os.path.join(buttonDir, 'icon.png')
			shutil.copy2(iconFilePath, iconDestPath)

		self.Close()

	def BtnSelIconClick(self, sender, e):
		dialog = System.Windows.Forms.OpenFileDialog()
		dialog.Filter = "PNG files (*.png)|*.png|All files (*.*)|*.*"
		if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
			self._txtbIconPath.Text = dialog.FileName
f = MainForm()
Application.Run(f)
# OUT = f.va