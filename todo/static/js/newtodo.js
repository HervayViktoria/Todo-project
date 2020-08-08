const todo = (() =>{
    const plus_sign = document.querySelector('.fa-plus');
    const input = document.getElementById("input");
    const ul = document.getElementById("ul");
    const lis = document.querySelectorAll(".li");
    const spans= document.querySelectorAll(".span");

    const host = location.host;
    const local = host.includes("localhost");
    return {
        init: () =>{
           
            todo.Load();
            todo.Create_new_input();
        },

        Load: ()=>{
            lis.forEach(item =>{
                item.addEventListener("click", event=>{
                    todo.CheckOff(item);
                });
            });

            spans.forEach(item =>{
                item.addEventListener("click", event=>{
                   event.stopPropagation();
                   todo.Delete(item);
                });
            });  
        },
        Create_new_input: ()=>{
           
                plus_sign.addEventListener('click', ()=>{
                    input.classList.toggle("display-input");
                   
                });

                input.addEventListener("keyup", e =>{
                    if ((e.keyCode === 13 &&  input.value != "")  || (e.keyCode === 66 && input.value != "")) {
                        var note = input.value;
                        todo.Ajax_for_creating_note(note);
                       
                    }
                });
                input.addEventListener("touchend", e =>{
                    if (input.value != "") {
                        var note = input.value;
                        todo.Ajax_for_creating_note(note);
                       
                    }
                });
                
        },
        Create_new_note: (id)=>{
            var span = document.createElement("span");
            span.setAttribute("class", "span");
            span.onclick = delete_element;
            var i = document.createElement("i");
            i.setAttribute("class", "fa fa-trash");
            i.setAttribute("title", "Delete");
            span.appendChild(i);
            var newLi = document.createElement("li");

            newLi.setAttribute("class", "li");
            newLi.setAttribute("data-value", id);
            newLi.onclick = check_off;
            newLi.appendChild(span);
            newLi.appendChild(document.createTextNode(input.value))
        
            ul.appendChild(newLi);
            input.value = "";


            function check_off(){
               todo.CheckOff(this);
            }

            function delete_element(){
               todo.Delete(this);
            }
        },
        CheckOff: (input)=>{
            input.classList.toggle("checkOff");
            checkedoff_ornot = input.getAttribute("class");
            id = input.getAttribute("data-value");
            if(checkedoff_ornot.includes("checkOff")){
                data =[id, 1];                
            }else{
                data = [id, 0];
            }
            console.log(data);
            todo.Ajax_for_done_or_not(data);
        },
        Delete: (input)=>{
         
           id = input.parentElement.getAttribute("data-value");
           todo.Ajax_for_delete(id);
           input.parentElement.remove();
        },
        Ajax_for_creating_note: (note_input) =>{

                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                  if (this.readyState == 4 && this.status == 200) {
                    created_note_id = this.responseText;
                    // console.log(this.responseText);
                    todo.Create_new_note(created_note_id);
                              
                  }
                };
                if(local){
                      xhttp.open("POST", "http://localhost:5000/create", true);
                }else{
                    xhttp.open("POST", "https://hervay-todo.herokuapp.com/create", true);
                }

                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send("note="+note_input+"&rnd_data="+"valami");
              
        },
        Ajax_for_done_or_not: (input)=>{
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function(){
                if (this.readyState == 4 && this.status == 200) {
                    console.log(this.responseText);
                }
            };

            if (local) {
                xhttp.open("POST", "http://localhost:5000/update", true);
            }else{
                xhttp.open("POST","https://hervay-todo.herokuapp.com/update", true);
            }

            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send("update_data="+input);
        },
        Ajax_for_delete: (id) =>{
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function(){
                if(this.readyState == 4 && this.status == 200){
                    console.log(this.responseText);
                }
            };
            if (local) {
                xhttp.open("POST", "http://localhost:5000/delete", true);
            }else{
                xhttp.open("POST", "https://hervay-todo.herokuapp.com/delete", true);
            }
        
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send("id="+id);
        }      

    }
})();



window.onload = () => {
    todo.init();
}