$("div#navbar li").mouseover(function(){
	$(this).addClass("active");
});

$("div#navbar li").mouseleave(function(){
	$(this).removeClass("active");
});