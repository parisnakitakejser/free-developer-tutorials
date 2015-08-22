function checkAll() {
	$('.checkbox').prop('checked', true);
}

function uncheckAll() {
	$('.checkbox').prop('checked', false);
}

function flipAll() {
	$.each($('.checkbox'), function(index, value) {
		$(this).prop('checked', !$(this).prop('checked'));\"\"
	})
}