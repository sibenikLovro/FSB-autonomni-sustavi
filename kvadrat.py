import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SubscriberPublisherNode(Node):
    def __init__(self):
        super().__init__('subscriber_publisher_node')
        self.subscription = self.create_subscription(
            Int32, '/broj', self.callback, 1)
        self.publisher = self.create_publisher(Int32, '/kvadrat_broja', 1)

    def callback(self, msg):
        number = msg.data
        square = number ** 2
        square_msg = Int32()
        square_msg.data = square
        self.publisher.publish(square_msg)
        self.get_logger().info('Published square of %d: %d' % (number, square))

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
