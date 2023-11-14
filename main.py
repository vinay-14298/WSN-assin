from mininet.topo import Topo
class MyTopo( Topo ):
    def __init__(self):
        "Create a custom topology."
        Topo.__init__(self)
        host1=self.addHost('h1')
        host2=self.addHost('h2')
        host3=self.addHost('h3')
        switch1=self.addSwitch('s1')
        self.addLink(host1,switch1)
        self.addLink(switch1,host2)
        self.addLink(switch,host3)
topos={'mytopo': (lambda :MyTopo())}