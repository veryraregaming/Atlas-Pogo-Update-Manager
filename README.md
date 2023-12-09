#Atlas-Pogo-Update-Manager
Atlas-Pogo-Update-Manager is a powerful tool designed to automate the updating process for Pokémon GO (Pogo) and Atlas on a fleet of devices. This tool is especially useful for managing multiple installations, ensuring that all your devices are running the version of the apps you specify.

Features
Targeted Updates: Updates Pokémon GO and Atlas to the specific versions provided in the APK files.
Automated Device Management: Connects to devices in a specified IP range and performs necessary updates and reboots.
Version Control: Determines the need for updates by comparing installed versions against the APK files provided.
User-Friendly Feedback: Utilizes colorama for color-coded output, making process monitoring intuitive and straightforward.
How It Works
The script checks the version of Pokémon GO and Atlas installed on each device against the version in the pogo.apk and atlas.apk files placed in the root directory of the project. If the installed version is older, the script automatically updates the app to the version provided in the APK file.

Setup and Usage
Preparation:

Clone the repository to your local machine.
Place your pogo.apk and atlas.apk files in the root directory of the project. These APK files are the versions to which your devices will be updated.
Requirements:

Ensure that adb (Android Debug Bridge) and aapt2 (Android Asset Packaging Tool 2) are installed and properly set up on your system.
Running the Scripts:

Execute update.py to update Pokémon GO and Atlas on your devices based on the APKs provided.
Run reboot.py for device reboots, with options for rebooting all or selected devices.
Customization:

Modify the IP range within the scripts to align with your network setup.
Contributing
Your contributions are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, feel free to open an issue or submit a pull request.

License
This project is released under the MIT License. Please see the LICENSE file for more details.