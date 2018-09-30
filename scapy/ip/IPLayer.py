from scapy.all import IP
import codecs

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
		return self.packet

	def update_packet(self, arguments={}):
		if not isinstance(arguments, dict): return "Please provide a dictionay"
		for param in arguments:
			if not hasattr(self.packet, param): continue
			setattr(self.packet, param , arguments[param])

	# def get_src_ip(self):
	# 	return self.packet.src

	# def get_dest_ip(self):
	# 	return self.packet.dest

	# def add_or_update_src_ip(self, src):
	# 	self.packet.src = src

	# def add_or_update_dest_ip(self, dest):
	# 	self.packet.dest = dest

	def get_packet(self):
		return self.packet

	def show(self):
		self.packet.show()

a = IPLayer({'ttl': 90})
a.make()
# a.update_packet({'ttl': 909})
print(a.show())