from selenium import webdriver
import time

# Set up the Safari web driver
driver = webdriver.Safari()

# Function to refresh the page a specified number of times
def refresh_page(url, refresh_interval, refresh_count):
    # Open the webpage
    driver.get(url)
    print(f"Opened {url}")

    # Loop to refresh the page the specified number of times
    for i in range(refresh_count):
        time.sleep(refresh_interval)  # Wait for the refresh interval
        driver.refresh()  # Refresh the page
        print(f"Refreshed {i+1} out of {refresh_count} times at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Close the browser after refreshing
    driver.quit()
    print("Finished refreshing and closed the browser.")

# Get user input
url_to_refresh = input("Enter the URL you want to refresh: ")
refresh_interval = int(input("Enter the refresh interval (in seconds): "))
refresh_count = int(input("Enter the number of times to refresh: "))

# Start refreshing the page
try:
    refresh_page(url_to_refresh, refresh_interval, refresh_count)
except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()