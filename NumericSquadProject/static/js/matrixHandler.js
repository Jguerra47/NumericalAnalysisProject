let size = 3;

const program = () => {
    var tabla="<table class=\"table table-bordered table-primary\">";
    
    tabla+="<tr><td></td>";
    for(j=0;j<size;j++){ 
        tabla+="<td>"+(j+1)+ "</td>";
    }
    tabla+="</tr>";

    const params=["X", "Y"];
    
    for(i=0;i<2;i++){
        tabla+="<tr>";
        tabla+="<td>"+params[i]+"</td>";
        for(j=0;j<size;j++){ 
            tabla+="<td><input value={{"+params[i]+"."+j+"}} style= \"background: transparent;border: none;outline: none;\" type=\"number\" name=\""+params[i]+j+"\"> </td>";
        }
        tabla+="</tr>";
    }
    tabla+="</table>";
    tabla+="{% if state == 1%}"
    tabla+="{{X.0}}";
    document.getElementById("resultado").innerHTML=tabla;
}
window.onload = program

document.getElementById("sizePlus").addEventListener("click", (e) => {
    size++;
    document.getElementById("size").innerHTML = size;
    program();
});

document.getElementById("sizeMinus").addEventListener("click", (e) => {
    if (size != 0) size--;
    document.getElementById("size").innerHTML = size;
    program();
});
