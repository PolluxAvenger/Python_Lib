import sys
import usb.core
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "libusb-1.0.dll")
dev = usb.core.find(idVendor=0x3689, idProduct=0x3689)

dev.set_configuration()
sys.stdout.write(
    'VendorID=' + str(dev.idVendor) + '\n' +
    'Hexadecimal VendorID=' + hex(dev.idVendor) + '\n' +
    'ProductID=' + str(dev.idProduct) + '\n' +
    'Hexadecimal ProductID=' + hex(dev.idProduct) + '\n' +
    'Serial=' + str(dev.iSerialNumber) + '\n' +
    'Hexadecimal Serial=' + hex(dev.iSerialNumber) + '\n' +
    'bLength=' + str(dev.bLength) + '\n' +
    'Hexadecimal bLength=' + hex(dev.bLength) + '\n' +
    'bDescriptorType=' + str(dev.bDescriptorType) + '\n' +
    'Hexadecimal bDescriptorType=' + hex(dev.bDescriptorType) + '\n' +
    'bcdUSB=' + str(dev.bcdUSB) + '\n' +
    'Hexadecimal bcdUSB=' + hex(dev.bcdUSB) + '\n' +
    'bDeviceClass=' + str(dev.bDeviceClass) + '\n' +
    'Hexadecimal bDeviceClass=' + hex(dev.bDeviceClass) + '\n' +
    'bDeviceSubClass=' + str(dev.bDeviceSubClass) + '\n' +
    'Hexadecimal bDeviceSubClass=' + hex(dev.bDeviceSubClass) + '\n' +
    'bDeviceProtocol=' + str(dev.bDeviceProtocol) + '\n' +
    'Hexadecimal bDeviceProtocol=' + hex(dev.bDeviceProtocol) + '\n' +
    'bMaxPacketSize0=' + str(dev.bMaxPacketSize0) + '\n' +
    'Hexadecimal bMaxPacketSize0=' + hex(dev.bMaxPacketSize0) + '\n' +
    'bcdDevice=' + str(dev.bcdDevice) + '\n' +
    'Hexadecimal bcdDevice=' + hex(dev.bcdDevice) + '\n' +
    'iManufacturer=' + str(dev.iManufacturer) + '\n' +
    'Hexadecimal iManufacturer=' + hex(dev.iManufacturer) + '\n' +
    'bNumConfigurations=' + str(dev.bNumConfigurations) + '\n' +
    'Hexadecimal bNumConfigurations=' + hex(dev.bNumConfigurations) + '\n' +
    'address=' + str(dev.address) + '\n' +
    'Hexadecimal address=' + hex(dev.address) + '\n' +
    'bus=' + str(dev.bus) + '\n' +
    'Hexadecimal bus=' + hex(dev.bus) + '\n' +
    'port_number=' + str(dev.port_number) + '\n' +
    'Hexadecimal port_number=' + hex(dev.port_number) + '\n' +
    'port_numbers=' + str(dev.port_numbers) + '\n' +
    'speed=' + str(dev.speed) + '\n' +
    'Hexadecimal speed=' + hex(dev.speed) + '\n'
)

