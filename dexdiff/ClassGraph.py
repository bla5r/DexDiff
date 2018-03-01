from androguard.core.bytecodes.dvm import DalvikVMFormat

class ClassGraph:
	def __init__(self, dexFilename):
		self.rawFile = open(dexFilename, "r")
		self.dvmRepr = dvm = DalvikVMFormat(raw.read())

	def __exit__(self):
		self.rawFile.close()
