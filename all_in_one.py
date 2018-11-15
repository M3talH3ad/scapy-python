from scapy.all import *

class IPLayer(object):
	"""docstring for IPLayer"""
	"""Argument has to a dictionay of python """
	def __init__(self, arguments={}):
		# super(IPLayer, self).__init__()
		self.packet = None
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		self.arguments = arguments

	def make(self):
		self.packet = IP()
		for param in self.arguments: 
			if not hasattr(self.packet, param): continue
			setattr(self.packet, param , self.arguments[param])
		return self

	def updatePacket(self, arguments={}):
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		for param in arguments:
			if not hasattr(self.packet, param): continue
			setattr(self.packet, param , arguments[param])

	def getPacket(self):
		return self.packet

	def show(self):
		return self.packet.show()

	def addTCP(self):
		packet = TCPLayer()._getTCP()
		print(packet)
		self.packet = self.packet/packet
		return self

	def prependEther(self):
		packet = EtherLayer()._getEther()
		self.packet = packet/self.packet
		return self

	def _getIP():
		return IP()


class TCPLayer(object):
	"""docstring for TCPLayer"""
	def __init__(self, arguments={}):
		# super(IPLayer, self).__init__()
		self.packet = None
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		self.arguments = arguments

	def make(self):
		self.packet = TCP()
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

	def _getTCP(self):
		return TCP()

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

class EtherLayer(object):
	"""docstring for TCPLayer"""
	def __init__(self, arguments={}):
		# super(IPLayer, self).__init__()
		self.packet = None
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		self.arguments = arguments

	def make(self):
		self.packet = Ether()
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

	def _getEther(self):
		return Ether()

	def addIP(self):
		packet = IPLayer()._getIP()
		self.packet = self.packet/packet
		return self


class IOOperations(object):
	"""docstring for IOOperations"""
	def __init__(self, packet):
		# super(IOOperations, self).__init__()
		self.packet = packet

	def raw(self):
		return raw(self.packet)
		
	def show(self):
		return self.packet.show()

class PacketConstuctor(object):
	"""docstring for PacketConstuctor"""
	def __init__(self):
		# super(PacketConstuctor, self).__init__()
		self.arg = None

	def createIPPacket(self, arguments={}):
		return IPLayer(arguments)
	
	def createTCPPacket(self, arguments={}):
		return TCPLayer(arguments)

	def createUDPPacket(self, arguments={}):
		return UDPLayer(arguments)

	def createEtherPacket(self, arguments={}):
		return EtherLayer(arguments)	

# print(PacketConstuctor().createIPPacket())