$(function(){
	var fullContainer = $(".full-container");
	var navBtns = fullContainer.find(".nav-2l a");

	var SectionHandler ={
		currentSection:null,
		sections:{},
		init:function(){
			SectionHandler.gotoSection("section_1");
			navBtns.on("click",function(e) {
				SectionHandler.gotoSection($(e.target).data("section"));
			});
		},
		gotoSection:function(id){
			var section = SectionHandler.sections[id]?SectionHandler.sections[id]:SectionHandler.sections[id]=$("#"+id);
			if(SectionHandler.currentSection){
				SectionHandler.fadeOut(SectionHandler.currentSection);
			}
			SectionHandler.fadeIn(section);
			SectionHandler.currentSection = section;
		},
		fadeOut:function(section){
			section.css("top","110%");
		},
		fadeIn:function(section){
			section.css("top","10%");
		}
	}


	SectionHandler.init();



	$.ajax({
		type: "POST",
		url: "/api/v1/account/resgister",
		data:{},
		success:function(data){
			console.log(data);
		}
	});
	
});