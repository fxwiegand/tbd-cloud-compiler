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
    <div class="mb-3">
        <div class="form-check form-switch-xl">
          <input class="form-check-input" type="checkbox" id="add-cheap-deps">
          <label class="form-check-label" for="add-cheap-deps">Automatically add apps with shared dependencies.</label>
          <div id="dep-help" class="form-text">If you choose to check this option, the tbd-cloud-compiler will check if any apps share the same (or a subset of the ) dependencies that are already used by the given apps and will add them automatically to your build.</div>
        </div>
    </div>
  <div class="mb-3">
    <select class="form-select" aria-label="select" id="platform">
      <option value="v2" selected>Regular tbd</option>
      <option value="aem">AEM</option>
      <option value="mk2">tbd mk2</option>
    </select>
    <label class="form-check-label" for="platform">Choose the platform for your firmware.</label>
  </div>
</form>
<button id="compile-button" onclick="trigger_workflow()" class="btn btn-primary" aria-describedby="button-help">Compile Firmware</button>
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
        
        let add_cheap_deps = $("#add-cheap-deps").is(":checked");
        let platform = $(#plattform).find(":selected").val();
        console.log(platform);
        console.log($("#platform").value);
       
        let oauth_token = $('#oauth-token').val();
        let user = $('#fork-url').val().split('/')[0];
        let repo = $('#fork-url').val().split('/')[1];

        let workflow = "custom-build.yml";

        let url = `https://api.github.com/repos/${user}/${repo}/actions/workflows/${workflow}/dispatches`;
        let body = {
            "ref": "cloud-compiler",
            "inputs": {"apps": removed_apps.join('#'), "deps": add_cheap_deps.toString()}
        };

        let auth = `token ${oauth_token}`;

        let header = {
            "Authorization": auth,
        };
  
        let help = `Your new ctag-tbd firmware will now be compiled. This will take a few minutes. You can download the firmware as an artifact from the latest run at the <a href="https://github.com/${user}/${repo}/actions" target="_blank">GitHub Actions section of your ctag-tbd fork</a>.`;
  
        let error_help = `<div id="error_help">Ooops, something went wrong! Please make sure that your Fork and OAuth token are both valid. You can also take a look at the <a href="user-guide">user guide</a> to check if you did everything right. If you tried everything and still face a problem please feel free to <a href="https://github.com/fxwiegand/tbd-cloud-compiler/issues/new/choose" target="_blank">open an issue</a> over at GitHub.</div>`;

        let button_success_content = `<span id="spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true" style="display: none"></span> Compiling Firmware...`;
  
        $.ajax({
            type: "POST",
            url: url,
            headers: header,
            data: JSON.stringify(body),
            success: function() {
                $('#compile-button').removeClass( "btn-primary" );
                $('#compile-button').removeClass( "btn-danger" );
                $('#compile-button').addClass( "btn-success" );
                $('#compile-button').html(button_success_content);
                $('#button-help').append(help);
                $('#spinner').show();
                $('#error_help').hide();
                $('#compile-button').prop('disabled', true);
                console.log('success');
            },
            error: function() {
                $('#compile-button').removeClass( "btn-primary" );
                $('#compile-button').addClass( "btn-danger" );
                $('#button-help').append(error_help);
                console.log('error');
            }
        });
    }
</script>
