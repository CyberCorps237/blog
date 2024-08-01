let Name=document.getElementById('name');
let Email=document.getElementById('email');
let Phone=document.getElementById('phone');
let Message=document.getElementById('message');
const forms = document.querySelector('form');


forms.addEventListener('submit', (e)=>{ 
    e.preventDefault();
    let nom = Name.value;
    let email = Email.value;
    let phone = Phone.value;
    let message = Message.value;
    


    let name_erreur = document.getElementById('name_erreur');
    let email_erreur = document.getElementById('email_erreur');
    let phone_erreur = document.getElementById('phone_erreur');
    let message_erreur = document.getElementById('message_erreur');
    // let email_erreur = "veiller renseigner le champ";
    // let phone_erreur = "veiller renseigner le champ";
    // let message_erreur = "veiller renseigner le champ";
    let submitErrorMessage  = "echec de l'envoi du message";

    if(nom == ''){
        
        name_erreur.innerHTML = "veiller renseigner le champ";
        name_erreur.style.color = 'red';
        e.preventDefault();
    }
    if(message == ''){
        message_erreur.innerHTML = "veiller renseigner le champ";
        message_erreur.style.color = 'red';
        e.preventDefault();
    }
    if(phone == ''){
        phone_erreur.innerHTML = "veiller renseigner le champ";
        phone_erreur.style.color = 'red';
        e.preventDefault();
    }
    if(email == ''){
        email_erreur.innerHTML = "veiller renseigner le champ";
        email_erreur.style.color = 'red';
        e.preventDefault();
    }else{
        erreur
    }
    console.log(nom,email,phone,message)
    
})