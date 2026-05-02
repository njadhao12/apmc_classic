/* Popup Open */

document.getElementById("complaintMenu").onclick=function(e){
e.preventDefault();
document.getElementById("popup").style.display="flex";
};

document.getElementById("complaintCard").onclick=function(){
document.getElementById("popup").style.display="flex";
};

/* Close Popup */

document.getElementById("closeBtn").onclick=function(){
document.getElementById("popup").style.display="none";
};

/* Submit Complaint */

document.getElementById("complaintForm").addEventListener("submit", async function(e){

e.preventDefault();

document.getElementById("msg").innerHTML="Submitting...";

let data = {
doctype:"Complaint Registration",
full_name:document.getElementById("full_name").value,
mobile_no:document.getElementById("mobile_no").value,
email:document.getElementById("email_id").value,
subject:document.getElementById("subject").value,
complaint_details:document.getElementById("details").value,
status:"Pending"
};

try{

await fetch('/api/resource/Complaint Registration',{
method:'POST',
headers:{
'Content-Type':'application/json'
},
body:JSON.stringify(data)
});

document.getElementById("msg").innerHTML="तक्रार यशस्वीरित्या नोंद झाली.";

document.getElementById("complaintForm").reset();

}catch(error){

document.getElementById("msg").style.color="red";
document.getElementById("msg").innerHTML="Error! पुन्हा प्रयत्न करा.";

}

});


/* Company Data Fetch */

async function loadCompany(){

try{

let res = await fetch('/api/resource/Company');
let data = await res.json();

if(data.data.length > 0){

document.getElementById("company_name").innerHTML=data.data[0].name;

}

}catch(err){}

}

loadCompany();