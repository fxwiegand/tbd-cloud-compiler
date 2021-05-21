<h1>Welcome to the ctag-cloud-compiler</h1>

<p>You can compile custom firmware for your ctag-tbd that only contains the apps you need in order to have more room for samples on your module.</p>

<h1>Apps</h1>

<form>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
      <label class="form-check-label" for="flexSwitchCheckDefault">freeverb</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
      <label class="form-check-label" for="flexSwitchCheckDefault">BBeats</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
      <label class="form-check-label" for="flexSwitchCheckDefault">Dust</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
      <label class="form-check-label" for="flexSwitchCheckDefault">EChorus</label>
    </div>
    <label for="basic-url" class="form-label">Your ctag-tbd fork</label>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon3">https://github.com/</span>
      <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" placeholder="cnorris/ctag-tbd">
    </div>
    <div class="mb-3">
        <label for="oauth-help" class="form-label">GitHub OAuth token</label>
        <input type="text" class="form-control" id="oauth-token" aria-describedby="oauth-help">
        <div id="oauth-help" class="form-text">This token will be needed to trigger the GitHub Action in your fork to build the firmware. Generating such a token is described in the <a target="_blank" href="https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token">GitHub docs</a>.</div>
    </div>
    <button type="submit" class="btn btn-primary">Compile Firmware</button>
</form>

