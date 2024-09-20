# Webpage Auto-Refresher

This project contains scripts to automatically refresh a webpage at specified intervals using Selenium WebDriver. Two versions of the script are provided: one using ChromeDriver and another using SafariDriver.

## Prerequisites

- Python 3.x
- Selenium package
- ChromeDriver (for `refresh.py`)
- SafariDriver (for `refresh_with_safari.py`)

## Installation

1. **Install Selenium:**
    ```sh
    pip install selenium
    ```

2. **Download ChromeDriver:**
    - Download the appropriate version of ChromeDriver for your operating system from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver` executable in a known location and update the `CHROMEDRIVER_PATH` in `refresh.py`.

3. **Enable SafariDriver:**
    - SafariDriver comes pre-installed with Safari on macOS.
    - Enable "Allow Remote Automation" in Safari's Develop menu.

## Usage

### Using ChromeDriver

1. **Edit `refresh.py`:**
    - Update the `CHROMEDRIVER_PATH` variable to the path where your `chromedriver` is located.

2. **Run the script:**
    ```sh
    python refresh.py
    ```

3. **Follow the prompts:**
    - Enter the URL you want to refresh.
    - Enter the refresh interval (in seconds).
    - Enter the number of times to refresh.

### Using SafariDriver

1. **Run the script:**
    ```sh
    python refresh_with_safari.py
    ```

2. **Follow the prompts:**
    - Enter the URL you want to refresh.
    - Enter the refresh interval (in seconds).
    - Enter the number of times to refresh.

## Example

```sh
Enter the URL you want to refresh: https://example.com
Enter the refresh interval (in seconds): 10
Enter the number of times to refresh: 5
```
The script will open the specified URL in the browser and refresh it at the specified interval for the specified number of times.

## Notes
- Ensure that the web drivers are properly installed and configured.
- For Safari, make sure "Allow Remote Automation" is enabled in the Develop menu.

## License
This project is licensed under the MIT License.