from scapy.all import *

class IOOperations(object):
	"""docstring for IOOperations"""
	def __init__(self, packet):
		# super(IOOperations, self).__init__()
		self.packet = packet


	def raw(self):
		return raw(self.packet)
		
	def show(self):
		return self.packet.show()