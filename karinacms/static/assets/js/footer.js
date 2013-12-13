(function(){
	function footer(){
		// alert('here');
		var h = $('footer').height();
		var top = $(document).height() > $(window).height() ? $(document).height() -  h : $(window).height() - h;
		$('footer').css('top', top + 'px');
	}

	$(window).on('load', footer);
	$(window).on('resize', footer);
})();
