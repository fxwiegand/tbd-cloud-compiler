# Motivation

Using the _ctag-tbd_ for playing back samples is a wonderful thing.
Memory for samples is sadly limited by the overall ROM of the ESP32 and also the size of the _ctag-tbd_ firmware.
The _tbd-cloud-compiler_ allows users to reduce the size of the _ctag-tbd_ firmware, therefore making up more free space for samples, by removing one or multiple individual apps that they do not want to use with their module.

# Usage

The _tbd-cloud-compiler_ tries to make it as easy as possible for the user to free up more space for samples.
Following these steps should guide you through the process of generating your own custom tbd firmware:

1. If you don't already own a GitHub account go and create one. It is fully free and should be fairly easy.
2. [Create a fork](https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo) of the [_ctag-tbd_ repository](https://github.com/ctag-fh-kiel/ctag-tbd) by clicking on the corresponding button on the top right.
3. Make sure GitHub Actions are activated for your fork by going to the corresponding tab at your fork and clicking on the green button.
4. [Generate an OAuth-Token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) for your account that will allow you to trigger workflows for your repositories.
5. Open the [_tbd-cloud-compiler_](https://fxwiegand.github.io/tbd-cloud-compiler/) and select the apps you want to include in your firmware, enter the url of your _ctag-tbd_ fork and the OAuth token.
6. Click on compile firmware and download it once it's ready.
7. Flash the firmware to your _ctag-tbd_ and enjoy your newly acquired memory for samples. Make sure to flash the firmware via USB using the [ESP Tool](https://github.com/espressif/esptool). This is necessary because bootloader and the overall memory partition also need to be updated which is not possible via the web uui. 
