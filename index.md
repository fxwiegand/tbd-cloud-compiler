<h1>Welcome to the tbd-cloud-compiler</h1>

<p>
The <i>tbd-cloud-compiler</i> allows users to reduce the size of the <i>ctag-tbd</i> firmware, therefore making up more free space for their beloved samples, by removing one or multiple individual apps that they don't want to use with their module. For more information take a look at the <a href="user-guide">user guide</a>.
</p>

<div class="alert alert-warning" role="alert">
  Note that the tbd-cloud-compiler is still under construction and not fully tested! 
</div>

<h1>Apps</h1>

<form>
    <div class="row">
    {% for app in site.apps %}
    <div class="col-4 mt-1">
        <div class="form-check form-switch">
          <input class="form-check-input app-checkbox" type="checkbox" id="{{ app }}">
          <label class="form-check-label" for="{{ app }}">{{ app }}</label>
        </div>
    </div>
    {% endfor %}
    </div>
    <label for="basic-url" class="form-label mt-2">Your ctag-tbd fork</label>
    <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon3">https://github.com/</span>
        <input type="text" class="form-control" id="fork-url" aria-describedby="basic-addon3" placeholder="cnorris/ctag-tbd">
    </div>
    <div class="mb-3">
        <label for="oauth-help" class="form-label">GitHub OAuth token</label>
        <input type="text" class="form-control" id="oauth-token" aria-describedby="oauth-help">
        <div id="oauth-help" class="form-text">This token will be needed to trigger the GitHub Action in your fork to build the firmware. Generating such a token is described in the <a target="_blank" href="https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token">GitHub docs</a>.</div>
    </div>
</form>
<button id="compile-button" onclick="trigger_workflow()" class="btn btn-primary" aria-describedby="button-help">
  <span id="spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true" style="display: none"></span>
  Compile Firmware
</button>
<div id="button-help" class="form-text"></div>

<script>
    function trigger_workflow() {
        let included_apps = [];
        let removed_apps = [];
        $('.app-checkbox').each(function () {
            let id = `#${this.id}`;
            if ($(id).is(":checked")) {
                included_apps.push(this.id);
            } else {
                removed_apps.push(this.id);
            }
        });
        let oauth_token = $('#oauth-token').val();
        let user = $('#fork-url').val().split('/')[0];
        let repo = $('#fork-url').val().split('/')[1];

        let workflow = "custom-build.yml";

        let url = `https://api.github.com/repos/${user}/${repo}/actions/workflows/${workflow}/dispatches`;
        let body = {
            "ref": "cloud-compiler",
            "inputs": {"apps": removed_apps.join('#')}
        };

        let auth = `token ${oauth_token}`;

        let header = {
            "Authorization": auth,
        };
  
        let help = `Your new ctag-tbd firmware will now be compiled. This will take a few minutes. You can download the firmware as an artifact from the latest run at the <a href="https://github.com/${user}/${repo}/actions" target="_blank">GitHub Actions section of your ctag-tbd fork</a>.`;

        $.ajax({
            type: "POST",
            url: url,
            headers: header,
            data: JSON.stringify(body),
            success: function() {
                $('#compile-button').removeClass( "btn-primary" );
                $('#compile-button').addClass( "btn-success" );
                $('#compile-button').text("Compiling Firmware...");
                $('#button-help').text(help);
                $('#spinner').show();
                $('#compile-button').prop('disabled', true);
                console.log('success');
            },
            error: function() {
                $('#compile-button').removeClass( "btn-primary" );
                $('#compile-button').addClass( "btn-danger" );
                console.log('error');
            }
        });
    }
</script>
