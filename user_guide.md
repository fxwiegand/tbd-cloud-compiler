<h1 id="motivation">Motivation</h1>
<p>Using the <em>ctag-tbd</em> for playing back samples is a wonderful thing.
Memory for samples is sadly limited by the overall ROM of the ESP32 and also the size of the <em>ctag-tbd</em> firmware.
The <em>tbd-cloud-compiler</em> allows users to reduce the size of the <em>ctag-tbd</em> firmware, therefore making up more free space for samples, by removing one or multiple individual apps that they do not want to use with their module.</p>
<h1 id="usage">Usage</h1>
<p>The <em>tbd-cloud-compiler</em> tries to make it as easy as possible for the user to free up more space for samples.
Following these steps should guide you through the process of generating your own custom tbd firmware:</p>
<ol>
<li>If you don&#39;t already own a GitHub account go and create one. It is fully free and should be fairly easy.</li>
<li><a href="https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo">Create a fork</a> of the <a href="https://github.com/ctag-fh-kiel/ctag-tbd"><em>ctag-tbd</em> repository</a> by clicking on the corresponding button on the top right.</li>
<li><a href="https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token">Generate an OAuth-Token</a> for your account that will allow you to trigger workflows for your repositories.</li>
<li>Open the <a href="https://fxwiegand.github.io/tbd-cloud-compiler/"><em>tbd-cloud-compiler</em></a> and select the apps you want to include in your firmware, enter the url of your <em>ctag-tbd</em> fork and the OAuth token.</li>
<li>Click on compile firmware and download it once it&#39;s ready.</li>
<li>Flash the firmware to your <em>ctag-tbd</em> and enjoy your newly acquired memory for samples. Make sure to flash the firmware via USB using the <a href="https://github.com/espressif/esptool">ESP Tool</a>. This is necessary because bootloader and the overall memory partition also need to be updated which is not possible via the web ui.</li>
</ol>
 