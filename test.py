from all_in_one import PacketConstuctor

packet = PacketConstuctor().createIPPacket()
print(type(packet))
print(packet.show())
packet = packet.addTCP()
