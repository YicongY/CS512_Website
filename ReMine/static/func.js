function submitCorpus() {
    let c = document.getElementById('inText').value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://dmserv4.cs.illinois.edu:1111/remine", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send();
    console.log(xhr);
    document.getElementById("outText").innerHTML=xhr.responseText;
}
