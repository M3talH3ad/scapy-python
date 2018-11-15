import ip
# from pyscapy.tcp.TCPLayer import TCPLayer
# from pyscapy.udp.UDPLayer import UDPLayer
# from pyscapy.ether.EtherLayer import EtherLayer

class PacketConstuctor(object):
	"""docstring for PacketConstuctor"""
	def __init__(self):
		# super(PacketConstuctor, self).__init__()
		self.arg = None

	def createIPPacket(self, arguments={}):
		return ip.IPLayer.IPLayer(arguments)
	
	# def createTCPPacket(self, arguments={}):
	# 	return TCPLayer(arguments)

	# def createUDPPacket(self, arguments={}):
	# 	return UDPLayer(arguments)

	# def createEtherPacket(self, arguments={}):
	# 	return EtherLayer(arguments)