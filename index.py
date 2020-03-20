#import cgi
print ("comment-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<html>
<head>
<title>Signaler un probleme </title>
<script type="text/javascript">
<!--
function verif_formulaire()
{
 if(document.forms.probleme.value!=="")
   {
   pb=document.forms.probleme.value;
   alert("le probleme est: " +pb);
   document.forms.probleme.focus();
   return false;
  }
  }
  //-->
</script>
<style>
 input {
 background-color:#FFF3F3;
 padding:25px;
 border:1px solid #F5C5C5;
 border-radius:5px;
 width:400px;
 box-shadow:2px 2px 3px #C0C0C0 inset;
}
</style>
</head>
<body>
<form name="forms" method="post" onSubmit="return verif_formulaire()">
<p>Votre probleme:<input type="text" name="probleme"></br> </p>
<button>Envoyer votre probleme</button>
</from>
</body>
</html>
"""
print(html)