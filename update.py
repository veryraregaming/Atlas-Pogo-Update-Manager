import subprocess
import re
from colorama import Fore, Style

def generate_ip_list(start_ip, end_ip):
    # Convert IP addresses to integer representations
    start_ip_int = int(start_ip.split(".")[-1])
    end_ip_int = int(end_ip.split(".")[-1])

    # Generate the list of IP addresses
    ip_list = []
    for ip_int in range(start_ip_int, end_ip_int + 1):
        ip_address = ".".join(start_ip.split(".")[:-1]) + f".{ip_int}"
        ip_list.append(ip_address)

    return ip_list

def get_version_from_apk(apk_file):
    # Use aapt2 tool to extract the versionName attribute
    try:
        version_output = subprocess.check_output(["aapt2", "dump", "badging", apk_file])
    except subprocess.CalledProcessError:
        print(f"Error reading APK file: {apk_file}")
        return None

    # Extract version information
    version_match = re.search(r"versionName='(\S+)'", version_output.decode("utf-8"))
    return version_match.group(1) if version_match else None

def is_device_connected(device_ip):
    try:
        output = subprocess.check_output(["adb", "devices"])
        return device_ip in output.decode()
    except subprocess.CalledProcessError:
        return False

def get_installed_version(device_ip, package_name):
    try:
        version_output = subprocess.check_output(["adb", "-s", device_ip, "shell", "dumpsys", "package", package_name])
    except subprocess.CalledProcessError:
        return None

    version_match = re.search(r"versionName=(\S+)", version_output.decode("utf-8"))
    return version_match.group(1) if version_match else None

def check_and_install_apk(device_ip, package_name, apk_file):
    if not is_device_connected(device_ip):
        subprocess.run(["adb", "connect", device_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    desired_version = get_version_from_apk(apk_file)
    installed_version = get_installed_version(device_ip, package_name)

    if installed_version and desired_version and installed_version < desired_version:
        print(f"Updating {package_name} on {device_ip} from {installed_version} to {desired_version}")
        subprocess.run(["adb", "-s", device_ip, "install", "-r", apk_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif installed_version == desired_version:
        color = Fore.RED if package_name == "com.nianticlabs.pokemongo" else Fore.BLUE
        print(f"{color}{package_name} on {device_ip} is already up to date (version {installed_version}){Style.RESET_ALL}")
    else:
        print(f"Failed to get installed version for {package_name} on device: {device_ip}")

    subprocess.run(["adb", "disconnect", device_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def reboot_device(device_ip):
    if not is_device_connected(device_ip):
        subprocess.run(["adb", "connect", device_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if is_device_connected(device_ip):
        print(f"Rebooting {device_ip}")
        try:
            subprocess.run(["adb", "-s", device_ip, "reboot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Error rebooting {device_ip}: {e}")
    else:
        print(f"Cannot reboot {device_ip}: Device not connected or failed to connect")


# Main execution
start_ip = "192.168.50.101"
end_ip = "192.168.50.134"
devices = generate_ip_list(start_ip, end_ip)

for device in devices:
    check_and_install_apk(device, "com.nianticlabs.pokemongo", "pogo.apk")
    check_and_install_apk(device, "com.pokemod.atlas", "atlas.apk")
    reboot_device(device)
