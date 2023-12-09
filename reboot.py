import subprocess
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_device(ip_address):
    try:
        result = subprocess.run(["adb", "connect", ip_address], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Connected to {ip_address}")
        else:
            logging.error(f"Failed to connect to {ip_address}: {result.stderr}")
    except Exception as e:
        logging.error(f"Error connecting to {ip_address}: {e}")

def reboot_device(ip_address):
    try:
        result = subprocess.run(["adb", "-s", ip_address, "reboot"], capture_output=True, text=True)
        if result.returncode == 0:
            logging.info(f"Reboot command sent to {ip_address}")
            time.sleep(60)  # Wait for the device to reboot
        else:
            logging.error(f"Failed to reboot {ip_address}: {result.stderr}")
    except Exception as e:
        logging.error(f"Error rebooting {ip_address}: {e}")

def main():
    reboot_option = input("Choose reboot option: (1) Reboot all devices, (2) Select devices: ")
    
    devices = [f"192.168.50.{i}" for i in range(101, 134)]
    
    if reboot_option == "1":
        for device in devices:
            connect_to_device(device)
            reboot_device(device)
        logging.info("Rebooting and connecting to all ATVs completed.")
    
    elif reboot_option == "2":
        for device in devices:
            confirmation = input(f"Do you want to reboot {device}? (yes/no): ").lower()
            if confirmation in ["yes", "y"]:
                connect_to_device(device)
                reboot_device(device)
        logging.info("Rebooting and connecting to selected ATVs completed.")
    
    else:
        logging.error("Invalid reboot option selected.")

if __name__ == "__main__":
    main()
