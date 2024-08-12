#!/usr/bin/env python3
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy

class DCMotorPositionPublisher(Node):

    def __init__(self):
        super().__init__('position_pub_node') # Inicializamos el nodo
        self.get_logger().info('Enviando posición solicitada al tópico dc_position.')
        self.posicion_numero = 0
        self.subscription = self.create_subscription(Joy,'joy', self.joy_callback, 1)
        self.imu_pub = self.create_publisher(Float32, 'dc_position', 1) # Publicamos la posición

    def joy_callback(self, msg):
        R1_pressed = msg.buttons[5]  # R1 botón que permite acceder al movimiento
        R3_left = msg.axes[2] < -0.5  # Joystick derecho izquierda
        R3_right = msg.axes[2] > 0.5  # Joystick derecho derecha

        if R1_pressed:
            self.posicion_numero = (float(self.posicion_numero))

            if R3_left:
                self.posicion_numero = self.posicion_numero + 5
            elif R3_right:
                self.posicion_numero = self.posicion_numero - 5

        msg = Float32() # Creamos un mensaje de tipo Imu
        msg.data = float(self.posicion_numero)
        self.imu_pub.publish(msg)         


def main(args=None):
    rclpy.init(args=args) # Inicializamos las comunicaciones de ROS
    node = DCMotorPositionPublisher() # Creamos un objeto de la clase ImuNode
    try: # Intentamos mantener el nodo en ejecución
        rclpy.spin(node) 
    except KeyboardInterrupt: # Si se presiona Ctrl+C, se cierra el nodo
        pass
    rclpy.shutdown() # Cerramos las comunicaciones de ROS

if __name__ == '__main__':
    main()