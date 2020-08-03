const todo = (() =>{
    const plus_sign = document.querySelector('.fa-plus');
    const input = document.getElementById("input");
    const ul = document.getElementById("ul");
    return{
        init: ()=>{
            todo.Create();
            todo.Checkoff();
            
        },
        Create: ()=>{
            
            plus_sign.addEventListener("click", ()=>{
                
                input.classList.toggle("display-input");

                input.addEventListener("keyup", function(event){
                    if(event.keyCode == 13){
                        var new_li = document.createElement("li");
                        new_li.setAttribute("title", "Click to cross out");
                        new_li.setAttribute("class", "li");
                        
                        var new_i = document.createElement("i");
                        new_i.setAttribute("class", "fa fa-trash");
                        new_i.setAttribute("title", "Delete");
                        var span = document.createElement("span");
                        span.appendChild(new_i);
                        new_li.appendChild(span);
                        var new_item = input.value;
                        new_li.appendChild(document.createTextNode(new_item));
                        ul.appendChild(new_li);
                        input.value = "";

                        todo.Checkoff();
                    }
                });
             
            });
        }, 
        Checkoff: ()=>{
            let myEl = document.querySelectorAll("ul");
                myEl.map(element => {
                    element.addEventListener("click", function(event){
                        if (event.target.matches("li") ){
                        // Not really sure how you'd handle the fadeOut, probably easiest with a CSS class
                        event.target.classList.toggle("checkOff");
                        }
                    });
                });
           
            
        }
    }
})();

window.onload = ()=>{
    todo.init();
}