jQuery(document).ready(function ($) {
    function toggleDocs(event) {

	    if (event.target && event.target.className == 'see-more--menu secondary-button button-sm') {

	        var next = event.target.nextElementSibling;


	        if (next.style.display == "none") {
	            next.style.display = "block";

	        } else {
	            next.style.display = "none";
	        }
	    }
	}

	document.addEventListener('click', toggleDocs, true);
	var userFeed = new Instafeed({
        get: 'user',
        userId: '5341507967',
        accessToken: '5341507967.ba4c844.d566f98063f74ac8b1252d29feb901f0',
        limit: 6,
        // sortBy: 'random',
        resolution: 'standard_resolution',
        template: '<img src="{{image}}" class="col-xs-12 col-sm-4 padding-none" />',
      });
      console.log(userFeed);
      userFeed.run();
});