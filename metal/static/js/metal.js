$(document).ready(function() {
	// home button
	$("#home").click(function(){
		$(window).attr("location", "/");
	});

	// if we have a songspace element, fill it
	if ($("#songspace").length) {
		$.get("api/html", function(data) {
			$("#songspace").html(data);
		});
	}
});
