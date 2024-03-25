import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import time

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher = self.create_publisher(Int32, '/broj', 1)
        timer_period = 1.0  # 1 Hz
        self.timer = self.create_timer(timer_period, self.publish_number)
        self.number = 0

    def publish_number(self):
        msg = Int32()
        msg.data = self.number
        self.publisher.publish(msg)
        self.number += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
