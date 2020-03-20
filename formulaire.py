# import cgi
print("comment-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<html>
<head>
<title>Notre 1er projet en python 2Ginfo</title>
<script type="text/javascript">
<!--
function verif_formulaire()
{
 if(document.formulaire.nom.value == "")  {
   alert("Veuillez entrer votre nom!");
   document.formulaire.nom.focus();
   return false;
  }
 if(document.formulaire.mot_de_passe.value == "") {
   alert("Veuillez entrer votre mot de passe!");
   document.formulaire.mot_de_passe.focus();
   return false;
  }
 if(document.formulaire.courriel.value == "") {
   alert("Veuillez mettre l'@!");
   document.formulaire.courriel.focus();
   return false;
  }
 if(document.formulaire.courriel.value.indexOf('@') == -1) {
   alert("Veuillez mettre l'@!");
   document.formulaire.courriel.focus();
   return false;
  }
 if(document.formulaire.age.value == "") {
   alert("L'age doit être un nombre!");
   document.formulaire.age.focus();
   return false;
  }
 var chkZ = 1;
 for(i=0;i<document.formulaire.age.value.length;++i)
   if(document.formulaire.age.value.charAt(i) < "1"
   || document.formulaire.age.value.charAt(i) > "99")
     	 chkZ = -1;
 if(chkZ == -1) {
   alert("votre age n'est pas correcte veuillez mettre un nombre !!!");
       document.formulaire.age.focus();
   return false;
  }
}
//-->
</script>
<style>
	body {
 font-family:"trebuchet ms",sans-serif;
 font-size:90%;
 }
form {
 background-color:#FAFAFA;
 padding:10px;
 width:280px;
 }
 input {
 background-color:#FFF3F3;
 padding:3px;
 border:1px solid #F5C5C5;
 border-radius:5px;
 width:200px;
 box-shadow:1px 1px 2px #C0C0C0 inset;
}
input[type=submit], input[type=reset] {
 width:100px;
 margin-left:5px;
 box-shadow:1px 1px 1px #D83F3D;
 cursor:pointer;
 }
 button{
 background-color:#FFF3F3;
 padding:3px;
 border:1px solid #F5C5C5;
 border-radius:5px;
 width:100px;
 margin-left:5px;
 box-shadow:1px 1px 1px #D83F3D;
 cursor:pointer;
 }
</style>
</head>
<body>
<h1>Formulaire avec python </h1>
<h2> Bienvenue sur le programme </h2>
<p>Si un probleme survient lors de la navigation, signalez le ici </p>
<a href="index.py"> ici </a>
<div style="width:100%;display:block;text-align:center;">
<body>
<form name="formulaire" action="result.py" method="post" onSubmit="return verif_formulaire()">
<pre>
             Nom:<input type="text" size="40" name="nom">
          Prenom:<input type="text" size="40" name="pre">
        Courriel:<input type="text" size="40" name="courriel">
    Mot de Passe:<input type="password" size="40" name="mot_de_passe"> 
Numero telephone:<input type="number" name="numerodetelephone" placeholder="+216..">
             Age:<input type="text" size="40" name="age">
  Lieu residence:<select name="gouvernat"></br>
 				<option value="Tunis">Tunis</option>
                <option value=" Ariana">Ariana</option>
                <option value="Beja">Beja</option>
                <option value="Ben Arous">Ben Arous</option>
                <option value="Bizerte">Bizerte</option>
                <option value="Gabes">Gabes</option>
                <option value="Gafsa">Gafsa</option>
                <option value="Jendouba">Jendouba</option>
                <option value="Kairouan">Kairouan</option>
                <option value="Kasserine">Kasserine</option>
                <option value="Kébili">Kébili</option>
                <option value="Kef">Kef</option>
                <option value="Mahdia">Mahdia</option>
                <option value="Manouba">Manouba</option>
                <option value="Médenine">Médenine</option>
                <option value="Monastir">Monastir</option>
                <option value="Nabeul">Nabeul</option>
                <option value="Sfax">Sfax</option>
                <option value="Sidi bouzid">Sidi bouzid</option>
                <option value="Siliana">Siliana</option>
                <option value="Sousse">Sousse</option>
                <option value="Tataouine">Tataouine</option>
                <option value="Tozeur">Tozeur</option>
                <option value="Zaghouan">Zaghouan</option>

            </select> </br>

formulaire: <input type="submit" value="Afficher"><input type="reset" value="Tout enlever">
            <button  formaction="supprimer.py" >Supprimer</button> <button formaction="ajouter.py">Ajouter</button>
</pre>
</form>

</body>
</html>
"""
print(html)