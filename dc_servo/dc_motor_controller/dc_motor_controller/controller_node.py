#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import serial
import time
import argparse

from rclpy.node import Node
from std_msgs.msg import Float32

class DCMotorController(Node):

    def __init__(self, serial_port):
        super().__init__('controller_node')
        self.get_logger().info('Se inició el motor en ACM1.')
        self.serial_port = None
        self.serial_port_name = serial_port
        self.pose_subscriber_ = self.create_subscription(Float32, 'dc_position', self.correct_position,1)
        self.init_serial()

    def init_serial(self):
        try:
            self.serial_port = serial.Serial(
                port=self.serial_port_name,
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
            )
            time.sleep(1)  # Esperar a que el puerto se inicialice
            self.get_logger().info('UART initialized for DC motor on port: %s' % self.serial_port_name)
        except serial.SerialException as e:
            self.get_logger().error('Error initializing UART: %s' % str(e))
            raise e
    

    def correct_position(self, msg: Float32):
        self.posicion_deseada = msg.data
        command = "N1 p{} v100 O G3/n".format(self.posicion_deseada)
        self.serial_port.write(command.encode())
  
    
def main(args=None):
    parser = argparse.ArgumentParser(description='DC Motor Node')
    parser.add_argument('--serial-port', dest='serial_port', type=str, default='/dev/ttyACM0', help='Serial port name (default: /dev/ttyACM0)')
    args = parser.parse_args()

    rclpy.init(args=None)
    try:
        node = DCMotorController(args.serial_port)
        rclpy.spin(node) 
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()