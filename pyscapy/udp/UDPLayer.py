from scapy.all import UDP
import codecs

class UDPLayer(object):
	"""docstring for TCPLayer"""
	def __init__(self, arguments={}):
		# super(IPLayer, self).__init__()
		self.packet = None
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		self.arguments = arguments

	def make(self):
		self.packet = UDP()
		for param in self.arguments:
			if not hasattr(self.packet, param): continue 
			setattr(self.packet, param , self.arguments[param])
		return self

	def updatePacket(self, arguments={}):
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		for param in arguments:
			if not hasattr(self.packet, param): continue
			setattr(self.packet, param , arguments[param])
		return self

	def getPacket(self):
		return self.packet

	def show(self):
		return self.packet.show()

	def _getUDP(self):
		return UDP()
