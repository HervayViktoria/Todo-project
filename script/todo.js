//check off specific todos by clicking
$("ul").on("click","li", function(){ //when an LI is clicked inside of a UL run this code, ez segít abban, hogy a jövőbeli LI-okon is működjön a kód---az a lényeg, hogy az elején olyan elementhez kell hozzáadni ami már a legelején is létezik és majd esetleg adunk hozzá új dolgokat
	
	$(this).toggleClass("checkOff");
	
	
});
 /*
 Toggle mögött ez a logika!
 
 $("li").click(function(){
	//if li is gray
	if($(this).css("color") === "rgb(128, 128, 128)"){ //az rgb colorCode-ot kell használni a hasonlításhoz, egyébként nem működik
		//turn is black
		$(this).css({
			color: "black",
			textDecoration: "line-through"
		
		});
	
	}else{
	
		$(this).css({
			color: "gray",
			textDecoration: "line-through" //lehet bele object-et tenni key-value párokkal, de csak a camelCase működik benne! 
		});
	}


});*/
 
 //click on X to delete Todo
$("ul").on("click","span", function(event){
	//szóval van az a probléma, hogy a span benne van az li-ben az ulben a bodyban, és ha mindre van téve mondjuk egy click event akkor szép sorban megtörténik pedig te csak azt akarod tiggerelni ami a spanre van állítba, ebben segít ez:
	
	event.stopPropagation();
	//span clicked li removed, but first fadeOut to be nicer
	$(this).parent().fadeOut(500,function(){
		 $(this).remove();
			
	});

});
//new todo hozzáadása!! 
$("input[type='text']").on("keypress", function(event){
	if(event.which === 13){ //event.keyCode vanillaJS-ben
		//először ki kell nyerni a value-t az input mezőből
		var todoText = $(this).val();
		//create a new li and append to ul--először ki kell választanai a ul-t és hozzáfűzni a html-t magával az infóval
		$("ul").append("<li title='Click to cross out'><span><i class='fa fa-trash' title='Delete'></i></span> " + todoText + "</li>");
		$(this).val("");

	}
//VAnillaJS: 
/*
var newItem = input.value;
		//megcsinálod az új li-t vagy akármit tulajdonképpen
	var newLi = document.createElement("li");
	aztán ahhoz hozzáadod a kinyert infot, valami NODE-izét kell kreálni..
	newLi.appendChild(document.createTextNode(newItem));
	//utána magához az ul-hez is hozzá kell adni
		ul.appendChild(newLi);

*/
	
});

//if the mouse hover over the input, input gets blue border
/*$("input").hover(function(){
		
	$(this).toggleClass("hoverEffect");
});*/

//ha a plusz  ikonra kattintunk akkor az inputnak el kell tűnni illetve meg kell jelenni
$(".fa-plus").click(function(){
		$("input[type='text']").fadeToggle();
});