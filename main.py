from mininet.net import Mininet
from mininet.node import Controller,OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def emptyNet():
    net=Mininet(topo=None, build=False)
    info('Adding Controller\n')
    net.addController('c0')
    info('Adding hosts\n')
    h1=net.addHost('h1',ip='10.0.2.1')
    h2=net.addHost('h2',ip='10.0.2.2')
    h3=net.addHost('h3',ip='10.0.2.3')
    info('Adding switch\n')
    s1=net.addSwitch('s1',cls=OVSSwitch)
    s2=net.addSwitch('s2',cls=OVSSwitch)
    s3=net.addSwitch('s3',cls=OVSSwitch)
    net.addLink(h1,s1)
    net.addLink(h2,s2)
    net.addLink(h3,s3)
    net.addLink(s1,s2)
    net.addLink(s2,s3)
    net.addLink(s3,s1)
    info('starting network\n')
    net.start()
    s1.cmd('ifconfig s1 10.0.1.1')
    s2.cmd('ifconfig s2 10.0.1.2')
    s3.cmd('ifconfig s3 10.0.1.3')
    info('enabling spanning tree\n')
    s1.cmd('ovs-vsctl set bridge s1 stp-enable=true')
    s1.cmd('ovs-vsctl set bridge s2 stp-enable=true')
    s1.cmd('ovs-vsctl set bridge s3 stp-enable=true')
    info('* Running CLI\n')
    CLI(net)
    info('* Stopping netwrok\n')
    net.stop()
if __name__ = '__main__':
    setLogLevel('info')
    emptyNet()

