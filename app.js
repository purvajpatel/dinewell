const restrictions = document.getElementsByName('restrictions');
const submit_var = document.getElementById('SUBMIT');
var result = document.getElementById('result');

const url = "http://127.0.0.1:5000/"
const proxy = "https://cors-anywhere.herokuapp.com/";
let len = restrictions.length;
let res = "";
let dict = [];
submit_var.addEventListener('click', function() {
    res = "";
    for(var i = 0; i < len ; i++) {
       if(restrictions[i].type === 'checkbox') {
           if(restrictions[i].checked) {
               res += "1";
           } else {
               res += "0";
           }
       }
    }
    
    dict = get_food(res);
    
})

function get_food(res) {
    food = {};
    $.get( url + res, function( data, status ) {
        var str = " "
        Object.keys(data).forEach((key) => {
            if(!data[key].includes("No")) {
                str += data[key] + "     ";
            }
        });
        result.innerHTML = "<pre>" + str + "</pre>";
      });
    return food;
   
}