// Initialize the page and declare variables
var init = function(){
	$('#speed').text(0);
	$('textarea').keyup(update_speed);//update_speed	
}

var start_time = null;
var end_time;

// Calculate the current typing speed
var calc_speed = function(evt){
	if (start_time === null){
		start_time = evt.timeStamp;
		console.log(evt.timeStamp);
		return 0;
	}
	var diff = evt.timeStamp - start_time;
	var numChars = $("textarea").val().length;
	return Math.floor(60*1000*numChars/diff);
}

// Update the text area with the typing speed
var update_speed = function(evt){
	$('#speed').text(calc_speed(evt));
}

// Initialize everything
$(document).ready(init);