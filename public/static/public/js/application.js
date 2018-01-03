jQuery(document).ready(function ($) {
    function toggleDocs(event) {

	    if (event.target && event.target.className == 'see-more--menu') {

	        var next = event.target.nextElementSibling;


	        if (next.style.display == "none") {
	            next.style.display = "block";

	        } else {
	            next.style.display = "none";
	        }
	    }
	}

	document.addEventListener('click', toggleDocs, true);
});