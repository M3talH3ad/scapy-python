from scapy.all import IP
import sys

from ..tcp.TCPLayer import TCPLayer
from ..ether.EtherLayer import EtherLayer
# print(sys.path)


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
		self.packet = self.packet/packet
		return self

	def prependEther(self):
		packet = EtherLayer()._getEther()
		self.packet = packet/self.packet
		return self

	def _getIP():
		return IP()