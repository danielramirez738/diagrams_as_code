# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=True, direction="TB" ):
    ELB("Load balancer") >> EC2("web") >> RDS("user Database")